from time import time
import sys
sys.path.insert(0, '../../')  # noqa: E402
from basic import *

t0 = time()
i_txt = my_read_input()

lvl = 0
for x, c in enumerate(i_txt):
    if c == '(':
        lvl += 1
    elif c == ')':
        lvl -= 1
    if lvl == -1:
        break
print(x + 1)  # base 0
t1 = time()
print('time: ', t1 - t0)
