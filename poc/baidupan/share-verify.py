import os
import requests

AppID = os.environ.get('BaiduPan_AppID')
AppKey = os.environ.get('BaiduPan_AppKey')
Secretkey = os.environ.get('BaiduPan_Secretkey')
Signkey = os.environ.get('BaiduPan_Signkey')
access_token = os.environ.get('BaiduPan_AccessToken')
print(f'access_token = {access_token}')

short_url = '1yqJ8Y40VsmWWIN1C143Z1Q'
share_verify_url = f'https://pan.baidu.com/apaas/1.0/share/verify?product=netdisk?appid={AppID}&access_token={access_token}&short_url={short_url}'
data = {
    'pwd': 'uv52'
}

response = requests.post(share_verify_url, data)
print(response.content)