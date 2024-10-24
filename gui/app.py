from PyQt5.QtWidgets import QApplication, QStyleFactory
from gui.main_window import MainWindow
import params

"""
The App class inherits from QApplication,
it manages the GUI application
"""

class App(QApplication):
	def __init__(self, project: "Project"):
		super().__init__([])
		self.project = project 	# store the project reference
		
		# create the main window
		style = QStyleFactory.create(params.style) 	# create Qt5 style
		self.setStyle(style) 		 				# set Qt5 style
		self.window = MainWindow() 					# create the main window
		
		# reposition the window to the second screen if necessary
		screens = self.screens()
		if params.second_screen and len(screens) > 1:
			second_screen = screens[1]
			screen_geometry = second_screen.geometry()
			self.window.move(screen_geometry.left(), screen_geometry.top())
		
		self.window.center() 		# center the window within the screen
		
		# display the window
		if params.full_screen:
			self.window.showMaximized()
		else:
			self.window.show()