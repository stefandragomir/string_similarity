"""************************************************************************************************
***************************************************************************************************
************************************************************************************************"""
from textdistance import jaro
from strs_generic import STRS_ALG_Generic

"""************************************************************************************************
***************************************************************************************************
************************************************************************************************"""
class STRS_ALG_Jaro(STRS_ALG_Generic):

	def __init__(self,debug=True):

		STRS_ALG_Generic.__init__(self,debug=debug)

		self.result.type = "edit"

	def compare(self,str1,str2):

		if self.debug:
			self.log("jaro comparison")

		self.start_time()

		self.result.distance  = jaro(str1,str2)

		self.end_time()

		self.result.nos         = max(len(str1),len(str2))
		self.result.threshold  = 90
		self.result.similarity = self.result.distance * 100

		return self.result