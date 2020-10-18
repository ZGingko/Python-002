import requests
from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False)

headers = {
    'User-Agent': us.random(),
    'Referer': 'https://shimo.im/login?from=home'
}

s = requests.Session()

login_url = 'https://shimo.im/lizard-api/auth/password/login'
form_data = {
    'mobile': '+8613866666666',
    'password': 'shimopassword'
}

response = s.post(login_url, data=form_data,
                  headers=headers, cookies=s.cookies)

print(response.text)
