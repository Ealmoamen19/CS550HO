import random as r

import math as m

rand = r.randrange(0,2 * m.pi + 1)

value = m.sin(rand) ** 2.0 + m.cos(rand) ** 2.0

print(value)