import sublime
import sublime_plugin
import os.path

def openJs(window, dirName, filePath):
	if os.path.isfile(dirName + '/controllers/' + filePath + '.js'):
		window.open_file(dirName + '/controllers/' + filePath + '.js')
	else:
		print("no js")

def openTss(window, dirName, filePath):
	if os.path.isfile(dirName + '/styles/' + filePath + '.tss'):
		window.open_file(dirName + '/styles/' + filePath + '.tss')
	else:
		print("no tss")

def openXml(window, dirName, filePath):
	if os.path.isfile(dirName + '/views/' + filePath + '.xml'):
		window.open_file(dirName + '/views/' + filePath + '.xml')
	else:
		print("no xml")

#TODO: nested folder structures
class SurfTiopenCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		filePath = self.view.file_name()

		if filePath:
			root, ext = os.path.splitext(filePath)

			pathList = root.split("/")

			endFolder = ''
			filePath = ''

			if ext == '.js':
				endFolder = 'controllers'
			elif ext == '.tss':
				endFolder = 'styles'
			elif ext == '.xml':
				endFolder = 'views'

			#get paths before and after end folder (controllers, styles, or views)
			endIndex = pathList.index(endFolder)
			dirName = "/".join(pathList[:endIndex])
			filePath = "/".join(pathList[(endIndex + 1):])

			if ext == '.js':
				openTss(self.view.window(), dirName, filePath)
				openXml(self.view.window(), dirName, filePath)
			elif ext == '.tss':
				openJs(self.view.window(), dirName, filePath)
				openXml(self.view.window(), dirName, filePath)
			elif ext == '.xml':
				openJs(self.view.window(), dirName, filePath)
				openTss(self.view.window(), dirName, filePath)
