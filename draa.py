from prody import *
from pylab import *

parse = parsePDB('5eh1')

plt = showProtein(parse)
show(plt)