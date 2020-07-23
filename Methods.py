# /***********************************************/
#  * File dynamically created from IP: 23/07/2020 11:59:55
#  * DO NOT MANUALLY EDIT
# /***********************************************/

class Methods:
	def __init__(self):
		self._FIRST_AVAILABLE_LOG_RUN = -1
		self._LAST_AVAILABLE_LOG_RUN = -2

	def Depth(self, index):
		return self._IPProxy.GetCurveData(1, index)

	def get_out_format(self):
		return self._textInputParameters[0]

	out_format = property(fget=get_out_format)

