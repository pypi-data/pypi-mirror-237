class FakePrinter:
  def __init__(self):
    self.history = []
  __call__ = lambda self, x: self.history.append(x)
  def reset(self): self.history = []

f = lambda: FakePrinter()

def t():
  fp = f()
  if fp.history != []: return 0
  
  fp('boo')
  if fp.history != ['boo']: return 0
  
  fp('bang')
  if fp.history != ['boo', 'bang']: return 0
  
  fp.reset()
  if fp.history != []: return 0

  return 1
