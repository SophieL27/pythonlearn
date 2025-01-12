import json
import requests
import web_request



def req_post_ai(data1):
    token_headers={'Authorization':'Bearer '+web_request.user_token}

    result=requests.post(web_request.web_url + "/ai", headers=token_headers, json=data1)
    print(result.text)
    result = json.loads(result.text)
    if 'code' in result and result['code'] == 0:
        print(result)
        content = result['data']["output"]["choices"][0]["message"]['content']
        return True, content
    else:
       return False, result.get('msg', '未知错误')

if __name__ == '__main__':
    ###########
    username="admin"
    password="123456"
    data={"username":username,"password":password}
    result=requests.post(web_request.web_url+"/login",params=data)
    result=json.loads(result.text)

    if result['code'] == 0:
        web_request.user_token=result['data']['token']
        web_request.user_id=result['data']['userId']
        web_request.username=result['data']['username']

    #print(result)
    ############
    question_list = []
    q1 = "AI的发展?"
    q2 = "该领域最具有影响力的人物"
    q3 = "最新的发展趋势"
    question_list.append(q1)
    question_list.append(q2)
    question_list.append(q3)
    data = {"questionList":question_list}
    result, result_data = req_post_ai(data)
    if result:
        print(result_data)
    else:
        print('请求失败')
