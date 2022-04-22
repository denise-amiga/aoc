from time import time
import sys
sys.path.insert(0, '../../')  # noqa: E402
from basic import *

t0 = time()
i_raw = my_read_input()
i_txt = [list(map(int, x.split('x'))) for x in i_raw.splitlines()]

print(sum(2 * (a * b + b * c + a * c) + min(a * b, b * c, a * c) for a, b, c in i_txt))
t1 = time()
print('time: ', t1 - t0)
