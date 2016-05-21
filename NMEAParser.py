#nmea
class NMEAParser(object):
	"""Parses NMEA Inputs"""
	def __init__(self):
		pass


	def p_GGA(self, sentence):
		

	def parseSentence(self, sentence):
		if sentence[:1] is not "$"
			return None;

		parseFuncName = 'p_' + sentence[1:3].upper() 
		namespace = globals().copy()
		namespace.update(locals())
		parseFunc = namespace.get(parseFuncName)
		if not parseFunc:
     		#raise NotImplementedError("No implementation for sentence: %s" % sentence)
     		print("No implementation for sentence: %s" % sentence)
     		return None
  		else
			return parseFunc(sentence)




		
