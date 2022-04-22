from time import time
import sys
sys.path.insert(0, '../../')  # noqa: E402
from basic import *

t0 = time()
i_txt = my_read_input()

t1 = time()
print('time: ', t1 - t0)
