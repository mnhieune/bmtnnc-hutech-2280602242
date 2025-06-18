from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher
# Giả sử các module Playfair, Railfence, và Vigenere được lưu trong thư mục Test/cipher
# Bạn cần tạo các file này trong Test/cipher hoặc điều chỉnh đường dẫn import
# from Test.cipher.playfair import PlayfairCipher
# from Test.cipher.railfence import RailfenceCipher
# from Test.cipher.vigenere import VigenereCipher

app = Flask(__name__)

# Route for home page
@app.route("/")
def home():
    return render_template('index.html')

# Route for RSA
@app.route("/rsa")
def rsa():
    return render_template('rsa.html')

# Routes for Caesar Cipher
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

# Routes for Playfair Cipher
@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

@app.route("/playfair/encrypt", methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    # Playfair = PlayfairCipher()
    # encrypted_text = Playfair.encrypt_text(text, key)
    # Chỗ này cần triển khai PlayfairCipher
    encrypted_text = "Encrypted text placeholder for Playfair"
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/playfair/decrypt", methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    # Playfair = PlayfairCipher()
    # decrypted_text = Playfair.decrypt_text(text, key)
    # Chỗ này cần triển khai PlayfairCipher
    decrypted_text = "Decrypted text placeholder for Playfair"
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

# Routes for Railfence Cipher
@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/railfence/encrypt", methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    # Railfence = RailfenceCipher()
    # encrypted_text = Railfence.encrypt_text(text, key)
    # Chỗ này cần triển khai RailfenceCipher
    # Ví dụ đơn giản hóa:
    rail = [''] * key
    row, dir_down = 0, False
    for char in text:
        rail[row] += char
        if row == 0:
            dir_down = True
        elif row == key - 1:
            dir_down = False
        row += 1 if dir_down else -1
    encrypted_text = ''.join(rail)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/railfence/decrypt", methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    # Railfence = RailfenceCipher()
    # decrypted_text = Railfence.decrypt_text(text, key)
    # Chỗ này cần triển khai RailfenceCipher
    decrypted_text = "Decrypted text placeholder for Railfence"
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

# Routes for Vigenere Cipher
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    # Vigenere = VigenereCipher()
    # encrypted_text = Vigenere.encrypt_text(text, key)
    # Chỗ này cần triển khai VigenereCipher
    encrypted_text = "Encrypted text placeholder for Vigenere"
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    # Vigenere = VigenereCipher()
    # decrypted_text = Vigenere.decrypt_text(text, key)
    # Chỗ này cần triển khai VigenereCipher
    decrypted_text = "Decrypted text placeholder for Vigenere"
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

# Main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)