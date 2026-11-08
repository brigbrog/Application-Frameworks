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


# fear not

class Window(QMainWindow):
	def __init__(self):
		super().__init__(parent=None)

		self.resize(1000, 800)
		self.setWindowTitle("QMainWindow")
		
		# initialize the interface
		self._init_ui()


	def _init_ui(self):
		pass


	def _createMenu(self):
		menubar = self.menuBar()
		menubar.setNativeMenuBar(False)
		file_menu = menubar.addMenu("&Menu")
		file_menu.addAction("&Exit", self.close)
		# other menu actions

		
	def _createToolBar(self):
		tools = QToolBar()
		tools.addAction("Exit", self.close)
		self.addToolBar(tools)
		
	def _createStatusBar(self, message = "Status Bar"):
		status = QStatusBar()
		status.showMessage(message)
		self.setStatusBar(status)

	def _createFunctionBar(self):
		functions = QToolBar()
		self.addToolBar(Qt.ToolBarArea.LeftToolBarArea, functions)


class ImageWindow(Window):
	def __init__(self, windowTitle="Image Viewer"):
		super().__init__() 
		self.setWindowTitle(windowTitle)
		self.scene = None 


	def _init_ui(self):
	
		self.graphicsView = QGraphicsView()
		self.setCentralWidget(self.graphicsView)
		self._createImageToolBar()
		self._createStatusBar(message="status")


	def _createImageToolBar(self):

		functions = QToolBar()

		# add methods actions in subclass override like this: 
		functions.addAction("LOAD IMAGE", self._loadImage)
		functions.addAction("EXPORT IMAGE", self._exportImage)

		# add functions to the toolbar
		self.addToolBar(Qt.ToolBarArea.LeftToolBarArea, functions)


	def _loadImage(self):
		# Override with subclass implementation
		pass
		# fpath, _ = QFileDialog.getOpenFileName(
		# 		self, "Select Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)"
		# 	)
		# if not fpath:
		# 	return

		# image_pil = Image.open(fpath)
		# image_pil = image_pil.convert("L")

		# im_data = image_pil.tobytes("raw", "L")
		# qimage = QImage(
		# 	im_data, 
		# 	image_pil.width,
		# 	image_pil.height, 
		# 	image_pil.width, 
		# 	QImage.Format.Format_Grayscale8
		# )

		# pixmap = QPixmap.fromImage(qimage)
		# self._reload_canvas(pixmap)


	def _exportImage(self):
		# Override with subclass implementation		
		pass
		# if not self.scene:
		# 	print("VOID SCENE") # <----------------------- SEND TO STATUS
		# 	return None
		
		# fpath, _ = QFileDialog.getSaveFileName(
		# 		self, "Select Save Location", "", ""
		# 	)
		# if not fpath:
		# 	return


	def _reload_canvas(self, pixmap: QPixmap):
		if self.scene is None:
			self.scene = QGraphicsScene(self)
			self.graphicsView.setScene(self.scene)
		else:
			self.scene.clear()

		self.pixmap_item = QGraphicsPixmapItem(pixmap)
		self.scene.addItem(self.pixmap_item)
		self.graphicsView.fitInView(self.pixmap_item, Qt.AspectRatioMode.KeepAspectRatio)
	









