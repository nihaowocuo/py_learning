"""
from urllib.request import urlopen
# 响应，但里面不只有我们想要的，而是有很多的响应头等
# 此处我想要的是内容主体
response = urlopen(url)
# 从响应中读取内容
# response.read()

# 输出了一些的字节
# print(response.read())
# 我该如何将字节还原成字符串
# 给出的解码提示：charset=UTF-8"
# print(response.read().decode("utf-8"))
# 打开一个文件存储这些信息
# 注意此处的默认写入编码
# with open("my_baidu.html",mode="w",encoding="utf-8") as f:
#     f.write(response.read().decode("utf-8")) # 读取到的是网页的源代码
#
# print("over!")

request的作用，是把上述的代码进一步简化
注意：此并非py自带的模块，因此需要进行安装

"""
import requests
url = 'https://www.sogou.com/web?query=%E5%91%A8%E6%9D%B0%E4%BC%A6'
resp = requests.get(url)
print('状态码:', resp.status_code)   # 200 = 成功
print(resp.text[:500])              # 打印前 500 字符，看是不是 sogou 的 HTML

