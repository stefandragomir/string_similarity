"""************************************************************************************************
***************************************************************************************************
************************************************************************************************"""
from textdistance import levenshtein
from strs_generic import STRS_ALG_Generic

"""************************************************************************************************
***************************************************************************************************
************************************************************************************************"""
class STRS_ALG_Levenshtein(STRS_ALG_Generic):

	def __init__(self,debug=True):

		STRS_ALG_Generic.__init__(self,debug=debug)

	def compare(self,str1,str2):

		if self.debug:
			self.log("levenshtein comparison")

		self.start_time()

		self.result.distance  = levenshtein(str1,str2)

		self.end_time()

		self.result.nos         = max(len(str1),len(str2))
		self.result.threshold  = 90
		self.result.similarity = (100.0 / float(self.result.nos)) * (self.result.nos - self.result.distance)
		
		return self.result