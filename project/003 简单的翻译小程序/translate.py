# -*- coding: utf-8 -*-
# @Time    : 2018/8/12 17:02
# @Author  : HardyYao
# @FileName: translate.py
# @Software: PyCharm

import requests
import json

def translate(words):
    # 有道词典API
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    # 提交的表单数据，包含需要翻译的内容
    postData = {
        'i': words,
        'type': 'AUTO',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'typoResult': 'false'
    }
    # 将 postData 发送给有道词典网站服务器，相当于在有道词典网站输入内容->点击翻译
    response = requests.post(url, data=postData)

    # 如果返回的 status_code 为 200，则表示翻译成功
    if response.status_code == 200:
        # 返回服务器响应的文本内容
        return response.text
    else:
        print("调用有道词典API失败，请再试一遍！")
        # 失败则返回None
        return None

def get_translate_result(responseText):
    # 将文本内容加载成 json 格式
    result = json.loads(responseText)
    print("输入的词为：%s" % result['translateResult'][0][0]['src'])
    print("翻译结果为：%s" % result['translateResult'][0][0]['tgt'])

def main():
    print("本程序调用有道词典的API进行翻译，可达到以下效果：")
    print("外文-->中文")
    print("中文-->英文")
    # 利用循环，运行一次程序即可实现多个词或句的翻译
    while True:
        words = input('请输入你想要翻译的词或句：')
        transResult = translate(words)
        get_translate_result(transResult)
        flag = input('输入 y 可继续翻译其它词或句，输入其它则会退出程序！')
        if flag == 'y':
            pass
        else:
            break

if __name__ == '__main__':
    main()
