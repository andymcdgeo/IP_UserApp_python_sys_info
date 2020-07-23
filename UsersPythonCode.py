__author__ = 'Andy McDonald'
__date__ = '23/07/2020'
__version__ = '0.1'

from Methods import Methods
from IpClassicPythonLink import IPLink
from PGL.IP.API import IntPetroAPI
import sys
import os

class UserApp(Methods, IPLink):

	def UserCode(self):
		# Retrieve all installed packages in the current Python environment
		try:
			from pip._internal.operations import freeze
		except ImportError: # If pip version is < 10.0 then use this command
			from pip.operations import freeze
		
		packages = freeze.freeze()

		if self.out_format == 'File':
			self.write_to_file(packages)
		else:
			self.write_to_ip_messageboard(packages)

	def ipprint(self, input_string):
			messageboard = IntPetroAPI().GetService('PGL.IP.Services.IMessageBoard, PGL.IP.Services')
			messageboard.Add(1, str(input_string))


	def write_to_file(self, packages):
		with open('Python Installation Info.txt', 'w') as f:
			f.write('Python Installation Information\n\n')
			f.write('Python Version:\n')
			f.write('    ' + sys.version+ '\n')
			f.write('IP Installation Folder:\n')
			f.write('    ' + sys.executable + '\n\n')
			f.write('Python Paths:\n')
			for path in sys.path:
				f.write('    ' + path + '\n')
			f.write('\nCurrent Working Directory:\n')
			f.write('    ' + os.getcwd() + '\n\n')

			f.write('Installed Packages & Versions:\n')
			for package in packages:
				f.write(package + '\n')

	def write_to_ip_messageboard(self, packages):
		self.ipprint('Python Installation Information\n')
		self.ipprint('Python Version:\n')
		self.ipprint('    ' + sys.version+ '\n')
		self.ipprint('IP Installation Folder:\n')
		self.ipprint('    ' + sys.executable + '\n\n')
		self.ipprint('Python Paths:\n')
		for path in sys.path:
				self.ipprint('    ' + path + '\n')
		self.ipprint('\nCurrent Working Directory:\n')
		self.ipprint('    ' + os.getcwd() + '\n\n')

		self.ipprint('Installed Packages & Versions:\n')
		for package in packages:
			self.ipprint(package + '\n')