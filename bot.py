# -*- coding: utf-8 -*-

############################################################
###1               Information and Import                ###

###Import
import requests

### Baidu info
APP_ID = '19642375'
API_KEY = 'XBWYcWlMvE11TVb3dbaGvtD9'
SECRET_KEY = 'aje8SyhLkd6elXrpUtTkSzsVzl7x8udH'
### RuYi info
APP_KEY = 'bfdeb392-0e9e-452f-8eec-09a1de2e58d0'

############################################################
###2              Main Functions and Methods             ###

def privatePost(question, user):
    # post info
    info = {
                "q": question,
                "app_key": APP_KEY,
                "user_id": user
            }
    result = requests.get('http://api.ruyi.ai/v1/message', info).json()  # using get method
    answer = result['result']['intents'][0]['outputs'][0]['property']['text']
    return answer

def publicPost(question):
    # # post info
    # info = {
    #             "q": question,
    #             "app_key": APP_KEY,
    #             "user_id": 'Public'
    #         }
    # result = requests.get('http://api.ruyi.ai/v1/message', info).json()  # using get method
    # print(result)
    # skill = result['result']['intents'][0].get('skill_id')
    # if skill:
    #     answer = '对不起，该功能暂不对未登录用户开放，请登录后再试'
    # else:
    #     answer = result['result']['intents'][0]['outputs'][0]['property']['text']
    answer = '对不起，该功能暂不对未登录用户开放，请登录后再试'
    return answer

def post(question, user):
    if user:
        return privatePost(question, user)
    else:
        return publicPost(question)
