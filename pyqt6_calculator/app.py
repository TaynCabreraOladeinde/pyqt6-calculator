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
        
        self.buttons_container = QWidget()
        self.buttons_container_layout = QHBoxLayout()
        self.buttons_container.setLayout(self.buttons_container_layout)
        self.container_layout.addWidget(self.buttons_container)
        
        self.reset_button = QPushButton("Reset")
        self.reset_button.setMinimumSize(100, 50)
        self.reset_button.clicked.connect(self.reset)
        self.buttons_container_layout.addWidget(self.reset_button)
        
        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.setMinimumSize(100, 50)
        self.calculate_button.clicked.connect(self.calculate_tip)
        self.buttons_container_layout.addWidget(self.calculate_button)
        
        
        self.tip_amount_label = QLabel("Tip Amount: N/A")
        self.tip_amount_label.setFont(QFont("Helvetica", 12))
        self.tip_amount_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.container_layout.addWidget(self.tip_amount_label)
        
        self.after_tip_label = QLabel("After Tip: N/A")
        self.after_tip_label.setFont(QFont("Helvetica", 12))
        self.after_tip_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.container_layout.addWidget(self.after_tip_label)
    
    def calculate_tip(self):
        tip_amount = self.before_tip_doubleSpinBox.value() * (self.tip_percentage_spinbox.value() / 100)
        after_tip = tip_amount + self.before_tip_doubleSpinBox.value()
        self.tip_amount_label.setText(f"Tip Amount: ${round(tip_amount, 2)}")
        self.after_tip_label.setText(f"After Tip: ${round(after_tip, 2)}")
    
    def reset(self):
        self.before_tip_doubleSpinBox.setValue(0.00)
        self.tip_percentage_spinbox.setValue(10)
        self.tip_amount_label.setText(f"Tip Amount: N/A")
        self.after_tip_label.setText(f"After Tip: N/A")


app = QApplication([])

window = MainWindow()

window.show()

app.exec()
