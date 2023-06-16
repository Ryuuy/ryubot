from flask import Flask, request
import requests
import botchatgpt
server = Flask(__name__)
class API:

    @staticmethod
    def send(message,data):#进来的时候必须是messga
        #print("在send调用了")
        if data["post_type"]=="message":
            uid = data['user_id']
            message_time = data['time']
            message_type = data['message_type']
            if message_type == "group":
                group_id = data["group_id"]
                params = {
                    "message_type":message_type,
                    "user_id":str(uid),
                    "group_id" : str(group_id),
                    "message":message
                }

            elif(message_type == "private"):
                params = {
                    "message_type":message_type,
                    "user_id":str(uid),
                    "message":message
                }


        url = "http://127.0.0.1:5700/send_msg"

        requests.get(url,params=params)



@server.route('/', methods=['post'])
def post_data():
    data = request.get_json()
    print(data)
    if data["post_type"]=="message":
        botchatgpt.gpt(data)
        message=data.get("message")
        print(message)
    return "OK"


if __name__ == '__main__':
    server.run(port=5701, host='0.0.0.0')
    #, use_reloader=False