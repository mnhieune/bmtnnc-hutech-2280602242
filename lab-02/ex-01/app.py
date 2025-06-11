from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher
from cipher.playfair import PlayFairCipher

app = Flask(__name__)

# ràng buoc
def process_cipher(cipher_type, text, key, action):
    try:
        if cipher_type == "caesar":
            key = int(key)
            if key < 0:
                return f"Lỗi: Key phải là số không âm"
            cipher = CaesarCipher()
            method = cipher.encrypt_text if action == "encrypt" else cipher.decrypt_text
            result = method(text, key)
        elif cipher_type == "playfair":
            if not key.isalpha():
                return f"Lỗi: Key chỉ được chứa chữ cái"
            cipher = PlayFairCipher()
            matrix = cipher.create_playfair_matrix(key)
            method = cipher.playfair_encrypt if action == "encrypt" else cipher.playfair_decrypt
            result = method(text, matrix)
        elif cipher_type == "railfence":
            key = int(key)
            if key < 2:
                return f"Lỗi: Key phải lớn hơn hoặc bằng 2"
            cipher = RailFenceCipher(key)
            method = cipher.encrypt if action == "encrypt" else cipher.decrypt
            result = method(text)
        elif cipher_type == "vigenere":
            if not key.isalpha():
                return f"Lỗi: Key chỉ được chứa chữ cái"
            cipher = VigenereCipher(key)
            method = cipher.encrypt if action == "encrypt" else cipher.decrypt
            result = method(text)
        else:
            return f"Lỗi: Cipher không hợp lệ"
        return f"text: {text}<br/>key: {key}<br/>{action}ed text: {result}"
    except ValueError:
        return f"Lỗi: Key phải là một số nguyên" if cipher_type in ["caesar", "railfence"] else f"Lỗi: Dữ liệu đầu vào không hợp lệ"

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')


@app.route("/<cipher_type>/encrypt", methods=['POST'])
def encrypt(cipher_type):
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    return process_cipher(cipher_type, text, key, "encrypt")

@app.route("/<cipher_type>/decrypt", methods=['POST'])
def decrypt(cipher_type):
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    return process_cipher(cipher_type, text, key, "decrypt")

# railf fence
class RailFenceCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, plain_text):
        rails = [[] for _ in range(self.key)]
        rail_index = 0
        direction = 1
        for char in plain_text:
            rails[rail_index].append(char)
            if rail_index == 0:
                direction = 1
            elif rail_index == self.key - 1:
                direction = -1
            rail_index += direction
        return ''.join(''.join(rail) for rail in rails)
    
    def decrypt(self, cipher_text):
        rail_lengths = [0] * self.key
        rail_index = 0
        direction = 1
        for _ in range(len(cipher_text)):
            rail_lengths[rail_index] += 1
            if rail_index == 0:
                direction = 1
            elif rail_index == self.key - 1:
                direction = -1
            rail_index += direction
        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(cipher_text[start:start + length])
            start += length
        plain_text = ""
        rail_index = 0
        direction = 1
        for _ in range(len(cipher_text)):
            plain_text += rails[rail_index][0]
            rails[rail_index] = rails[rail_index][1:]
            if rail_index == 0:
                direction = 1
            elif rail_index == self.key - 1:
                direction = -1
            rail_index += direction
        return plain_text

# Vigenere Cipher class
class VigenereCipher:
    def __init__(self, key):
        self.key = key.upper()

    def encrypt(self, plain_text):
        key = self._extend_key(plain_text)
        cipher_text = ""
        for p, k in zip(plain_text.upper(), key):
            if p.isalpha():
                shift = ord(k) - ord('A')
                encrypted_char = chr((ord(p) - ord('A') + shift) % 26 + ord('A'))
                cipher_text += encrypted_char
            else:
                cipher_text += p
        return cipher_text

    def decrypt(self, cipher_text):
        key = self._extend_key(cipher_text)
        plain_text = ""
        for c, k in zip(cipher_text.upper(), key):
            if c.isalpha():
                shift = ord(k) - ord('A')
                decrypted_char = chr((ord(c) - ord('A') - shift) % 26 + ord('A'))
                plain_text += decrypted_char
            else:
                plain_text += c
        return plain_text

    def _extend_key(self, text):
        return (self.key * (len(text) // len(self.key) + 1))[:len(text)]

# Main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)