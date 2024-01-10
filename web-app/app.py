from os import environ
from time import sleep
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from transpiler import Transpiler

app = Flask(__name__)
CORS(app)

@app.route('/output', methods=['GET'])
@cross_origin()
def output():
    sleep(0.5)
    with open('output/output.txt', 'r') as f:
        code = f.read()
        print(code)
    return jsonify({"target_code": f"{code}"})

@app.route('/input_source', methods = ['POST'])
@cross_origin()
def source_code():
    content = request.get_json()
    print(f"Recieved Data: \n{content}")
    code = content['source_code']
    # with open('output.txt', 'w') as f:
    #     f.write(code)
    print(code)
    Transpiler(source_code=code).transpile()
    response = {'message': 'Data received successfully'}
    return jsonify(response)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    port = int(environ.get("PORT", 5000))
    app.run(host='127.0.0.1', port=port, debug=True)
