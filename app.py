from flask import Flask
from flask_cors import CORS
from caesar_cipher_api import caesar_cipher_api
from statistics_api import statistics_api

app = Flask(__name__)
#app.config['APPLICATION_ROOT'] = '/api'
app.register_blueprint(caesar_cipher_api, url_prefix='/api/caesar_cipher')
app.register_blueprint(statistics_api, url_prefix='/api/statistics')
CORS(app)

@app.route('/api')
def index():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
