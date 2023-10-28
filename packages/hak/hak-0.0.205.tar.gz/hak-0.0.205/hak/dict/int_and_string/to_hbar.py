from hak.pxyf import f as pxyf

# hbar with centred text
def f(x):
  _w = x['w'] - 2
  _x = '+'+x['string'].replace(' ', '+')+'+'
  return f'{_x:^{_w}}'.replace(' ', '-').replace('+', ' ')

t = lambda: pxyf({'w': 30, 'string': 'foo'}, '----------- foo ------------', f)
