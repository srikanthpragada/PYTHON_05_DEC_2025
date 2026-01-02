import sys

#print(sys.argv)
if len(sys.argv) < 2:
    print('Sorry! Name not found!')
else:
    print ('Hello', sys.argv[1])