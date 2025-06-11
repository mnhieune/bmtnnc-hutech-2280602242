import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.playfair import Ui_Dialog
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

      
        self.ui.txt_key.textChanged.connect(self.call_api_matrix)

    def call_api_matrix(self):
        url = "http://127.0.0.1:5000/api/playfair/creatematrix"
        payload = {
            "key": self.ui.txt_key.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                matrix = data.get("playfair_matrix", [])
                formatted_matrix = "\n".join([" ".join(row) for row in matrix])
                self.ui.txt_matrix.setPlainText(formatted_matrix)
            else:
                self.ui.txt_matrix.setPlainText("Lỗi khi gọi API tạo matrix.")
        except requests.exceptions.RequestException as e:
            self.ui.txt_matrix.setPlainText(f"Lỗi: {e}")

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/playfair/encrypt"
        payload = {
            "plain_text": self.ui.txt_plain_text.toPlainText(),
            "key": self.ui.txt_key.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher_text.setPlainText(data.get("encrypted_text", ""))
            else:
                self.ui.txt_cipher_text.setPlainText("Lỗi khi gọi API mã hóa.")
        except requests.exceptions.RequestException as e:
            self.ui.txt_cipher_text.setPlainText(f"Lỗi: {e}")

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/playfair/decrypt"
        payload = {
            "cipher_text": self.ui.txt_cipher_text.toPlainText(),
            "key": self.ui.txt_key.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plain_text.setPlainText(data.get("decrypted_text", ""))
            else:
                self.ui.txt_plain_text.setPlainText("Lỗi khi gọi API giải mã.")
        except requests.exceptions.RequestException as e:
            self.ui.txt_plain_text.setPlainText(f"Lỗi: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
