from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def webhook2():
    return 'hello', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
