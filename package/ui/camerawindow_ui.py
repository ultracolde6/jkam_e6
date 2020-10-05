# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_resources\camerawindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CameraWindow(object):
    def setupUi(self, CameraWindow):
        CameraWindow.setObjectName("CameraWindow")
        CameraWindow.resize(505, 778)
        self.centralwidget = QtWidgets.QWidget(CameraWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.view_stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
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
        self.fluorescence_view_page = QtWidgets.QWidget()
        self.fluorescence_view_page.setObjectName("fluorescence_view_page")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.fluorescence_view_page)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.fluorescence_view_widget = FluorescenceViewWidget(self.fluorescence_view_page)
        self.fluorescence_view_widget.setObjectName("fluorescence_view_widget")
        self.gridLayout_6.addWidget(self.fluorescence_view_widget, 0, 0, 1, 1)
        self.view_stackedWidget.addWidget(self.fluorescence_view_page)
        self.gridLayout.addWidget(self.view_stackedWidget, 0, 0, 1, 3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.camera_control_widget = CameraControlWidget(self.centralwidget)
        self.camera_control_widget.setObjectName("camera_control_widget")
        self.verticalLayout.addWidget(self.camera_control_widget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.imagecapturemodewidget = ImageCaptureModeWidget(self.centralwidget)
        self.imagecapturemodewidget.setObjectName("imagecapturemodewidget")
        self.horizontalLayout_2.addWidget(self.imagecapturemodewidget)
        self.roi_analyzer_widget = RoiIntegrationAnalyzer(self.centralwidget)
        self.roi_analyzer_widget.setObjectName("roi_analyzer_widget")
        self.horizontalLayout_2.addWidget(self.roi_analyzer_widget)
        self.gaussian2d_analyzer_widget = GaussianFitAnalyzer(self.centralwidget)
        self.gaussian2d_analyzer_widget.setObjectName("gaussian2d_analyzer_widget")
        self.horizontalLayout_2.addWidget(self.gaussian2d_analyzer_widget)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.savebox_verticalLayout = QtWidgets.QVBoxLayout()
        self.savebox_verticalLayout.setObjectName("savebox_verticalLayout")
        self.savebox_widget = SaveBoxWidget(self.centralwidget)
        self.savebox_widget.setObjectName("savebox_widget")
        self.savebox_verticalLayout.addWidget(self.savebox_widget)
        self.horizontalLayout.addLayout(self.savebox_verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 3)
        CameraWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CameraWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 505, 26))
        self.menubar.setObjectName("menubar")
        CameraWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CameraWindow)
        self.statusbar.setObjectName("statusbar")
        CameraWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CameraWindow)
        QtCore.QMetaObject.connectSlotsByName(CameraWindow)

    def retranslateUi(self, CameraWindow):
        _translate = QtCore.QCoreApplication.translate
        CameraWindow.setWindowTitle(_translate("CameraWindow", "jkam"))
from package.analyzers.gaussianfitanalyzer import GaussianFitAnalyzer
from package.analyzers.roiintegrationanalyzer import RoiIntegrationAnalyzer
from package.widgets.absorption_view_widget import AbsorptionViewWidget
from package.widgets.cameracontrolwidget import CameraControlWidget
from package.widgets.fluorescence_view_widget import FluorescenceViewWidget
from package.widgets.imagecapturemodewidget import ImageCaptureModeWidget
from package.widgets.imagevieweditor import ImageViewEditor
from package.widgets.saveboxwidget import SaveBoxWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CameraWindow = QtWidgets.QMainWindow()
    ui = Ui_CameraWindow()
    ui.setupUi(CameraWindow)
    CameraWindow.show()
    sys.exit(app.exec_())
