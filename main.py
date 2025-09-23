import sys

from PySide6.QtCore import QThread, Slot, QDateTime
from PySide6.QtWidgets import QApplication, QWidget
from WaferInspectorSchedulerUI.ui_form import Ui_Widget
from TCP_Client.TCP import clsTCPClient
from Timer import CountdownTimer

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        #Initialise the UI
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Set dateTimeEdit to current date and time
        self.ui.dateTimeEdit.setDateTime(QDateTime.currentDateTime())

        #Disable the start scheduling button and the stop scheduling button.
        self.ui.pushButton_StartScheduling.setEnabled(False)
        self.ui.pushButton_StopScheduling.setEnabled(False)

        #Connect the button to the functions
        #Start a connection button
        self.ui.pushButton_MW3Connect.clicked.connect(self.estabilishAConnection)
        #Connect the start drawing button
        self.ui.pushButton_StartScheduling.clicked.connect(self.startScheduling)
        #Initial the global parameter
        self.currentStatus = ''
        self.currentAction = ''
        

    def estabilishAConnection(self):
        #Start a new connection to MW3
        #Read the user input port number
        self.portNumber  = int(self.ui.lineEdit_MW3PortNumber.text())
        self.newConnection = clsTCPClient(self.portNumber)
        #Create a QThread object
        self.thread = QThread()
        #Move the processing to the thread
        self.newConnection.moveToThread(self.thread)
        #Connect signals and slots
        self.thread.started.connect(self.newConnection.makeNewConnection)
        self.newConnection.finished.connect(self.thread.quit)
        self.newConnection.finished.connect(self.newConnection.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.newConnection.signalIsConnected.connect(self.afterFirstTimeConnection)
        self.newConnection.signalResponseFromMW3.connect(self.reportCurrentStatus)
        
        #Start the thread
        self.thread.start()

    @Slot()
    def afterFirstTimeConnection(self):
        self.ui.pushButton_MW3Connect.setEnabled(False)
        self.ui.pushButton_MW3Connect.setText('Connected')
        self.ui.lineEdit_MW3PortNumber.setEnabled(False)
        self.ui.pushButton_StartScheduling.setEnabled(True)
    
    @Slot()
    def reportCurrentStatus(self, currentStatus):
        print(currentStatus)
        self.currentStatus = currentStatus
    
    @Slot()
    def startScheduling(self):
        #Calculate the time difference in seconds
        now = QDateTime.currentDateTime()
        target = self.ui.dateTimeEdit.dateTime()
        diff_seconds = now.secsTo(target)
        #print(f"Scheduling will start in {diff_seconds} seconds.")
        #self.currentStatus = f"Scheduling will start in {diff_seconds} seconds."
        #self.ui.label_CurrentStatus.setText(self.currentStatus)
         #Start a countdown timer
        self.timer = CountdownTimer(diff_seconds)
        #Start a new thread for the countdown timer
        self.timerThread = QThread()
        self.timer.moveToThread(self.timerThread)
        self.timerThread.started.connect(self.timer.start)
        #When the measurement is finished, clean up the timer and the thread
        self.timer.finished.connect(self.timerThread.quit)
        self.timer.finished.connect(self.timer.deleteLater)
        self.timerThread.finished.connect(self.timerThread.deleteLater)
       
        self.timer.messageUpdate.connect(self.updateCountdownMessage)
        self.timer.timeUp.connect(self.executeScheduling)
        self.timer.timeForPreparation.connect(self.preparationForWaferInspection)

        self.timerThread.start()
        #Disable the start scheduling button and enable the stop scheduling button
        self.ui.pushButton_StartScheduling.setEnabled(False)
        self.ui.pushButton_StopScheduling.setEnabled(True)

        
    
    @Slot(str)
    def updateCountdownMessage(self, message):
        self.currentStatus = message
        self.ui.label_CurrentStatus.setText(self.currentStatus)

    @Slot()
    def executeScheduling(self):
        print("Executing wafer inspection")
        self.currentAction = "Executing wafer inspection"
        self.ui.label_CurrentStatus_2.setText(self.currentAction)
        #Here you can add the code to start the actual scheduling process
        #For example, sending commands to MW3 via self.newConnection
        self.newConnection.sendACommand('WaferInspectorStart()')
        #After scheduling is done, re-enable the start scheduling button and disable the stop scheduling button
        self.ui.pushButton_StartScheduling.setEnabled(False)
        self.ui.pushButton_StopScheduling.setEnabled(True)
        #self.timerThread.quit()
        #self.timerThread.wait()
        
    
    @Slot()
    def preparationForWaferInspection(self):
        print("Autofocusing...")
        self.currentAction = "Autofocusing..."
        self.ui.label_CurrentStatus_2.setText(self.currentAction)
        self.newConnection.sendACommand('DoAutofocus()')
        print("Refreshing markers...")
        self.currentAction = "Refreshing markers..."
        self.ui.label_CurrentStatus_2.setText(self.currentAction)
        self.newConnection.sendACommand('RefreshMarkers()')
        print("Transforming coordinates...")
        self.currentAction = "Transforming coordinates..."
        self.ui.label_CurrentStatus_2.setText(self.currentAction)
        self.newConnection.sendACommand('IncludeOffsetCorrection()')
        self.newConnection.sendACommand('IncludeRotationCorrection()')
        self.newConnection.sendACommand('IncludeSlopeCorrection()')
        self.newConnection.sendACommand('ExcludeStretchShearCorrection()')
        self.newConnection.sendACommand('AlignExpectedToActual()')
        self.newConnection.sendACommand('MoveToOrigin()')
        #Updating status
        print("Preparation done. Waiting for the inspection to start...")
        self.currentAction = "Preparation done. Waiting for the inspection to start..."
        self.ui.label_CurrentStatus_2.setText(self.currentAction)

if __name__=="__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    #Move the widget to the bottom left of the monitor position
    widget.move(10,650)
    

    sys.exit(app.exec())