from hak.pf import f as pf
from hak.pxyf import f as pxyf
from hak.classes.block import Block

f = lambda x: Block(x.split('\n'))

def t_a():
  x = '\n'.join([
    'foobie scoobie',
    'bar',
    'bang'
  ])
  y = Block([
    'foobie scoobie',
    'bar',
    'bang'
  ])
  return pxyf(x, y, f)

def t():
  if not t_a(): return pf('!t_a')
  return 1
