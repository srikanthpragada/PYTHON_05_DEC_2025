import sys

# add new folder to module search path
sys.path.append(r'c:\classroom\dec5\demo\lib')

print(sys.path)  # print module search path

import strfuns as sf
print(sf.countupper('Abc'))



