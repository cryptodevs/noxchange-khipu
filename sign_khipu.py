import hashlib
import hmac
import sys
import urllib
import simple_khipu

def run():
    """
    Generate token.
    """    
    secret = sys.argv[1]
    method = sys.argv[2]
    service = sys.argv[3]
    data = sys.argv[4]

    print(simple_khipu.sign_message(secret,method,service,data))
    

if __name__ == '__main__':
    run()
