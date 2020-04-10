
#python strs.py --file1=c:\projects\string_similarity\data\data_1.txt --file2=c:\projects\string_similarity\data\data_2.txt --alg=0 --debug

"""************************************************************************************************
***************************************************************************************************
************************************************************************************************"""
import os
import sys

from argparse         import ArgumentParser
from strs_levenshtein import STRS_ALG_Levenshtein
from strs_sorensen    import STRS_ALG_Sorensen
from strs_jaccard     import STRS_ALG_Jaccard

"""************************************************************************************************
***************************************************************************************************
************************************************************************************************"""
class STRS_Arguments(object):

    arguments = None

    def __init__(self):

        self.arg = ArgumentParser()

        self._add_arguments()

        self.arguments = self._parse_arguments()

    def _add_arguments(self):

        self.arg.add_argument('--file1',       type=str,              help='first string file to compare')
        self.arg.add_argument('--file2',       type=str,              help='second string file to compare')  
        self.arg.add_argument('--alg',         type=str,              help='algoritm to use: 0-levenshtein 1-sorensen 2-jaccard ')
        self.arg.add_argument('--debug',       action='store_true',   help='verbose') 

    def _parse_arguments(self):

        if len(sys.argv) == 1:

            self.arg.print_help()

            sys.exit(1)

        return self.arg.parse_args()

"""************************************************************************************************
***************************************************************************************************
************************************************************************************************"""
class STRS(STRS_Arguments):

    def __init__(self):

        STRS_Arguments.__init__(self)

    def run(self):

        _MAP = {
                    "0": STRS_ALG_Levenshtein,
                    "1": STRS_ALG_Sorensen,
                    "2": STRS_ALG_Jaccard,
                }

        if self.arguments.alg in list(_MAP.keys()):

            _alg = _MAP[self.arguments.alg](self.arguments.debug)

            if os.path.exists(str(self.arguments.file1)):

                _str1 = _alg.read_file(self.arguments.file1)

                if os.path.exists(str(self.arguments.file2)):

                    _str2 = _alg.read_file(self.arguments.file2)

                    _result = _alg.compare(_str1,_str2)

                    print(_result)
                    
                else:
                    print("error: file2 does not exist")
            else:
                print("error: file1 does not exist")
        else:
            print("error: unknown algorithm")


"""************************************************************************************************
***************************************************************************************************
************************************************************************************************"""
if __name__ == '__main__':

    _strs = STRS()

    _strs.run()