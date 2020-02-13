import socket
import requests


def get_img_url(av_id=2333):
    url = "https://api.bilibili.com/x/web-interface/view?aid="+str(av_id)

    try:
        resp = requests.get(url)
        content = resp.json()
        code = content.get("code")
        if code == 0:   # 只有code为0才表示返回数据信息正常
            data = {
                "code": 200,
                "img_url": content.get("data").get("pic"),
                "message": "查询成功"
            }
        else:
            data = {
                "code": 300,
                "img_url": "https://www.bilibili.com/",
                "message": "查无此视频号"
            }
    except BaseException:
        data = {
            "code": 400,
            "img_url": "https://www.bilibili.com/",
            "message": "信息获取失败"
        }

    return data


if __name__ == '__main__':
    print(get_img_url())