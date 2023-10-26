import configparser
import pandas as pd
from pypinyin import lazy_pinyin
import re

def get_config_value(config, section, option):
    try:
        value = config.get(section, option)
        return value
    except (configparser.NoSectionError, configparser.NoOptionError):
        return ""


# 解析 INI 配置文件
def parse_ini_config(ini_config_file):
    ini_config = configparser.ConfigParser()
    ini_config.read(ini_config_file, encoding="utf-8")
    return ini_config


def get_pinyin(chinese_words):
    pinyin = "".join(lazy_pinyin(chinese_words, errors='ignore'))
    return pinyin


def create_dataframe_from_ini(ini_config):
    data = []
    for section in ini_config.sections():

        tmp_list = []
        for col in ['from_group_name', 'from', 'to', 'prefix', 'fromuser']:
            tmp_list.append(get_config_value(ini_config, section, col))

        #print(tmp_list)
        data.append(tmp_list)

    #print(data)
    #print(data[:5])
    df = pd.DataFrame(data, columns=['from_group_name', 'from', 'to', 'prefix', 'fromuser'])
    df['pinyin'] = df['from_group_name'].apply(lambda x: get_pinyin(x))
    return df


import psutil
import socket
import subprocess
import time
import hashlib, base64
import requests
import json
import hmac, urllib


def send_dingtalk_message(access_token, secret, msg_text):
    url = f"https://oapi.dingtalk.com/robot/send?access_token={access_token}"

    timestamp = str(round(time.time() * 1000))
    string_to_sign = timestamp + "\n" + secret
    hmac_code = hashlib.sha256(string_to_sign.encode()).digest()
    signature = base64.b64encode(hmac_code).decode()

    headers = {"Content-Type": "application/json"}

    payload = {"msgtype": "text", "text": {"content": msg_text}, "at": {"isAtAll": False}}

    params = {"access_token": access_token, "timestamp": timestamp, "sign": signature}
    print("url:", url, "params:", params, "headers:", headers, "payload:", payload)
    response = requests.post(url, params=params, headers=headers, data=json.dumps(payload))
    result = json.loads(response.text)
    print("result:", result, "response.txt:", response.text)
    return response.text


# webhook = "Your_Webhook_URL"
# sign = "Your_Secret_Key"
# message = "Your_Message"

# response = send_dingtalk_message(webhook, sign, message)

# print(response)


def calculateSignature(secret):
    timestamp = int(time.time() * 1000)
    stringToSign = str(timestamp) + '\n' + secret
    hmacSha256 = hmac.new(secret.encode('utf-8'), stringToSign.encode('utf-8'), hashlib.sha256)
    return base64.encodebytes(hmacSha256.digest()).rstrip().decode("utf-8")


def get_timestamp_sign(secret):
    timestamp = str(round(time.time() * 1000))
    # secret = # SEC开头的
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    return (timestamp, sign)


def 获取带签URL(webhookstr, signstr):
    timestamp, sign = get_timestamp_sign(signstr)
    webhook = webhookstr + "&timestamp=" + timestamp + "&sign=" + sign
    return webhook


def 生成最终url(webhookstr, signstr, mode):

    if mode == 0:  # only 敏感字
        webhook = URL
    elif mode == 1 or mode == 2:  # 敏感字和加签 或 # 敏感字+加签+ip
        # 加签： https://oapi.dingtalk.com/robot/send?access_token=XXXXXX&timestamp=XXX&sign=XXX
        webhook = 获取带签URL(webhookstr, signstr)
    else:
        webhook = ""
        print("error! mode:   ", mode, "  webhook :  ", webhook)
    return webhook


def get_message(content, is_send_all):
    # 和类型相对应，具体可以看文档 ：https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq
    # 可以设置某个人的手机号，指定对象发送
    message = {
        "msgtype": "text",  # 有text, "markdown"、link、整体跳转ActionCard 、独立跳转ActionCard、FeedCard类型等
        "text": {
            "content": content  # 消息内容
        },
        "at": {
            "atMobiles": [
                "1862*8*****6",
            ],
            "isAtAll": is_send_all  # 是否是发送群中全体成员
        }
    }
    # print(message)
    return message


