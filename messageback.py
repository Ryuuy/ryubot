from listen import API

def send_message(data):
    if data["post_type"]=="message":
        uid = data['user_id']
        message_time = data['time']
        message_type = data['message_type']
        if message_type == "group":
            group_id = data["group_id"]
        elif(message_type == "private"):
            group_id == None

