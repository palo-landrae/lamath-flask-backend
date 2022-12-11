from flask import Flask
from flask_cors import CORS
from caesar_cipher_api import caesar_cipher_api

app = Flask(__name__)
#app.config['APPLICATION_ROOT'] = '/api'
app.register_blueprint(caesar_cipher_api, url_prefix='/api/caesar_cipher')
CORS(app)

@app.route('/api')
def index():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
