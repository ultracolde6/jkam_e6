from enum import Enum
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget
from package.ui.imagecapturemodewidget_ui import Ui_ImageCaptureModeWidget
from package.widgets.cameracontrolwidget import TriggerMode


class ImagingMode(Enum):
    VIDEO = 0
    ABSORPTION = 1
    FLUORESCENCE = 2


class LockMode(Enum):
    UNLOCKED = 0
    LOCKED = 1


class ImageCaptureModeWidget(QWidget, Ui_ImageCaptureModeWidget):
    state_set_signal = pyqtSignal(object)

    def __init__(self, parent=None):
        super(ImageCaptureModeWidget, self).__init__(parent=parent)
        self.setupUi(self)

        self.lock_mode = LockMode.UNLOCKED
        self.trigger_mode = TriggerMode.TRIGGERED
        self.imaging_mode = ImagingMode.VIDEO
        self.set_state()
        self.image_capture_buttonGroup.buttonClicked.connect(self.set_imaging_mode)
        self.set_imaging_mode()

    def set_state(self):
        if self.lock_mode is LockMode.UNLOCKED:
            self.unlock()
            self.set_trigger_mode(self.trigger_mode)
            self.set_imaging_mode()
        elif self.lock_mode is LockMode.LOCKED:
            self.lock()

    def set_trigger_mode(self, trigger_mode):
        self.trigger_mode = trigger_mode
        if self.trigger_mode is TriggerMode.CONTINUOUS:
            self.video_mode_radioButton.setChecked(True)
            self.absorption_mode_radioButton.setEnabled(False)
            self.fluorescence_mode_radioButton.setEnabled(False)
        elif self.trigger_mode is TriggerMode.TRIGGERED:
            self.video_mode_radioButton.setEnabled(True)
            self.absorption_mode_radioButton.setEnabled(True)
            self.fluorescence_mode_radioButton.setEnabled(True)
        self.set_imaging_mode()

    def set_imaging_mode(self):
        if self.video_mode_radioButton.isChecked():
            self.imaging_mode = ImagingMode.VIDEO
        elif self.absorption_mode_radioButton.isChecked():
            self.imaging_mode = ImagingMode.ABSORPTION
        elif self.fluorescence_mode_radioButton.isChecked():
            self.imaging_mode = ImagingMode.FLUORESCENCE
        self.state_set_signal.emit(self.imaging_mode)

    def lock(self):
        self.video_mode_radioButton.setEnabled(False)
        self.absorption_mode_radioButton.setEnabled(False)
        self.fluorescence_mode_radioButton.setEnabled(False)

    def unlock(self):
        self.video_mode_radioButton.setEnabled(True)
        self.absorption_mode_radioButton.setEnabled(True)
        self.fluorescence_mode_radioButton.setEnabled(True)
        self.set_trigger_mode(self.trigger_mode)
