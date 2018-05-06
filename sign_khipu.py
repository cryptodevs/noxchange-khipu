import hashlib
import hmac
import sys
import urllib

URL = 'https://khipu.com/api/2.0/'

def run():
    secret = sys.argv[1]
    method = sys.argv[2]
    service = sys.argv[3]
    data = sys.argv[4]

    decoded = "{0}&".format(method)
    decoded = decoded + urllib.quote("{0}{1}".format(URL, service), safe='')
    if data is not "":
        decoded = "{0}&{1}".format(decoded, data)
    print(hmac.new(secret, decoded, hashlib.sha256).hexdigest())

if __name__ == '__main__':
    run()
