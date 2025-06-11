import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.vigenere import Ui_Dialog
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/vigenere/encrypt"
        payload = {
            "plain_text": self.ui.txt_plain_text.toPlainText(),
            "key": self.ui.txt_key.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                if "encrypted_text" in data:
                    self.ui.txt_cipher_text.setText(data["encrypted_text"])
                else:
                    self.ui.txt_cipher_text.setText("Không có kết quả mã hóa từ API.")
            else:
                print("Lỗi khi gọi API (encrypt):", response.status_code)
        except requests.exceptions.RequestException as e:
            print("Lỗi mạng:", str(e))

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/vigenere/decrypt"
        payload = {
            "cipher_text": self.ui.txt_cipher_text.toPlainText(),
            "key": self.ui.txt_key.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                if "decrypted_text" in data:
                    self.ui.txt_plain_text.setText(data["decrypted_text"])
                else:
                    self.ui.txt_plain_text.setText("Không có kết quả giải mã từ API.")
            else:
                print("Lỗi khi gọi API (decrypt):", response.status_code)
        except requests.exceptions.RequestException as e:
            print("Lỗi mạng:", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())