import hashlib
import hmac
import sys
import urllib
import simple_khipu

URL = 'https://khipu.com/api/2.0/'

def run():
    user_id = sys.argv[1]
    secret = sys.argv[2]
    method = sys.argv[3]
    service = sys.argv[4]
    data = sys.argv[5]

    print(simple_khipu.sign_message(secret,method,service,data))
    
    """
     Test methods
    """
    #print(simple_khipu.check_payment(user_id,secret,data))
    print(simple_khipu.create_payment(user_id,secret,data))
    #print(simple_khipu.get_banks(user_id,secret,data))

if __name__ == '__main__':
    run()
