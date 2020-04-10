"""************************************************************************************************
***************************************************************************************************
************************************************************************************************"""
from Levenshtein  import distance
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

		_dist  = distance(str1,str2)
		_nos   = max(len(str1),len(str2))

		self.result.threshold  = 90
		self.result.similarity = (100.0 / float(_nos)) * (_nos - _dist)

		print(100.0 / float(_nos))
		print(_dist / _nos)

		if self.debug:

			self.log("levenshtein distance      = %s" % (_dist))
			self.log("maximum number of symbols = %s" % (_nos))

		return self.result