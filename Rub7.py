import sys

import math as m 

t = float(sys.argv[3])

r = float(sys.argv[2])

rr = float(r/100)

p = float(sys.argv[1])

print(p * (m.e ** (rr * t)))

