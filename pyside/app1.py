#from PySide.QtCore import *
from PySide.QtGui import *
from sys import exit, argv

class Window(QWidget):
	"""docstring for Window"""
	def __init__(self):
		QWidget.__init__(self)
		self.btnSumar = QPushButton("sumar")
		layout = QVBoxLayout()

app = QApplication(argv)
window = Window()
window.setWindowTitle("primera app PySide")
window.show()
exit(app.exec_())
