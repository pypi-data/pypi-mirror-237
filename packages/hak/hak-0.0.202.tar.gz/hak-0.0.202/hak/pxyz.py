from hak.pf import f as pf
from hak.fake.printer import f as FP
from hak.strings.compare import f as compare_strings

def f(x, y, z, p=print, new_line=False):
  q = '\n' if new_line else ' '
  if y != z:
    comparison = compare_strings(str(y), str(z))
    j = comparison['first_difference']
    w = 20
  return y == z or pf(
    [
      f'x:{q}{x}',
      f'y:{q}{y}',
      f'z:{q}{z}',

      'first difference:',
      str(y)[j-w:j+w],
      str(z)[j-w:j+w],
    ],
    p
  )

def t_true():
  _fake_printer = FP()
  x = {'x': 1, 'y': 1, 'z': 1}
  return all([f(**x, p=_fake_printer), _fake_printer.history == []])

def t_false():
  _fake_printer = FP()
  x = {'x': 1, 'y': 1, 'z': 2}
  return all([
    not f(**x, p=_fake_printer),
    _fake_printer.history == ['x: 1\ny: 1\nz: 2\nfirst difference:\n1\n2']
  ])

def t():
  # TODO: Insufficient test coverage: Skipped additional test for new line code
  if not t_true(): return pf('!t_true')
  if not t_false(): return pf('!t_false')
  return 1
