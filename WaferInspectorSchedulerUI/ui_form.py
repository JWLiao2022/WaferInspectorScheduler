# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(178, 360)
        self.layoutWidget = QWidget(Widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 10, 171, 331))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.layoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.layoutWidget1 = QWidget(self.groupBox)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 30, 144, 61))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_MW3PortNumber = QLineEdit(self.layoutWidget1)
        self.lineEdit_MW3PortNumber.setObjectName(u"lineEdit_MW3PortNumber")

        self.horizontalLayout.addWidget(self.lineEdit_MW3PortNumber)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.pushButton_MW3Connect = QPushButton(self.layoutWidget1)
        self.pushButton_MW3Connect.setObjectName(u"pushButton_MW3Connect")

        self.verticalLayout.addWidget(self.pushButton_MW3Connect)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.layoutWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.layoutWidget2 = QWidget(self.groupBox_2)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(0, 20, 151, 83))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.dateTimeEdit = QDateTimeEdit(self.layoutWidget2)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")

        self.verticalLayout_2.addWidget(self.dateTimeEdit)

        self.pushButton_StartScheduling = QPushButton(self.layoutWidget2)
        self.pushButton_StartScheduling.setObjectName(u"pushButton_StartScheduling")

        self.verticalLayout_2.addWidget(self.pushButton_StartScheduling)

        self.pushButton_StopScheduling = QPushButton(self.layoutWidget2)
        self.pushButton_StopScheduling.setObjectName(u"pushButton_StopScheduling")

        self.verticalLayout_2.addWidget(self.pushButton_StopScheduling)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.layoutWidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.label_CurrentStatus = QLabel(self.groupBox_3)
        self.label_CurrentStatus.setObjectName(u"label_CurrentStatus")
        self.label_CurrentStatus.setGeometry(QRect(10, 30, 151, 31))
        self.label_CurrentStatus_2 = QLabel(self.groupBox_3)
        self.label_CurrentStatus_2.setObjectName(u"label_CurrentStatus_2")
        self.label_CurrentStatus_2.setGeometry(QRect(10, 60, 151, 31))

        self.verticalLayout_3.addWidget(self.groupBox_3)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Wafer Spection Timer", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"MW3 connection", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Port", None))
        self.lineEdit_MW3PortNumber.setText(QCoreApplication.translate("Widget", u"8888", None))
        self.pushButton_MW3Connect.setText(QCoreApplication.translate("Widget", u"Connect!", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Widget", u"Scheduler", None))
        self.pushButton_StartScheduling.setText(QCoreApplication.translate("Widget", u"Start!", None))
        self.pushButton_StopScheduling.setText(QCoreApplication.translate("Widget", u"Stop!", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Widget", u"Current status", None))
        self.label_CurrentStatus.setText(QCoreApplication.translate("Widget", u"Waiting for scheduling...", None))
        self.label_CurrentStatus_2.setText(QCoreApplication.translate("Widget", u"Standing by...", None))
    # retranslateUi

