from flask import Blueprint, request, json

alphabet_upper = ''.join([chr(ascii) for ascii in range(65, 91)])

caesar_cipher_api = Blueprint('caesar_cipher_api', __name__)


@caesar_cipher_api.route('/encrypt', methods=['POST'])
def encrypt():
    if request.method == 'POST':
        data = json.loads(request.data)
        plaintext = data['plaintext'].upper()
        n_shift = int(data['shift'])
        n_step = int(data['step'])
        if data['isProgressive']:
            result = []
            for i in range(len(plaintext)):
                shifted_alphabet = alphabet_upper[n_shift +
                                                  i+(n_step-1):] + alphabet_upper[:n_shift+i+(n_step-1)]
                table = str.maketrans(alphabet_upper, shifted_alphabet)
                result.append(plaintext[i].translate(table))
            return ''.join(result)
        else:
            shifted_alphabet = alphabet_upper[n_shift:] + alphabet_upper[:n_shift]
            table = str.maketrans(alphabet_upper, shifted_alphabet)
            return plaintext.translate(table)
    else:
        return 'Bad Request!'

@caesar_cipher_api.route('/decrypt', methods=['POST'])
def decrypt():
    if request.method == 'POST':
        data = json.loads(request.data)
        plaintext = data['cipher'].upper()
        n_shift = int(data['shift'])
        n_step = int(data['step'])
        if data['isProgressive']:
            result = []
            for i in range(len(plaintext)):
                shifted_alphabet = alphabet_upper[n_shift +
                                                  i+(n_step-1):] + alphabet_upper[:n_shift+i+(n_step-1)]
                table = str.maketrans(shifted_alphabet, alphabet_upper)
                result.append(plaintext[i].translate(table))
            return ''.join(result)
        else:
            shifted_alphabet = alphabet_upper[n_shift:] + alphabet_upper[:n_shift]
            table = str.maketrans(shifted_alphabet, alphabet_upper)
        return plaintext.translate(table)
    else:
        return 'Bad Request!'
