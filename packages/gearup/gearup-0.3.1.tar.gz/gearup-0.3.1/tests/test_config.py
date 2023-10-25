from gearup import *

def test_kwargs():
  from gearup import gearup

  def f(**kwargs):
    print(kwargs)

  print()
  gearup(f)(['clf.alpha=1', 'clf.beta=2', 'method.beta=3'])

  def f1(alpha: float): return alpha
  def f2(beta: float, gamma: float): return beta + gamma

  def main(f, **kwargs):
    if f == 'f1':
      return apply(f1)(**kwargs.get('func', dict()))
    elif f == 'f2':
      return apply(f2)(**kwargs.get('func', dict()))
    else:
      raise NotImplementedError()

  gearup(main)(['f=f1', 'func.alpha=3'])
  gearup(main)(['f=f2', 'func.beta=5', 'func.gamma=6'])

def test_conf():
  def f1(alpha: float): return 2 * alpha
  def f2(beta: float, gamma: float): return beta + gamma

  def g1(x: float): return x + 1
  def g2(x: float, y: float): return x + y

  def main(f, g, **kwargs):
    return apply(f)(**kwargs['fargs']) * apply(g)(**kwargs['gargs'])

  assert gearup(main)(['f=f1', 'g=g2', 'fargs.alpha=2', 'gargs.x=2.0', 'gargs.y=1.5']) == 14.0
  assert gearup(main)(['f=f2', 'g=g1', 'fargs.beta=2', 'fargs.gamma=1e-1', 'gargs.x=9.0']) == 21.0

  try:
    gearup(main)(['f=f1'])
  except (ValueError, TypeError):
    import traceback
    print(traceback.format_exc())
  else:
    raise Exception()