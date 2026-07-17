#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Qwen 智能助手（硅基流动 SiliconFlow 版）
==================================================
文件结构（仅保留两个文件）：
  - Task_01.py  : 调用硅基流动 Qwen 模型 + 内置 HTTP 服务器
  - index.html  : 可视化聊天界面

模型：Qwen/Qwen2.5-7B-Instruct（硅基流动公开接口验证可用）
接口：硅基流动 OpenAI 兼容的 /v1/chat/completions

运行方式：
  python Task_01.py            # 启动网页，浏览器打开 http://localhost:8000
  python Task_01.py --cli      # 命令行问答模式（输入 quit 退出，reset 清空）

API Key 配置（二选一）：
  1) 环境变量：  export SILICONFLOW_API_KEY="你的key"
  2) 或直接修改下方 API_KEY 占位符
Key 在 https://cloud.siliconflow.cn 注册后获取。
==================================================
"""

import json
import os
import sys
import threading
import urllib.request
import urllib.error
import http.server
import socketserver

# ========== 配置区（按需修改） ==========
API_KEY = os.environ.get("SILICONFLOW_API_KEY", "sk-cbjioakbduchhsjhkdjdnabxddqnnsmcrderhbdmlvuqwwkl")
MODEL = "Qwen/Qwen2.5-7B-Instruct"   # 已验证可用；如需更大可用 Qwen 可换 Qwen/Qwen3-8B
API_URL = "https://api.siliconflow.cn/v1/chat/completions"
PORT = 8000
# =======================================

# 多轮对话历史（单用户本地工具，全局维护即可）
_messages = []
_lock = threading.Lock()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_PATH = os.path.join(BASE_DIR, "index.html")


def ask(user_message):
    """调用硅基流动 Qwen 模型，返回回复文本（失败则返回错误说明）。"""
    if not user_message.strip():
        return "请输入有效内容"

    # 未配置 Key 时给出友好提示，避免盲目发起请求
    if not API_KEY or API_KEY == "YOUR_SILICONFLOW_API_KEY":
        return ("⚠️ 尚未配置硅基流动 API Key。\n"
                "请打开 Task_01.py，在顶部 API_KEY 处填入你的 Key，\n"
                "或设置环境变量 SILICONFLOW_API_KEY 后重启服务。")

    # --- 快照当前对话历史，构建请求体 ---
    # 先对共享的 _messages 做快照，再追加本次用户消息；这样做的好处是：
    #   - 如果 API 调用失败，共享历史不会被污染
    #   - 快照过程中加锁，避免多线程竞态
    with _lock:
        history_snapshot = list(_messages)
        history_snapshot.append({"role": "user", "content": user_message})

    payload = {
        "model": MODEL,
        "messages": history_snapshot,
        "stream": False,
        "temperature": 0.7,
        "max_tokens": 1024,
    }
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        API_URL,
        data=data,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            result = json.loads(resp.read().decode("utf-8"))
        reply = result["choices"][0]["message"]["content"]
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "ignore")[:300]
        return f"接口返回错误：HTTP {e.code}\n{body}"
    except urllib.error.URLError as e:
        return f"网络请求失败：{e.reason}"
    except Exception as e:
        return f"程序异常：{str(e)}"

    # --- 调用成功，把实际发生的对话写入共享历史 ---
    with _lock:
        _messages.append({"role": "user", "content": user_message})
        _messages.append({"role": "assistant", "content": reply})
    return reply


class Handler(http.server.BaseHTTPRequestHandler):
    def _send_json(self, obj, status=200):
        body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            try:
                with open(INDEX_PATH, "r", encoding="utf-8") as f:
                    html = f.read()
            except Exception:
                self.send_error(404, "index.html not found")
                return
            body = html.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        else:
            self.send_error(404)

    def do_POST(self):
        if self.path != "/api/chat":
            self.send_error(404)
            return
        try:
            length = int(self.headers.get("Content-Length", 0))
            raw = self.rfile.read(length)
            payload = json.loads(raw.decode("utf-8"))
        except Exception:
            self._send_json({"error": "请求格式错误"}, status=400)
            return

        # message 可能是任意类型（数字/对象等），统一转字符串，避免 .strip() 崩溃
        message = str(payload.get("message") or "").strip()
        if not message:
            self._send_json({"error": "请输入有效内容"}, status=400)
            return

        # 输入过长保护，避免无意义的大请求拖垮模型
        if len(message) > 8000:
            self._send_json({"error": "输入过长，请控制在 8000 字以内"}, status=400)
            return

        # 清空对话
        if message.lower() == "reset":
            with _lock:
                _messages.clear()
            self._send_json({"reply": "对话已重置。"})
            return

        # 兜底：即使 ask 内部抛出未预期异常，也保证返回 JSON 而非断开连接
        try:
            reply = ask(message)
        except Exception as e:
            reply = f"服务异常：{str(e)}"
        self._send_json({"reply": reply})

    def log_message(self, fmt, *args):
        print("[web] " + (fmt % args))


def run_cli():
    print("=" * 30)
    print("  Qwen 智能助手（命令行）")
    print("  输入 quit 退出，reset 清空对话")
    print("=" * 30, "\n")
    while True:
        try:
            user_input = input("你：")
        except (EOFError, KeyboardInterrupt):
            print("\n再见！")
            break
        if user_input.strip().lower() == "quit":
            print("\n对话结束，再见！")
            break
        if user_input.strip().lower() == "reset":
            with _lock:
                _messages.clear()
            print("（对话已清空）\n")
            continue
        reply = ask(user_input)
        print(f"Qwen：{reply}\n")


def run_web():
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    try:
        httpd = socketserver.ThreadingTCPServer(("", PORT), Handler)
    except OSError as e:
        print(f"❌ 端口 {PORT} 被占用或无法绑定：{e}")
        print(f"   请关闭占用该端口的程序，或修改 Task_01.py 顶部的 PORT 后重试。")
        return
    with httpd:
        print("=" * 42)
        print("  Qwen 智能助手 · 网页版已启动")
        print(f"  请在浏览器打开: http://localhost:{PORT}")
        print("  按 Ctrl+C 停止服务")
        print("=" * 42)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n服务已停止。")


if __name__ == "__main__":
    if "--cli" in sys.argv:
        run_cli()
    else:
        run_web()