def lyy_send_ding_message(webhookstr, signstr, content, 是否图片, is_send_all):
    print("进入send_ding_message处理dd信息")
    baseurl = "https://oapi.dingtalk.com/robot/send?access_token="
    # 请求的URL，WebHook地址
    最终url = 生成最终url(baseurl + webhookstr, signstr, 1)
    # 主要模式有 0 ： 敏感字 1：# 敏感字 +加签 3：敏感字+加签+IP

    # print("最终提交的URL=: ",最终url)
    # 构建请求头部
    header = {"Content-Type": "application/json", "Charset": "UTF-8"}
    # 构建请求数据
    if 是否图片:
        msg_json = lyy_make_markdown_img_json(content)

    msg_json = get_message(content, is_send_all) if not 是否图片 else lyy_make_markdown_img_json(content)

    # 对请求的数据进行json封装
    json_str = json.dumps(msg_json)
    # 发送请求
    info = requests.post(url=最终url, data=json_str, headers=header)
    print("token=", webhookstr)
    # 打印返回的结果
    return info.text


def lyy_send_msg_json(webhookstr, signstr, msg_json):
    print("进入send_ding_message处理dd信息")
    baseurl = "https://oapi.dingtalk.com/robot/send?access_token="
    # 请求的URL，WebHook地址
    最终url = 生成最终url(baseurl + webhookstr, signstr, 1)
    # 主要模式有 0 ： 敏感字 1：# 敏感字 +加签 3：敏感字+加签+IP

    # print("最终提交的URL=: ",最终url)
    # 构建请求头部
    header = {"Content-Type": "application/json", "Charset": "UTF-8"}
    # 构建请求数据

    # 对请求的数据进行json封装
    json_str = json.dumps(msg_json)
    # 发送请求
    info = requests.post(url=最终url, data=json_str, headers=header)
    # 打印返回的结果
    return info.text

def lyy_make_markdown_img_json(content):
    message = {"msgtype": "markdown", "markdown": {"title": "。", "text": "####  \n> \n> ![screenshot](" + content + ")\n> "}, "at": {"isAtAll": False}}
    # print(message)
    return message


def get_headers_payload_params(access_token, secret, content, display=False):
    timestamp = str(round(time.time() * 1000))
    string_to_sign = timestamp + "\n" + secret
    hmac_code = hashlib.sha256(string_to_sign.encode()).digest()
    signature = base64.b64encode(hmac_code).decode()
    headers = {"Content-Type": "application/json"}
    payload = {"msgtype": "text", "text": {"content": content}, "at": {"isAtAll": False}}
    params = {"access_token": access_token, "timestamp": timestamp, "sign": signature}
    if display: print(hearders, payload, params)
    return headers, payload, params

def msg_json_from_text_or_imgurl(msg_text):
    # 定义正则表达式模式
    pattern = r'(https://|https://gchat\.qpic\.cn/0).*?\.(jpg\?auth_bizType=IM|png|jpg)$'
    if re.match(pattern, msg_text):
        print(f"匹配成功: {msg_text}")
        is_pic = True
        msg_json = message = {"msgtype": "markdown", "markdown": {"title": "[图片]", "text": "####  \n> \n> ![screenshot](" + msg_text + ")\n> "}, "at": {"isAtAll": False}}
    else:
        msg_json = { "msgtype": "text", "text": {"content": msg_text },"at": {"isAtAll": False}}
    return msg_json


if __name__ == '__main__':
    
    
    webhook = "62153505b1635f6f0a0b0ed41fb0f2e0dff5fd9373ce093be85b3f2db262012f"
    sign = "SECeba7ab6bc8fc2341a25034a5d5e703995279ebedb42455f9d4920752f3468701"
    img_str = "https://static.dingtalk.com/media/lALPD2BobLJPUpfNAs3NBME_1217_717.png"
    text1 = "这是一条测试消息，来源于lyyddforward main模块"

    msg_json = msg_json_from_text_or_imgurl(img_str)
    #result = lyy_send_ding_message(webhook, sign, text1,False,False)
    #result = lyy_send_ding_message(webhook, sign, img_str, True, False)
    result = lyy_send_msg_json(webhook, sign, msg_json)
    print(result)
    exit()
    task_dict = {'jiepan': 'D:/Soft/_lyytools/_jiepan/_jiepan.exe', 'gui-only': 'D:/Soft/_lyytools/gui-only/gui-only.exe', 'kingtrader': 'D:/Soft/_Stock/KTPro/A.点我登录.exe'}
    stopped = check_processes(task_dict)
    print("stopped=", stopped)

# if __name__ == '__main__':
    # cfg_path = r'D:\UserData\resource\ddForward'
    # ini_config_file = cfg_path + "/" + "ddForward.ini"
    # ini_config = parse_ini_config(ini_config_file)
    # df = create_dataframe_from_ini(ini_config)
    # # 打印 DataFrame
    # print(df[:5])
