import random
import string
from PyQt5 import QtWidgets, QtGui, QtCore

class GeradorSenhas(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gerador de Senhas")
        self.setup_ui()

    def setup_ui(self):
        self.comprimento_label = QtWidgets.QLabel("Comprimento da senha:")
        self.comprimento_input = QtWidgets.QSpinBox()
        self.comprimento_input.setMinimum(1)
        self.comprimento_input.setMaximum(100)
        self.letras_maiusculas_checkbox = QtWidgets.QCheckBox("Letras maiúsculas")
        self.letras_minusculas_checkbox = QtWidgets.QCheckBox("Letras minúsculas")
        self.numeros_checkbox = QtWidgets.QCheckBox("Números")
        self.simbolos_checkbox = QtWidgets.QCheckBox("Símbolos")
        self.gerar_senha_button = QtWidgets.QPushButton("Gerar Senha")
        self.senha_gerada_label = QtWidgets.QLabel()
        self.copiar_button = QtWidgets.QPushButton("Copie")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.comprimento_label)
        layout.addWidget(self.comprimento_input)
        layout.addWidget(self.letras_maiusculas_checkbox)
        layout.addWidget(self.letras_minusculas_checkbox)
        layout.addWidget(self.numeros_checkbox)
        layout.addWidget(self.simbolos_checkbox)
        layout.addWidget(self.gerar_senha_button)
        layout.addWidget(self.senha_gerada_label)
        layout.addWidget(self.copiar_button)

        self.setLayout(layout)

        self.gerar_senha_button.clicked.connect(self.gerar_senha)
        self.copiar_button.clicked.connect(self.copiar_senha)

    def gerar_senha(self):
        comprimento = self.comprimento_input.value()

        tipos_caracteres = []
        if self.letras_maiusculas_checkbox.isChecked():
            tipos_caracteres.append('letras_maiusculas')
        if self.letras_minusculas_checkbox.isChecked():
            tipos_caracteres.append('letras_minusculas')
        if self.numeros_checkbox.isChecked():
            tipos_caracteres.append('numeros')
        if self.simbolos_checkbox.isChecked():
            tipos_caracteres.append('simbolos')

        if not tipos_caracteres:
            self.senha_gerada_label.setText("Selecione pelo menos um tipo de caractere.")
            self.copiar_button.setEnabled(False)
        else:
            senha_gerada = self.gerar_senha_aleatoria(comprimento, tipos_caracteres)
            self.senha_gerada_label.setText("Senha gerada: " + senha_gerada)
            self.copiar_button.setEnabled(True)
            self.copiar_button.setText("Copie")

    def gerar_senha_aleatoria(self, comprimento, tipos_caracteres):
        caracteres = ''
        if 'letras_maiusculas' in tipos_caracteres:
            caracteres += string.ascii_uppercase
        if 'letras_minusculas' in tipos_caracteres:
            caracteres += string.ascii_lowercase
        if 'numeros' in tipos_caracteres:
            caracteres += string.digits
        if 'simbolos' in tipos_caracteres:
            caracteres += string.punctuation

        senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
        return senha

    def copiar_senha(self):
        senha = self.senha_gerada_label.text().replace("Senha gerada: ", "")
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(senha)

        self.copiar_button.setText("Copiado")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    gerador_senhas = GeradorSenhas()
    gerador_senhas.show()
    app.exec_()
