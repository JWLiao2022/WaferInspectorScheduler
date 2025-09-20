from PySide6.QtCore import QThread, Signal, QTimer

def seconds_to_hms(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return hours, minutes, secs


class CountdownTimer(QThread):
    timeUp = Signal()
    messageUpdate = Signal(str)

    def __init__(self, seconds, parent=None):
        super().__init__(parent)
        self.remaining = seconds
        self.timer = QTimer(self)
        self.timer.timeout.connect(self._tick)

    def start(self):
        self.timer.start(1000)

    def _tick(self):
        if self.remaining > 0:
            hours, minutes, secs = seconds_to_hms(self.remaining)
            msg = f"Time left: {hours}h {minutes}m {secs}s"
            print(msg, end="\r")
            self.messageUpdate.emit(msg)
            self.remaining -= 1
        else:
            self.timer.stop()
            print("Countdown finished!")
            self.messageUpdate.emit("Countdown finished!")
            self.timeUp.emit()
