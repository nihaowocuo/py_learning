# 手动将 py_learning 推送到 GitHub 指南

## 当前状态

本地已完成以下步骤：

- `git init`：初始化仓库
- `git remote add origin https://github.com/nihaowocuo/py_learning.git`：添加远程仓库
- `git add .` 与 `git commit -m "Initial commit"`：把所有文件提交到本地

只剩最后一步：**把本地提交推送到 GitHub**。

---

## 方案一：继续在当前目录里完成推送（推荐）

在你电脑本机的 CMD / PowerShell / Git Bash 里，进入项目目录：

```bash
cd E:\py_learning
```

然后执行：

```bash
git push -u origin main
```

首次推送会要求认证。

### 1.1 HTTPS 认证方式

GitHub 已不支持普通密码，需要**个人访问令牌（PAT）**：

1. 打开 https://github.com/settings/tokens
2. 点击 **Generate new token (classic)**
3. 勾选 `repo` 权限（可读写仓库）
4. 生成后复制 token
5. 在弹出的认证窗口里：
   - Username：你的 GitHub 用户名 `nihaowocuo`
   - Password：粘贴刚才复制的 token

### 1.2 SSH 认证方式（不想每次都输入 token）

如果你本地已经配置过 SSH key，可以改用 SSH 地址：

```bash
git remote set-url origin git@github.com:nihaowocuo/py_learning.git
git push -u origin main
```

如果还没配置 SSH key，需要先执行：

```bash
ssh-keygen -t ed25519 -C "你的邮箱"
cat ~/.ssh/id_ed25519.pub
```

把打印出来的公钥贴到 https://github.com/settings/keys 里。

---

## 方案二：从空仓库开始，完全手动操作

如果你希望从零开始重做一遍，可以先删除当前 `.git` 文件夹，再按 GitHub 页面提示执行：

```bash
cd E:\py_learning

# 1. 删除旧的本地仓库（可选，会丢失提交历史）
rm -rf .git

# 2. 按 GitHub 官方流程重新初始化
echo "# py_learning" > README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/nihaowocuo/py_learning.git
git push -u origin main
```

> 注意：本方案会重新生成仓库，之前的 `Initial commit` 历史会被覆盖。如果已经写好了文件，建议用方案一。

---

## 常见提示说明

- **LF will be replaced by CRLF**：这是 Windows 正常的换行符转换警告，不影响推送，可以忽略。如果想关闭，执行：
  ```bash
  git config --global core.autocrlf true
  ```
- **could not read Username**：说明没有认证，需要按上面的 HTTPS 或 SSH 方案配置。

---

## 推送成功后

浏览器打开 https://github.com/nihaowocuo/py_learning 即可看到所有文件。

以后修改了文件，只需三步同步：

```bash
git add .
git commit -m "修改说明"
git push
```
