from flask import Flask, jsonify, request, render_template
from cryptography.fernet import Fernet
import binascii
# import sys

app = Flask(__name__)
cipher_suite = Fernet(Fernet.generate_key())


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def post():
    if('action1' in request.form):
        text = request.form['text1']
        # print (request.form, file=sys.stderr)
        return render_template('index.html', value2=encryption(text))
    if('action2' in request.form):
        text = request.form['text2']
        # print (request.form, file=sys.stderr)
        return render_template('index.html', value1=decryption(text))


def encryption(message):
    stringToBytes = message.encode('utf-8')
    cipher = cipher_suite.encrypt(stringToBytes)
    bytesToHex = binascii.hexlify(cipher)
    return str(bytesToHex, 'ascii')


def decryption(message):
    stringToBytes = message.encode('utf-8')
    cipher = binascii.unhexlify(stringToBytes)
    plainText = cipher_suite.decrypt(cipher)
    return str(plainText, 'ascii')


if __name__ == '__main__':
    app.run()
