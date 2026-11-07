'''
layout_objects.py
'''

import sys
from PIL import Image

from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import (
	Qt
	)
from PyQt6 import (
	QtWidgets
	)
from PyQt6.QtWidgets import (
	QApplication,
	QLabel,
	QMainWindow,
	QStatusBar,
	QToolBar,
	QGraphicsView,
	QFileDialog,
	QGraphicsScene,
	QGraphicsPixmapItem
	)




class Window(QMainWindow):
	def __init__(self):

		super().__init__(parent=None)
		self.setWindowTitle("QMainWindow")
		self.setCentralWidget(QLabel("Central Widget"))
		
		#self._createImageViewer()

		self._createMenu()
		#self._createToolBar()
		self._createStatusBar()
		#self._createFunctionBar()
		
		

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


class ImageWindow(Window):
	def __init__(self):
		super().__init__()

		self.resize(1000, 800)
		self.setWindowTitle("Image Viewer")

		self.graphicsView = QGraphicsView()
		self.setCentralWidget(self.graphicsView)

		self.scene = None
		self._createImageToolBar()


	def _createImageToolBar(self):
		functions = QToolBar()
		functions.addAction("LOAD IMAGE", self._loadImage)

		# add more functions
		self.addToolBar(Qt.ToolBarArea.LeftToolBarArea, functions)


	def _loadImage(self):
		fpath, _ = QFileDialog.getOpenFileName(
				self, "Select Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)"
			)
		if not fpath:
			return

		image_pil = Image.open(fpath)
		image_pil = image_pil.convert("L")

		im_data = image_pil.tobytes("raw", "L")
		qimage = QImage(
			im_data, 
			image_pil.width, 
			image_pil.height, 
			image_pil.width, 
			QImage.Format.Format_Grayscale8
		)

		pixmap = QPixmap.fromImage(qimage)
		self.reload_canvas(pixmap)


	def reload_canvas(self, pixmap: QPixmap):
		if self.scene is None:
			self.scene = QGraphicsScene(self)
			self.graphicsView.setScene(self.scene)
		else:
			self.scene.clear()

		self.pixmap_item = QGraphicsPixmapItem(pixmap)
		self.scene.addItem(self.pixmap_item)
		self.graphicsView.fitInView(self.pixmap_item, Qt.AspectRatioMode.KeepAspectRatio)
	









