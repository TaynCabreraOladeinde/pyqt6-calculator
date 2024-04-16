from PyQt6.QtCore import QSize, Qt, QRect
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QGroupBox,
    QSpinBox,
    QDoubleSpinBox,
    QPushButton
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tip Calculator")
        self.UIComponent()
    def UIComponent(self):
        self.container = QWidget()
        self.container_layout = QVBoxLayout()
        self.container_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.container_layout.setContentsMargins(40, 40, 40, 40)
        self.container_layout.setSpacing(40)
        self.container.setLayout(self.container_layout)
        
        self.setCentralWidget(self.container)
        
        self.title_label = QLabel("Tip Calculator")
        self.container_layout.addWidget(self.title_label)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.title_label.setFont(QFont("Helvetica", 20))
        
        self.before_tip_container = QGroupBox("Before Tip")
        self.container_layout.addWidget(self.before_tip_container)
        self.before_tip_container_layout = QHBoxLayout()
        self.before_tip_container.setLayout(self.before_tip_container_layout)
        
        self.before_tip_doubleSpinBox = QDoubleSpinBox()
        self.before_tip_doubleSpinBox.setMinimumSize(250, 40)
        self.before_tip_doubleSpinBox.setMinimum(0.0)
        self.before_tip_doubleSpinBox.setPrefix("$ ")
        self.before_tip_doubleSpinBox.setSingleStep(10.00)
        self.before_tip_container_layout.addWidget(self.before_tip_doubleSpinBox)
        
        self.tip_percentage_container = QGroupBox("Tip Percent %")
        self.container_layout.addWidget(self.tip_percentage_container)
        self.tip_percentage_container_layout = QHBoxLayout()
        self.tip_percentage_container.setLayout(self.tip_percentage_container_layout)
        
        self.tip_percentage_spinbox = QSpinBox()
        self.tip_percentage_spinbox.setValue(10)
        self.tip_percentage_spinbox.setMinimum(5)
        self.tip_percentage_spinbox.setSingleStep(5)
        self.tip_percentage_spinbox.setMinimumSize(250, 40)
        self.tip_percentage_spinbox.setSuffix(" %")
        self.tip_percentage_container_layout.addWidget(self.tip_percentage_spinbox)
        
        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.setMinimumSize(100, 50)
        self.container_layout.addWidget(self.calculate_button)
        
        


app = QApplication([])

window = MainWindow()

window.show()

app.exec()