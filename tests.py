import hashlib
import hmac
import sys
import urllib
import simple_khipu

def run_tests():
    user_id = sys.argv[1]
    secret = sys.argv[2]
    data = sys.argv[3]

    
    """
     Run Test methods
    """
    print(simple_khipu.check_payment(user_id,secret,data))
    print(simple_khipu.create_payment(user_id,secret,data))
    print(simple_khipu.get_banks(user_id,secret,data))

if __name__ == '__main__':
    run_tests()
