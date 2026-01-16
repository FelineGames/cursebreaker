from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QFileDialog
)


class AddGameDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Add Game")
        self.setFixedSize(420, 280)
        self.setStyleSheet("""
            QDialog {
                background:#171D25;
                color:white;
            }
            QLabel {
                color:white;
            }
            QLineEdit {
                background:#1F2F50;
                color:white;
                padding:5px;
                border-radius:3px;
            }
        """)

        self.game_data = {}

        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(10)

        layout.addWidget(QLabel("Executable"))
        self.exe_input = QLineEdit()
        layout.addLayout(self._browse_row(self.exe_input, self.browse_exe))

        layout.addWidget(QLabel("Icon (optional)"))
        self.icon_input = QLineEdit()
        layout.addLayout(self._browse_row(self.icon_input, self.browse_icon))

        layout.addWidget(QLabel("Game Title"))
        self.title_input = QLineEdit()
        layout.addWidget(self.title_input)

        layout.addWidget(QLabel("Developer"))
        self.author_input = QLineEdit()
        layout.addWidget(self.author_input)

        layout.addStretch()

        btn_row = QHBoxLayout()
        btn_row.addStretch()

        confirm_btn = QPushButton("Add Game")
        confirm_btn.setFixedHeight(34)
        confirm_btn.setStyleSheet("""
            QPushButton {
                background:#1F2F50;
                color:white;
                padding:6px 20px;
                border-radius:4px;
            }
            QPushButton:hover {
                background:#2b406a;
            }
        """)
        confirm_btn.clicked.connect(self.confirm)

        btn_row.addWidget(confirm_btn)
        layout.addLayout(btn_row)

    def _browse_row(self, field, callback):
        row = QHBoxLayout()

        browse_btn = QPushButton("Browse")
        browse_btn.setStyleSheet("""
            QPushButton {
                background:#1F2F50;
                color:white;
                padding:4px 10px;
                border-radius:3px;
            }
            QPushButton:hover {
                background:#2b406a;
            }
        """)
        browse_btn.clicked.connect(callback)

        row.addWidget(field)
        row.addWidget(browse_btn)
        return row

    def browse_exe(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Select Executable", "", "Executable (*.exe)"
        )
        if path:
            self.exe_input.setText(path)

    def browse_icon(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Select Icon", "", "Images (*.png *.ico)"
        )
        if path:
            self.icon_input.setText(path)

    def confirm(self):
        self.game_data = {
            "title": self.title_input.text(),
            "author": self.author_input.text(),
            "exe": self.exe_input.text(),
            "icon": self.icon_input.text()
        }
        self.accept()
