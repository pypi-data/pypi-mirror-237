from hak.pf import f as pf
from hak.pxyz import f as pxyz
from hak.rate import Rate
from hak.strings.compare import f as compare_strings

_f = lambda x, i=0: '{\n'+',\n'.join([
  (
    ' '*(i+2)+f"'{k}': {_f(x[k], i+2)}"
    if isinstance(x[k], dict) else
    ' '*(i+2)+f"'{k}': {repr(x[k])}"
  )
  for k
  in sorted(x.keys())
])+'\n'+' '*i+'}'

f = lambda x: _f(x, 0).replace('{\n\n}', '{}')

def t_a():
  x = {
    'assets': {
      'cash': {
        'primary': Rate(n=0, d=1, unit={'AUD': 1}),
        'secondary': Rate(n=0, d=1, unit={'AUD': 1})
      },
      'non_cash': {
        'accounts_receivable': Rate(n=0, d=1, unit={'AUD': 1}),
        'inventory': Rate(n=0, d=1, unit={'AUD': 1}),
        'property_and_equipment': Rate(n=0, d=1, unit={'AUD': 1})
      }
    },
    'equities': {
      'contributed_capital': Rate(n=0, d=1, unit={'AUD': 1}),
      'retained_earnings': Rate(n=0, d=1, unit={'AUD': 1})
    },
    'liabilities': {'notes_payable': Rate(n=0, d=1, unit={'AUD': 1})}
  }
  y = "\n".join([
    "{",
    "  'assets': {",
    "    'cash': {",
    "      'primary': Rate(n=0, d=1, unit={'AUD': 1}),",
    "      'secondary': Rate(n=0, d=1, unit={'AUD': 1})",
    "    },",
    "    'non_cash': {",
    "      'accounts_receivable': Rate(n=0, d=1, unit={'AUD': 1}),",
    "      'inventory': Rate(n=0, d=1, unit={'AUD': 1}),",
    "      'property_and_equipment': Rate(n=0, d=1, unit={'AUD': 1})",
    "    }",
    "  },",
    "  'equities': {",
    "    'contributed_capital': Rate(n=0, d=1, unit={'AUD': 1}),",
    "    'retained_earnings': Rate(n=0, d=1, unit={'AUD': 1})",
    "  },",
    "  'liabilities': {",
    "    'notes_payable': Rate(n=0, d=1, unit={'AUD': 1})",
    "  }",
    "}",
  ])
  z = f(x)
  if y != z:
    comparison = compare_strings(y, z)
    print(comparison)
    q = comparison['first_difference']
    w = 20
    print([y[q-w:q+w]])
    print([z[q-w:q+w]])
  return pxyz(x, y, z)

def t_b():
  x = {}
  y = '{}'
  z = f(x)
  if y != z:
    comparison = compare_strings(y, z)
    print(comparison)
    q = comparison['first_difference']
    w = 20
    print([y[q-w:q+w]])
    print([z[q-w:q+w]])
  return pxyz(x, y, z)

def t():
  if not t_a(): return pf('!t_a')
  if not t_b(): return pf('!t_b')
  return 1
