import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton

from utill.ActionUtlill import ActionMain  # Ensure ActionMain is defined in this module


class Ui_Form(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('카드 및 이메일 입력')
        self.setGeometry(100, 100, 600, 400)  # Increased size for the log area

        layout = QVBoxLayout()

        # 카드 입력창
        self.cardLabel = QLabel('카드사 입력:')
        self.cardLineEdit = QLineEdit()
        self.cardLineEdit.setPlaceholderText('수집 하려는 목록 작성')
        self.cardLineEdit.setText('현대카드, 국민카드, 삼성카드')  # 기본값 설정

        # 이메일 입력 텍스트 상자
        self.emailLabel = QLabel('이메일 입력:')
        self.emailTextEdit = QTextEdit()
        self.emailTextEdit.setPlaceholderText('여러 이메일을 입력하세요... (각 줄마다 한 개씩)')

        # 로그 출력창
        self.logLabel = QLabel('로그:')
        self.logTextEdit = QTextEdit()
        self.logTextEdit.setReadOnly(True)
        self.logTextEdit.setPlaceholderText('작업 진행 중 로그가 여기에 표시됩니다.')

        # 버튼
        self.submitButton = QPushButton('뉴스 크롤링')
        self.submitButton.clicked.connect(self.onSubmit)

        # 레이아웃에 추가
        layout.addWidget(self.cardLabel)
        layout.addWidget(self.cardLineEdit)
        layout.addWidget(self.emailLabel)
        layout.addWidget(self.emailTextEdit)
        layout.addWidget(self.submitButton)
        layout.addWidget(self.logLabel)
        layout.addWidget(self.logTextEdit)

        self.setLayout(layout)

    def uiLog(self, message):
        self.logTextEdit.append(message)

    def onSubmit(self):
        self.submitButton.setEnabled(False)  # Disable the button
        selected_card = self.cardLineEdit.text()
        emails = self.emailTextEdit.toPlainText().splitlines()
        self.log(f"선택한 카드: {selected_card}")
        self.log(f"입력된 이메일: {emails}")

        ActionMain(selected_card, emails)

def display():
    app = QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    sys.exit(app.exec_())


