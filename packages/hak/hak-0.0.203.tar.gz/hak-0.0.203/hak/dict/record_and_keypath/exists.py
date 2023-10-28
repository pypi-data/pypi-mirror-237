from hak.pf import f as pf
from hak.pxyf import f as pxyf

def f(x):
  d = x['record']
  if x['keypath']:
    k = x['keypath'][0]
    if k in d:
      return f({'record': d[k], 'keypath': x['keypath'][1:]})
    else:
      return False
  else:
    return True

def t_0():
  x = {'record': {'a': {'b': 0, 'c': 2}}, 'keypath': ('a', 'd')}
  y = False
  return pxyf(x, y, f)

def t_1():
  x = {'record': {'a': {'b': 0, 'c': 2}}, 'keypath': ('a', 'c')}
  y = True
  return pxyf(x, y, f)

def t():
  if not t_0(): return pf('!t_0')
  if not t_1(): return pf('!t_1')
  return 1
