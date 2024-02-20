from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel,QVBoxLayout,QSpacerItem,QSizePolicy,QFrame
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QResizeEvent

class StatusBarInfo(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("border:none;")
        # Create a QHBoxLayout for the QLabel widgets
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)     

        # Add QLabel widgets to the horizontal layout
        self.ql_cordinate = QLabel()
        self.ql_cordinate.setStyleSheet(
            "QLabel { border: none; border-left: 1px solid rgb(210, 210, 210); }"
        )
        self.ql_cordinate.setFixedSize(140, 15)
        self.horizontalLayout.addWidget(self.ql_cordinate)

        self.ql_zoom_level = QLabel()
        self.ql_zoom_level.setStyleSheet(
            "QLabel { border: none; border-left: 1px solid rgb(210, 210, 210); }"
        )
        self.ql_zoom_level.setFixedSize(50, 15)
        self.horizontalLayout.addWidget(self.ql_zoom_level)

        self.ql_windows = QLabel()
        self.ql_windows.setStyleSheet(
            "QLabel { border: none; border-left: 1px solid rgb(210, 210, 210); }"
        )
        self.ql_windows.setFixedSize(121, 15)
        self.horizontalLayout.addWidget(self.ql_windows)

        self.ql_text_encoding = QLabel()
        self.ql_text_encoding.setStyleSheet(
            "QLabel { border: none; border-left: 1px solid rgb(210, 210, 210); }"
        )
        self.ql_text_encoding.setFixedSize(100, 15)
        self.horizontalLayout.addWidget(self.ql_text_encoding)

        self.retranslateUi()


    def retranslateUi(self):
        # Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.ql_cordinate.setText(QCoreApplication.translate("Form", u"Ln 1, Col 1", None))
        self.ql_zoom_level.setText(QCoreApplication.translate("Form", u"100%", None))
        self.ql_windows.setText(QCoreApplication.translate("Form", u"Windows(CRLF)", None))
        self.ql_text_encoding.setText(QCoreApplication.translate("Form", u"UTF-8", None))