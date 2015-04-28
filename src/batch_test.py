__author__ = 'tylorchilders'

import linear_least_squares,sys,multi_class_linsqu
from cStringIO import StringIO

RUNS = 3

backup = sys.stdout

sys.stdout = StringIO()
linear_least_squares.main(RUNS)
single = sys.stdout.getvalue().split(",")
sys.stdout.close()

sys.stdout = StringIO()
multi_class_linsqu.main(RUNS)
multi = sys.stdout.getvalue().split(",")
sys.stdout.close()

sys.stdout = backup

print single
print multi