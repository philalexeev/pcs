# main.py

# import mypack.module1
# import mypack.module2

# mypack.module1.greet('phx')
# mypack.module2.depart('phx')

# ----------------------------

# from mypack import module1, module2

# module1.greet('phx')
# module2.depart('phx')

# ----------------------------

# from mypack import module1 as m1, module2 as m2

# m1.greet('phx')
# m2.depart('phx')

# ----------------------------

from mypack.module1 import greet
from mypack.module2 import depart

greet('phx')
depart('phx')

# ----------------------------

from mypack.subpack.module3 import band

for legend in band:
    greet(legend)
