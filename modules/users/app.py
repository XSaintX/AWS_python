import json
import os
from db.database import DataBase

def lambda_handler(event, context):
    print("Received event: ", event)
    print("Context: ", context)
    body_response_2 = {}
    keys = ["id", "nombre", "apellido", "ciudad"]
    if event.get("path") == "/users" and event.get("httpMethod") == "GET":
        db = DataBase()
        users = db.get_users()
        body_response_2 = {
            "usuarios": [
                dict(zip(keys, user))
                for user in users
            ]
        }
    elif event.get("path") == "/users" and event.get("httpMethod") == "POST":
        body_response_2 = {"message": "CREATE U"}
    # List_users = []
    # for i in users:
    #     List_users.append(
    #         {
    #             "id": i[0],
    #             "nombre": i[1],
    #             "apellido": i[2],
    #             "ciudad": i[3]
    #         }
    #     )



    # body_response_1 = {
    #     "usuarios": List_users
    # }
    # print("Predata --> ", users)
    
    # body_response_2 = {
    #     "usuarios": [
    #         dict(zip(keys, user))
    #         for user in users
    #     ]
    # }
    # body_response_2 = {
    #     "usuarios": [dict(user) for user in users]
    # }
    # print("Users --> ", body_response_2)
    return {
        "headers": {
            "Access-Control-Allow-Origin": "*",
        },
        "statusCode": 200,
        "body": json.dumps(body_response_2)
    }