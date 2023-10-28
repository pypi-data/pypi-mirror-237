from hak.pxyz import f as pxyz
from hak.pf import f as pf
from hak.rate import Rate

# remove leaves from tree where value
def _f(tree, value, path_so_far):
  for k in tree:
    if tree[k] == value:
      return path_so_far+[k]
    else:
      if isinstance(tree[k], dict):
        if tree[k].keys():
          return _f(tree[k], value, path_so_far+[k])
  return None

f = lambda tree, value: _f(tree, value, [])

def t_a():
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

def t_b():
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

def t_c():
  x = {
    'tree': {},
    'value': 0.5
  }
  y = None
  z = f(**x)
  return pxyz(x, y, z)

def t_d():
  x = {
    'tree': {
      'assets': {
        'cash': {
          'secondary': Rate(n=2, d=1, unit={'AUD': 1}),
          'primary': Rate(n=1, d=1, unit={'AUD': 1})
        },
        'non_cash': {
          'inventory': Rate(n=3, d=1, unit={'AUD': 1}),
          'property_and_equipment': Rate(n=4, d=1, unit={'AUD': 1}),
          'accounts_receivable': Rate(n=5, d=1, unit={'AUD': 1})
        }
      },
      'equities': {
        'contributed_capital': Rate(n=6, d=1, unit={'AUD': 1}),
        'retained_earnings': Rate(n=7, d=1, unit={'AUD': 1})
      },
        'liabilities': {'notes_payable': Rate(n=8, d=1, unit={'AUD': 1})
      }
    },
    'value': {}
  }
  y = None
  z = f(tree=x['tree'], value=x['value'])
  return pxyz(x, y, z)  

def t():
  if not t_a(): return pf('!t_a')
  if not t_b(): return pf('!t_b')
  if not t_c(): return pf('!t_c')
  if not t_d(): return pf('!t_d')
  return 1
