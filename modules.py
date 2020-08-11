# compiled python files are stored in _pycache_ folder

# from sales import *   || Bad practise to import everything
# 1
import sales  # sales.py
from sales import calc_shipping, calc_tax

calc_shipping()
calc_tax

# 2
sales.calc_tax()
sales.calc_shipping()

# module should contain highly related things
