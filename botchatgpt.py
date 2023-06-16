from flask import Flask, request
import requests
from listen import API
import openai
import json


def gpt(data):
    message = data["message"]
    openai.api_key= ""
    if message[0:4]==".gpt":
        if data["message"][4]=="3":
            
            #print("进来了3")
            gpt_message = data["message"][5:]
            response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                    #{"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": gpt_message},
                    # {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
                    # {"role": "user", "content": "Where was it played?"}
                ]
            )
            API.send(response['choices'][0]['message']['content'])
        if data["message"][4]=="4":
            gpt_message = data["message"][5:]
            API.send("你向gpt4发送的是"+gpt_message)
    else:

        print("猫")
        gpt_message = data["message"]
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0.1,
        max_tokens=2048,
        top_p = 0.2,
        messages=[
                # {"role": "system", "content": "你是个猫娘,很爱帮助别人解决问题,名字叫猫猫。性格是外向可爱乖巧活泼俏皮，有少女朝气。平时你很乐观开朗,但偶尔也比较敏感。当你伤心,你会用语言回击。"},
                {"role": "user", "content": gpt_message},
                # {"role": "assistant", "content": "我是个猫娘,很爱帮助别人解决问题,名字叫猫猫。性格是外向可爱乖巧活泼俏皮，有少女朝气。平时我很乐观开朗,但偶尔也比较敏感。当你伤心,我会用语言回击。"},
                # # {"role": "user", "content": "Where was it played?"}
                # {"role": "user", "content": gpt_message}
            ]
        )
        API.send(response['choices'][0]['message']['content'],data)
        print(response['usage'])
    return 0



    



