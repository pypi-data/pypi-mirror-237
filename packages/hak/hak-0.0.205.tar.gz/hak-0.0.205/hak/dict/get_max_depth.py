from hak.dict.is_a import f as is_dict
from hak.pf import f as pf
from hak.pxyf import f as pxyf

f = lambda x: _f(x, 0)
_f = lambda x, q: max(
  [0] +
  [_f(x[k], q+1) if is_dict(x[k]) else q+1 for k in x]
)

def t():
  if not pxyf({},                                    0, f): return pf('!t_0')
  if not pxyf({'a': 0},                              1, f): return pf('!t_1')
  if not pxyf({'a': {'a': 0}},                       2, f): return pf('!t_2_a')
  if not pxyf({'a': {'a': 0, 'b': 0}},               2, f): return pf('!t_2_b')
  if not pxyf({'a': {'a': {'a': 0}, 'b': 0}},        3, f): return pf('!t_3')
  if not pxyf({'a': {'a': {'a': {'a': 0}}, 'b': 0}}, 4, f): return pf('!t_4')
  return 1
