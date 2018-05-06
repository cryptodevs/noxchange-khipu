import boto3, json, time
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello world'

@app.route('/testnotify', methods=['POST'])
def testnotify():

    test_dict = request.form.to_dict()
    data = json.dumps(test_dict)
    client = boto3.client('s3')
    key = str(int(time.time()))
    bucket = 'test-nkl-1'
    client.put_object(Body=data, Bucket=bucket, Key='notify/{0}.txt'.format(key))
    return jsonify(test_dict)

@app.route('/testreturn', methods=['POST'])
def testreturn():

    test_dict = request.form.to_dict()
    data = json.dumps(test_dict)
    client = boto3.client('s3')
    key = str(int(time.time()))
    bucket = 'test-nkl-1'
    client.put_object(Body=data, Bucket=bucket, Key='return/{0}.txt'.format(key))
    return jsonify(test_dict)

@app.route('/form', methods=['GET'])
def test_form():
    return render_template('form.html')

if __name__ == '__main__':
    app.run()

