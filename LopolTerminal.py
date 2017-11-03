import sublime
import sublime_plugin
import subprocess
import os

class Error():

	def GivenWrongPath(path):
		print("[WARNING]LopolTerminal: Folder Not Found " + "\"" + path + "\"")

	def RootNotFound(path):
		print("[WARNING]LopolTerminal: Root Folder Not Found")

class WinTerminalCommand(sublime_plugin.WindowCommand, Error):

	# Returns LIST
	def GetPaths(self):

		root = self.window.folders()
		settings = sublime.load_settings('LopolTerminal.sublime-settings')
		userPaths = settings.get('folders') if settings else None

		if userPaths:	# user set custom paths
			toReturn = []
			for cur in userPaths:					# loop thru given paths
				path = os.path.join(root[0], cur)	# get absoulte path
				if os.path.isdir(path):				# check if given folder exists
					toReturn.append(path)
				else:
					Error.GivenWrongPath(cur)
			return toReturn # return list of absolute paths

		elif root: # we have root folder and empty settings
			return [root[0]]
		else: 
			Error.RootNotFound() # no root and settings


	def run(self):
		for cur in self.GetPaths():
			subprocess.Popen(['cmd'], cwd=cur)