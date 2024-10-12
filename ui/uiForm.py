from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton

from utill.ActionUtlill import ActionMain


class Ui_Form(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('뉴스 크롤링')
        # 화면 표추 x, 화면 표출 y, 가로, 세로
        self.setGeometry(100, 100, 500, 500)

        layout = QVBoxLayout()

        # 카드 입력창
        self.cardLabel = QLabel('카드사 입력:')
        self.cardLineEdit = QLineEdit()
        self.cardLineEdit.setPlaceholderText('수집 하려는 목록 작성')
        # 기본값 설정
        self.cardLineEdit.setText('현대카드, 국민카드, 삼성카드')

        # 이메일 입력 텍스트 상자
        self.emailLabel = QLabel('이메일 입력:')
        self.emailTextEdit = QTextEdit()
        self.emailTextEdit.setPlaceholderText('여러 이메일을 입력하세요... (각 줄마다 한 개씩)')

        # 버튼
        self.submitButton = QPushButton('뉴스 크롤링')
        self.submitButton.clicked.connect(self.onSubmit)

        # 레이아웃에 추가
        layout.addWidget(self.cardLabel)
        layout.addWidget(self.cardLineEdit)
        layout.addWidget(self.emailLabel)
        layout.addWidget(self.emailTextEdit)
        layout.addWidget(self.submitButton)

        self.setLayout(layout)

    def onSubmit(self):
        self.submitButton.setEnabled(False)  # Disable the button
        selected_card = self.cardLineEdit.text()
        emails = self.emailTextEdit.toPlainText().splitlines()

        ActionMain(selected_card, emails)




