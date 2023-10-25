from gearup import apply

def test_apply():
  class A(object):
    def __init__(self, x):
      self.x = x

  def f(a: A, x: int, y: int):
    return a

  assert isinstance(apply(f, '1', 2, 3), A)
  assert isinstance(apply(f, '1', 2, 3).x, str)
  assert isinstance(apply(f, A(1), 2, 3).x, int)