from hak.pxyz import f as pxyz
from hak.pf import f as pf

# remove leaves from tree where value
f = lambda tree, value: {
  k: (
    f(tree[k], value)
    if isinstance(tree[k], dict) else
    v
  )
  for (k, v) in tree.items()
  if v != value
}

def t_0():
  x = {
    'tree': {
      'a': 0,
      'b': {
        'c': 2,
        'd': {
          'e': 0,
          'f': 1
        },
        'g': 0,
        'h': 1
      },
      'i': 0,
      'j': 1
    },
    'value': 0
  }
  y = {
    'b': {
      'c': 2,
      'd': {
        'f': 1
      },
      'h': 1
    },
    'j': 1
  }
  z = f(**x)
  return pxyz(x, y, z)

def t_1():
  x = {
    'tree': {
      'a': 0,
      'b': {
        'c': 2,
        'd': {
          'e': 0,
          'f': 1
        },
        'g': 0,
        'h': 1
      },
      'i': 0,
      'j': 1
    },
    'value': 1
  }
  y = {
    'a': 0,
    'b': {
      'c': 2,
      'd': {
        'e': 0
      },
      'g': 0,
    },
    'i': 0
  }
  z = f(**x)
  return pxyz(x, y, z)

def t():
  if not t_0(): return pf('!t_0')
  if not t_1(): return pf('!t_1')
  return 1
