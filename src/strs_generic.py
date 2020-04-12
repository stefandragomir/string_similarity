
from time import time

"""************************************************************************************************
***************************************************************************************************
************************************************************************************************"""
class STRS_ALG_Result(object):

    def __init__(self):

        self.threshold    = 90
        self.similarity   = 0
        self.similar      = False
        self.time         = None
        self.distance     = None
        self.nos          = None
        self.type         = None

    @property
    def similarity(self):

        return self.__similarity

    @similarity.setter
    def similarity(self,value):

        self.__similarity = value
        

        if value >= self.threshold:
            self.similar = True
        else:
            self.similar = False
    
    def __repr__(self):

        return self.__print()

    def __str__(self):

        return self.__print()

    def __print(self):

        _txt  = "SIMILAR         : %s\n" % (self.similar,)
        _txt += "SIMILARITY      : %s%%\n" % ("{:.2f}".format(self.similarity))
        _txt += "THRESHOLD       : %s%%\n" % (self.threshold)
        _txt += "EXECUTION TIME  : %s\n" % (self.time)
        _txt += "DISTANCE        : %s\n" % (self.distance)
        _txt += "NR OF SYMBOLS   : %s\n" % (self.nos)
        _txt += "ALG TYPE        : %s\n" % (self.type)

        return _txt

"""************************************************************************************************
***************************************************************************************************
************************************************************************************************"""
class STRS_ALG_Generic(object):

    def __init__(self,debug=False):

        self.debug  = debug
        self.result = STRS_ALG_Result()

    def log(self,txt):

        print("----> %s" % (txt))

    def read_file(self,path):

        _data = ""

        with open(path,'r+') as _file:

            _data = _file.read()

        return _data

    def compare(self,str1,str2):

        raise "Not Implemented"

    def start_time(self):

        self.__start_time = time()

    def end_time(self):

        self.result.time = time() - self.__start_time

    def get_time(self):

        return self.__end_time - self.start_time