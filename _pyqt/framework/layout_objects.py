'''
layout_objects.py
'''

import sys
from PyQt6.QtCore import Qt
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QStatusBar, QToolBar


class Window(QMainWindow):
	def __init__(self):
		super().__init__(parent=None)
		self.setWindowTitle("QMainWindow")
		self.setCentralWidget(QLabel("Central Widget"))
		self._createMenu()
		self._createToolBar()
		self._createStatusBar()
		self._createFunctionBar()
		
		

	def _createMenu(self):
		menu = self.menuBar().addMenu("&Menu")
		menu.addAction("&Exit", self.close)          # "Exit" action
		
	def _createToolBar(self):
		tools = QToolBar()
		tools.addAction("Exit", self.close)
		self.addToolBar(tools)
		
	def _createStatusBar(self):
		status = QStatusBar()
		status.showMessage("Status Bar")
		self.setStatusBar(status)

	def _createFunctionBar(self):
		functions = QToolBar()
		self.addToolBar(Qt.ToolBarArea.LeftToolBarArea, functions)

	


