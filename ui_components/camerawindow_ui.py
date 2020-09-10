# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'camerawindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CameraWindow(object):
    def setupUi(self, CameraWindow):
        CameraWindow.setObjectName("CameraWindow")
        CameraWindow.resize(1033, 509)
        self.centralwidget = QtWidgets.QWidget(CameraWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.roi_analyzer_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.roi_analyzer_checkBox.setObjectName("roi_analyzer_checkBox")
        self.verticalLayout.addWidget(self.roi_analyzer_checkBox)
        self.gridLayout.addLayout(self.verticalLayout, 3, 0, 1, 3)
        self.view_stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.view_stackedWidget.sizePolicy().hasHeightForWidth())
        self.view_stackedWidget.setSizePolicy(sizePolicy)
        self.view_stackedWidget.setObjectName("view_stackedWidget")
        self.imageview_page = QtWidgets.QWidget()
        self.imageview_page.setObjectName("imageview_page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.imageview_page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.videovieweditor = ImageViewEditor(self.imageview_page)
        self.videovieweditor.setObjectName("videovieweditor")
        self.gridLayout_2.addWidget(self.videovieweditor, 0, 0, 1, 1)
        self.view_stackedWidget.addWidget(self.imageview_page)
        self.absorption_view_page = QtWidgets.QWidget()
        self.absorption_view_page.setObjectName("absorption_view_page")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.absorption_view_page)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.absorption_view_widget = AbsorptionViewWidget(self.absorption_view_page)
        self.absorption_view_widget.setObjectName("absorption_view_widget")
        self.gridLayout_3.addWidget(self.absorption_view_widget, 0, 2, 1, 1)
        self.view_stackedWidget.addWidget(self.absorption_view_page)
        self.gridLayout.addWidget(self.view_stackedWidget, 0, 0, 3, 2)
        self.camera_control_widget = CameraControlWidget(self.centralwidget)
        self.camera_control_widget.setObjectName("camera_control_widget")
        self.gridLayout.addWidget(self.camera_control_widget, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 2, 1, 1)
        CameraWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CameraWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1033, 26))
        self.menubar.setObjectName("menubar")
        CameraWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CameraWindow)
        self.statusbar.setObjectName("statusbar")
        CameraWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CameraWindow)
        self.view_stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(CameraWindow)

    def retranslateUi(self, CameraWindow):
        _translate = QtCore.QCoreApplication.translate
        CameraWindow.setWindowTitle(_translate("CameraWindow", "jkam"))
        self.roi_analyzer_checkBox.setText(_translate("CameraWindow", "ROI Analyzer"))
from absorption_view_widget import AbsorptionViewWidget
from cameracontrolwidget import CameraControlWidget
from imagevieweditor import ImageViewEditor


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CameraWindow = QtWidgets.QMainWindow()
    ui = Ui_CameraWindow()
    ui.setupUi(CameraWindow)
    CameraWindow.show()
    sys.exit(app.exec_())
