import json

def lambda_handler(event, context):
    print(f"This is my event: {event}" )
    if event["name"] == "marco":
        return "polo"
    return "no"
    
