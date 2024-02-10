import sys
from gugik_getter import CorrectErrors

print(sys.argv)
CorrectErrors(sys.argv[1]).correct_in_loop()
