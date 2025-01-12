import json
import requests
import web_request

from web_request import web_url

def req_login(username, password):
    data = {"username": username, "password": password}
    result = requests.post(web_request.web_url + "/login", params=data)
    print(result.text)
    result = json.loads(result.text)

    if result['code'] == 0:
        web_request.user_token = result['data']['token']
        web_request.user_id = result['data']['userId']
        web_request.username = result['data']['username']

        return True,result['data']['token']

    else:
        return False,result['msg']
