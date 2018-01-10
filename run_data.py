import sys, json

def print_message(msg):
    return {"inbound_message": msg}

if __name__ == '__main__':
    request = json.load( sys.stdin )
    print(request)