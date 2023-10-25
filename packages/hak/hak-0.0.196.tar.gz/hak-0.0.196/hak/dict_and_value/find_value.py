from hak.pxyz import f as pxyz
from hak.pf import f as pf

# remove leaves from tree where value
# f = lambda tree, value: {
#   k: (
#     f(tree[k], value)
#     if isinstance(tree[k], dict) else
#     v
#   )
#   for (k, v) in tree.items()
#   if v != value
# }

def _f(tree, value, path_so_far):
  for k in tree:
    if tree[k] == value:
      return path_so_far+[k]
    else:
      if isinstance(tree[k], dict):
        return _f(tree[k], value, path_so_far+[k])
  return None

def f(tree, value):
  return _f(tree, value, [])

def t_0():
  x = {
    'tree': {
      'a': 0,
      'b': {
        'c': 2,
        'd': {
          'e': 0.5,
          'f': 1
        },
        'g': 0,
        'h': 1
      },
      'i': 0,
      'j': 1
    },
    'value': 0.5
  }
  y = ['b', 'd', 'e']
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
    'value': 0.5
  }
  y = None
  z = f(**x)
  return pxyz(x, y, z)

def t():
  if not t_0(): return pf('!t_0')
  if not t_1(): return pf('!t_1')
  return 1
