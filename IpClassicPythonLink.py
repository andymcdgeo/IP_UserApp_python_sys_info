class IPLink:

	def SetupParameters(self, CnIn, CnOut, ParIn, TxtParIn, FlagIn, StIndex, SpIndex, ZoneNum, TotZones, AXIn, AYIn, AXOut, AYOut, ParamCrvIn):
		self._inputCurves = list(CnIn)
		self._outputCurves = list(CnOut)
		self._inputParameters = list(ParIn)
		self._textInputParameters = list(TxtParIn)
		self._flagInputParameters = list(FlagIn)
		self._topIndex = StIndex
		self._bottomIndex = SpIndex
		self._totalZones = TotZones
		self._zoneNumber = ZoneNum
		self._inArrayX = list(AXIn)
		self._inArrayY = list(AYIn)
		self._outArrayX = list(AXOut)
		self._outArrayY = list(AYOut)
		self._parCnIn = list(ParamCrvIn)

	def ResetZoneParameters(self, ParIn, TxtParIn, FlagIn, ParamCrvIn, StIndex, SpIndex, ZoneNum):
		self._inputParameters = list(ParIn)
		self._textInputParameters = list(TxtParIn)
		self._flagInputParameters = list(FlagIn)
		self._parCnIn = list(ParamCrvIn)
		self._topIndex = StIndex
		self._bottomIndex = SpIndex
		self._zoneNumber = ZoneNum

	def SetupIPProxy(self, ip):
		self._IPProxy = ip

	def Run(self):
		self.UserCode()

	def get_TopDepth(self):
		return self._topIndex

	TopDepth = property(fget=get_TopDepth)

	def get_BottomDepth(self):
		return self._bottomIndex

	BottomDepth = property(fget=get_BottomDepth)

	def get_TotalZones(self):
		return self._totalZones

	TotalZones = property(fget=get_TotalZones)

	def get_ZoneNumber(self):
		return self._zoneNumber

	ZoneNumber = property(fget=get_ZoneNumber)

	def SetZone(self, zoneNum):
		self._IPProxy.SetZone(zoneNum)

	def get_Well_Name(self):
		return self.Read_Well_Attribute("WellName")

	Well_Name = property(fget=get_Well_Name)

	def get_Well_Company(self):
		return self.Read_Well_Attribute("Company")

	Well_Company = property(fget=get_Well_Company)

	def get_Well_Field(self):
		return self.Read_Well_Attribute("Field")

	Well_Field = property(fget=get_Well_Field)

	def Read_Well_Attribute(self, attributeName):
		return self._IPProxy.GetWellText(attributeName)

	def Write_Well_Attribute(self, attributeName, value):
		self._IPProxy.SetWellText(attributeName, value)

	def Read_Log_Attribute(self, attributeName, logRunNum):
		return self._IPProxy.GetLogText(attributeName, logRunNum)

	def Write_Log_Attribute(self, attributeName, value, logRunNum):
		self._IPProxy.SetLogText(attributeName, value, logRunNum)

	def Read_Curve_Attribute(self, curveNumber, attributeName):
		return self._IPProxy.GetText(2, curveNumber, attributeName)

	def Write_Curve_Attribute(self, curveNumber, attributeName, value):
		self._IPProxy.SetText(2, curveNumber, attributeName, value)

	# flags: 0 = Well, 1 = Log, 2 = Curve...
	def Read_Text(self, flags, index, attributeName):
		return self._IPProxy.GetText(flags, index, attributeName)

	def Write_Text(self, flags, index, attributeName, value):
		self._IPProxy.SetText(flags, index, attributeName, value)