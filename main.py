from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QGridLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QFileDialog
)
import os
import numpy as np

app = QApplication([])

class MainWindow(QMainWindow):
    def __init__(self,thedata) -> None:
        super().__init__()
        self.setWindowTitle("Database viewer")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Database Viewer"))
        gridWidget = QWidget()
        gridLayout = QGridLayout()
        gridWidget.setLayout(gridLayout)
        
        for i in range(thedata.shape[0]):
            for j in range(thedata.shape[1]):
                gridLayout.addWidget(QLineEdit(f"{thedata[i][j]}"), i, j)
        
        layout.addWidget(gridWidget)
        RENDER_WIDGET = QWidget()
        RENDER_WIDGET.setLayout(layout)
        self.setCentralWidget(RENDER_WIDGET)
 
 
class MainMenu(QMainWindow):
 
    def openFile(self) -> None:
        fileDialog = QFileDialog()
        fileDialog.setNameFilter(("CSV (*.csv)"))
        fileDialog.setFileMode(QFileDialog.ExistingFile)
        fileDialog.setViewMode(QFileDialog.Detail)
        fileDialog.setLabelText(QFileDialog.Accept, "Open")
        fileDialog.setLabelText(QFileDialog.Reject, "Cancel")
        fileDialog.setWindowTitle("Open File")
        fileDialog.setDirectory(os.getcwd())
        if fileDialog.exec() == QFileDialog.Accepted:
            fileName = fileDialog.selectedFiles()[0]
            thedata = np.loadtxt(fileName, delimiter=",", dtype=str)
            self.setVisible(False)
            nextwin = MainWindow(thedata=thedata)
            nextwin.show()
 
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Main Menu")
        mainWidget = QWidget()
        mainLayout = QVBoxLayout()
        openFileButton = QPushButton("Open A .csv file")
        openFileButton.clicked.connect(self.openFile)
        mainLayout.addWidget(openFileButton)
       
        mainWidget.setLayout(mainLayout)
        self.setCentralWidget(mainWidget)
 
menu = MainMenu()
menu.show()
app.exec()
