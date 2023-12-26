import os
import requests
# from bs4 import BeautifulSoup
import webbrowser

AppID = os.environ.get('BaiduPan_AppID')
AppKey = os.environ.get('BaiduPan_AppKey')
Secretkey = os.environ.get('BaiduPan_Secretkey')
Signkey = os.environ.get('BaiduPan_Signkey')

print(f'AppID = {AppID}')
print(f'AppKey = {AppKey}')
print(f'Secretkey = {Secretkey}')
print(f'Signkey = {Signkey}')


authorize_url = f'http://openapi.baidu.com/oauth/2.0/authorize?response_type=code&client_id={AppKey}&redirect_uri=oob&scope=basic,netdisk&device_id={AppID}'
print(authorize_url)
webbrowser.open(authorize_url)

# It will open your default browser and show the authorize page, authorize it and you will get the access token
# then you can set the environment variable use the command below, replace the code to your own.
#    export BaiduPan_AccessToken=3bebc530a1a320b3cffb036b024d82c8

# web_data = requests.get(authorize_url)
# soup = BeautifulSoup(web_data.content, 'html.parser')
# element_input = soup.select_one('#Verifier')
# access_token = element_input['value']
# print(f'access_token = {access_token}')

# with open('a.html', 'wb') as f:
#     f.write(web_data.content)
    
    
