# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cameracontrolwidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CameraControlWidget(object):
    def setupUi(self, CameraControlWidget):
        CameraControlWidget.setObjectName("CameraControlWidget")
        CameraControlWidget.resize(507, 240)
        self.gridLayout = QtWidgets.QGridLayout(CameraControlWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(CameraControlWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.camera_comboBox = QtWidgets.QComboBox(self.frame)
        self.camera_comboBox.setObjectName("camera_comboBox")
        self.camera_comboBox.addItem("")
        self.verticalLayout.addWidget(self.camera_comboBox)
        self.serial_label = QtWidgets.QLabel(self.frame)
        self.serial_label.setObjectName("serial_label")
        self.verticalLayout.addWidget(self.serial_label)
        self.arm_pushButton = QtWidgets.QPushButton(self.frame)
        self.arm_pushButton.setObjectName("arm_pushButton")
        self.verticalLayout.addWidget(self.arm_pushButton)
        self.start_pushButton = QtWidgets.QPushButton(self.frame)
        self.start_pushButton.setEnabled(False)
        self.start_pushButton.setObjectName("start_pushButton")
        self.verticalLayout.addWidget(self.start_pushButton)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.exposure_label = QtWidgets.QLabel(self.frame)
        self.exposure_label.setObjectName("exposure_label")
        self.horizontalLayout.addWidget(self.exposure_label)
        self.exposure_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.exposure_lineEdit.setObjectName("exposure_lineEdit")
        self.horizontalLayout.addWidget(self.exposure_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.exposure_pushButton = QtWidgets.QPushButton(self.frame)
        self.exposure_pushButton.setEnabled(False)
        self.exposure_pushButton.setObjectName("exposure_pushButton")
        self.verticalLayout.addWidget(self.exposure_pushButton)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 2, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.continuous_radioButton = QtWidgets.QRadioButton(self.frame)
        self.continuous_radioButton.setEnabled(False)
        self.continuous_radioButton.setChecked(True)
        self.continuous_radioButton.setObjectName("continuous_radioButton")
        self.mode_buttonGroup = QtWidgets.QButtonGroup(CameraControlWidget)
        self.mode_buttonGroup.setObjectName("mode_buttonGroup")
        self.mode_buttonGroup.addButton(self.continuous_radioButton)
        self.gridLayout_3.addWidget(self.continuous_radioButton, 1, 1, 1, 1)
        self.software_trigger_radioButton = QtWidgets.QRadioButton(self.frame)
        self.software_trigger_radioButton.setEnabled(False)
        self.software_trigger_radioButton.setObjectName("software_trigger_radioButton")
        self.trigger_buttonGroup = QtWidgets.QButtonGroup(CameraControlWidget)
        self.trigger_buttonGroup.setObjectName("trigger_buttonGroup")
        self.trigger_buttonGroup.addButton(self.software_trigger_radioButton)
        self.gridLayout_3.addWidget(self.software_trigger_radioButton, 3, 1, 1, 1)
        self.hardware_trigger_radioButton = QtWidgets.QRadioButton(self.frame)
        self.hardware_trigger_radioButton.setEnabled(False)
        self.hardware_trigger_radioButton.setChecked(True)
        self.hardware_trigger_radioButton.setObjectName("hardware_trigger_radioButton")
        self.trigger_buttonGroup.addButton(self.hardware_trigger_radioButton)
        self.gridLayout_3.addWidget(self.hardware_trigger_radioButton, 3, 0, 1, 1)
        self.triggered_radioButton = QtWidgets.QRadioButton(self.frame)
        self.triggered_radioButton.setEnabled(False)
        self.triggered_radioButton.setObjectName("triggered_radioButton")
        self.mode_buttonGroup.addButton(self.triggered_radioButton)
        self.gridLayout_3.addWidget(self.triggered_radioButton, 1, 0, 1, 1)
        self.software_trigger_pushButton = QtWidgets.QPushButton(self.frame)
        self.software_trigger_pushButton.setEnabled(False)
        self.software_trigger_pushButton.setObjectName("software_trigger_pushButton")
        self.gridLayout_3.addWidget(self.software_trigger_pushButton, 4, 0, 1, 2)
        self.trigger_mode_label = QtWidgets.QLabel(self.frame)
        self.trigger_mode_label.setObjectName("trigger_mode_label")
        self.gridLayout_3.addWidget(self.trigger_mode_label, 0, 0, 1, 2)
        self.trigger_source_label = QtWidgets.QLabel(self.frame)
        self.trigger_source_label.setObjectName("trigger_source_label")
        self.gridLayout_3.addWidget(self.trigger_source_label, 2, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 3, 2, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(CameraControlWidget)
        QtCore.QMetaObject.connectSlotsByName(CameraControlWidget)

    def retranslateUi(self, CameraControlWidget):
        _translate = QtCore.QCoreApplication.translate
        self.camera_comboBox.setItemText(0, _translate("CameraControlWidget", "Select Camera..."))
        self.serial_label.setText(_translate("CameraControlWidget", "Serial Number: xxxxxxxx"))
        self.arm_pushButton.setText(_translate("CameraControlWidget", "Arm Camera"))
        self.start_pushButton.setText(_translate("CameraControlWidget", "Start Camera"))
        self.exposure_label.setText(_translate("CameraControlWidget", "Exposure Time (ms)"))
        self.exposure_lineEdit.setText(_translate("CameraControlWidget", "10"))
        self.exposure_pushButton.setText(_translate("CameraControlWidget", "Update Exposure Time"))
        self.continuous_radioButton.setText(_translate("CameraControlWidget", "Continuous"))
        self.software_trigger_radioButton.setText(_translate("CameraControlWidget", "Software"))
        self.hardware_trigger_radioButton.setText(_translate("CameraControlWidget", "Hardware"))
        self.triggered_radioButton.setText(_translate("CameraControlWidget", "Triggered"))
        self.software_trigger_pushButton.setText(_translate("CameraControlWidget", "Software Trigger"))
        self.trigger_mode_label.setText(_translate("CameraControlWidget", "Trigger Mode"))
        self.trigger_source_label.setText(_translate("CameraControlWidget", "Trigger Source:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CameraControlWidget = QtWidgets.QWidget()
    ui = Ui_CameraControlWidget()
    ui.setupUi(CameraControlWidget)
    CameraControlWidget.show()
    sys.exit(app.exec_())
