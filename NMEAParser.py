from datetime import datetime 

class NMEAParser(object):
	"""	Parses NMEA Inputs
		debug level:
			0: No debugging Output
			1: Console Output
			2: Raise Not Implemented Error on missing parse function
	"""
	def __init__(self, debug=0):
		self.namespace = globals().copy()
		self.namespace.update(locals())
		self.debug = debug

	def isType(self, sentence, type):
		return sentence[1:3].upper() == type.upper()

	def parseSentence(self, sentence):
		if sentence[:1] is not "$"
			return;

		parseFuncName = 'p_' + sentence[1:3].upper() 
		parseFunc = self.namespace.get(parseFuncName)
		if not parseFunc and debug is 1:
     		print("No implementation for sentence: %s" % sentence)
     	else if not parseFunc and debug is 2:
     		raise NotImplementedError("No implementation for sentence: %s" % sentence)
  		else if parseFunc
			parseFunc(sentence)

class NMEAParserSP(object):
	"""Parses NMEA Inputs"""
	def __init__(self):
		self.namespace = globals().copy()
		self.namespace.update(locals())

	def p_GGA(self, sentence):
		parts = sentence.split(",")
		reParts = {}
		reParts["type"] = "GGA"
		reParts["time"] = datetime.strptime(part[1], "%H%M%S.%f")
		reParts["lat"] = (float(parts[2]), parts[3].upper())
		reParts["long"] = (float(parts[4]), parts[5].upper())
		reParts["height"] = float(parts[9])
		reParts["lastUpdate"] = float(parts[13])
		reParts["checksum"] = int(sentence.split("*")[1])
		return reParts

	def p_RMC(self, sentence):
		parts = sentence.split(",")
		reParts = {}
		reParts["time"] = datetime.strptime(part[1], "%H%M%S.%f")
		reParts["lat"] = (float(parts[3]), parts[4].upper())
		reParts["long"] = (float(parts[5]), parts[6].upper())
		reParts["speed"] = float(parts[7])
		reParts["course"] = float(parts[8])
		reParts["date"] = datetime.strptime(parts[9], "%d%m%y")
		reParts["checksum"] = int(sentence.split("*")[1])
		return reParts		

	def isType(self, sentence, type):
		return sentence[1:3].upper() == type.upper()

	def parseSentence(self, sentence):
		if sentence[:1] is not "$"
			return None;

		parseFuncName = 'p_' + sentence[1:3].upper() 
		parseFunc = self.namespace.get(parseFuncName)
		if not parseFunc:
     		#raise NotImplementedError("No implementation for sentence: %s" % sentence)
     		print("No implementation for sentence: %s" % sentence)
     		return None
  		else
			return parseFunc(sentence)