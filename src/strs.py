
#python strs.py --file1=c:\projects\string_similarity\data\data_1.txt --file2=c:\projects\string_similarity\data\data_2.txt --alg=0 --debug

"""************************************************************************************************
***************************************************************************************************
************************************************************************************************"""
import os
import sys

from argparse                  import ArgumentParser
from strs_levenshtein          import STRS_ALG_Levenshtein
from strs_hamming              import STRS_ALG_Hamming
from strs_damerau_levenshtein  import STRS_ALG_Damerau_Levenshtein
from strs_gotoh                import STRS_ALG_Gotoh
from strs_jaro                 import STRS_ALG_Jaro
from strs_jaro_winkler         import STRS_ALG_Jaro_Winkler
from strs_mlipns               import STRS_ALG_Mlipns
from strs_needleman_wunsch     import STRS_ALG_Needleman_Wunsch
from strs_smith_waterman       import STRS_ALG_Smith_Waterman
from strs_strcmp95             import STRS_ALG_Strccmp95


"""************************************************************************************************
***************************************************************************************************
************************************************************************************************"""
_ALG_MAP = [
                STRS_ALG_Levenshtein,
                STRS_ALG_Hamming,
                STRS_ALG_Damerau_Levenshtein,
                STRS_ALG_Gotoh,
                STRS_ALG_Jaro,
                STRS_ALG_Jaro_Winkler,
                STRS_ALG_Mlipns,
                STRS_ALG_Needleman_Wunsch,
                STRS_ALG_Smith_Waterman,
                STRS_ALG_Strccmp95,
            ]

"""************************************************************************************************
***************************************************************************************************
************************************************************************************************"""
class STRS_Arguments(object):

    arguments = None

    def __init__(self):

        self.arg = ArgumentParser()

        self._add_arguments()

        self.arguments = self._parse_arguments()

    def _get_alg_help(self):

        _txt = ""

        for _key in range(len(_ALG_MAP)):

            _txt += "%s-%s  " % (_key,_ALG_MAP[_key].__name__.split("STRS_ALG_")[1].lower())

        return _txt

    def _add_arguments(self):

        self.arg.add_argument('--file1',       type=str,              help='first string file to compare')
        self.arg.add_argument('--file2',       type=str,              help='second string file to compare')  
        self.arg.add_argument('--alg',         type=str,              help=self._get_alg_help())
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

        if self.arguments.alg != "all":

            self.arguments.alg = int(self.arguments.alg)

            self.run_alg(
                            int(self.arguments.alg),
                            self.arguments.file1,
                            self.arguments.file2,
                            self.arguments.debug
                        )
        else:
            for _index in range(len(_ALG_MAP)):

                self.run_alg(
                                _index,
                                self.arguments.file1,
                                self.arguments.file2,
                                self.arguments.debug
                            )
         

    def run_alg(self,index,file1,file2,debug):

        if index in range(len(_ALG_MAP)):

            _alg = _ALG_MAP[index](debug)

            if os.path.exists(str(file1)):

                _str1 = _alg.read_file(file1)

                if os.path.exists(str(file2)):

                    _str2 = _alg.read_file(file2)

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