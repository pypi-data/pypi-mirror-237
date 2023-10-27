# The main function provides a commandline interface for the package.
# This way you can use it via python -m modulename.
import sys
import pycutroh

def main():
    if len(sys.argv) > 1 and sys.argv[1] in ('-h','--help'):
        help(pycutroh)
    else:
        help(pycutroh)

if __name__ == '__main__':
    main()