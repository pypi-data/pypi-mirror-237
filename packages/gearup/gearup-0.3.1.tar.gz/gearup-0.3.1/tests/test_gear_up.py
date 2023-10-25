from gearup import *

def test_gear_up():
  def f(x : int, y : int):
    return x + y

  def g1(w : int, y : int):
    return w + y

  def g2(t : int, y : int):
    return t + y

  assert gearup(
    train=f,
    test=dict(
      x1=g1,
      x2=g2
    )
  )(['test', 'x1', 'w=2', 'y=4']) == 6

def test_choice():
  def f(x: int):
    return x

  def f2(x: int):
    return x

  def f3(x: int):
    return x + 1

  def main(method: choice(f, g=f2, h=f3), x: int):
    return method(x)

  gearup(main)(['f', '1'])
  gearup(main)(['g', '1'])
  gearup(main)(['h', '1'])

  try:
    gearup(main)(['f1', '1'])
  except (TypeError, ValueError):
    pass
  except:
    raise

  try:
    gearup(main)(['f2', '1'])
  except (TypeError, ValueError):
    pass
  except:
    raise

def test_member():
  class A:
    class B:
      @staticmethod
      def f(x: int):
        return x

      @staticmethod
      def g(x: int):
        return x + 1

    @staticmethod
    def h(x: int):
      return x + 2

  def main(method: member[A], x: int):
    return method(x)

  assert gearup(main)(['B.f', '1']) == 1
  assert gearup(main)(['B.g', '1']) == 2
  assert gearup(main)(['h', '1']) == 3

  try:
    gearup(main)(['f1', '1'])
  except (TypeError, ValueError):
    pass
  except:
    raise

  try:
    gearup(main)(['f2', '1'])
  except (TypeError, ValueError):
    pass
  except:
    raise

def test_apply():
  def g1(x, y, z: float):
    return x + y + z

  def g2(x, y, h: float, jj: str):
    return (x + y) / h + len(jj)

  def main(f: choice(g1, g2), x: int, y: float, **kwargs):
    return apply(f, x, y, **kwargs)

  result = gearup(main)(['g1', 'x=1', 'y=2.0', 'z=1e-1'])
  assert result == 3.1

  result = gearup(main)(['g2', 'x=1', 'y=2', 'jj=1e-1', 'h=10'])
  assert result == 4.3

  try:
    gearup(main)(['g2', 'x=1', 'y=2', 'z=1e-1'])
  except (ValueError, TypeError) as e:
    pass
  except:
    raise

def test_kwargs():
  def f1(x):
    return x + 1

  def f2(x, flag: bool=False):
    return x if flag else -x

  def g1(x, alpha: float):
    return alpha * x

  def g2(x, beta: float):
    return x / beta

  def main(f: choice(f1, f2), g: choice(g1, g2), x: float, **kwargs):
    y = apply(g, x, **kwargs.get('gconfig', dict()))
    return apply(f, y, **kwargs.get('fconfig', dict()))

  result = gearup(main)(['f=f1', 'g=g2', 'x=1', 'gconfig.beta=2.0'])
  assert result == 1.5

  result = gearup(main)(['f=f1', 'g=g1', 'x=1', 'gconfig.alpha=2.0'])
  assert result == 3.0

  result = gearup(main)(['f=f2', 'g=g1', 'x=1', 'gconfig.alpha=2.0'])
  assert result == -2.0

  result = gearup(main)(['f=f2', 'g=g1', 'x=1', 'fconfig.flag=True', 'gconfig.alpha=3.0'])
  assert result == 3.0

  try:
    gearup(main)(['f=f1', 'g=g1', 'x=1', 'gconfig.flag=True'])
  except (ValueError, TypeError) as e:
    pass
  except:
    raise

def test_number():
  def check(interval, x, y, z):
    print(interval)

    if x is not None:
      try:
        interval(str(x))
      except (TypeError, ValueError) as e:
        pass
      except:
        raise

    if y is not None:
      assert interval(str(y)) == y

    if z is not None:
      try:
        interval(str(z))
      except (TypeError, ValueError) as e:
        pass
      except:
        raise


  print()
  check(1 < number, 1, 5, None)
  check(1 <= number, 0, 5, None)
  check(number < 10, None, 5, 10)
  check(number <= 10, None, 5, 11)
  check((1 <= number) & (number <= 10), 0, 5, 11)
  check((1 <= number) & (number < 10), 0, 5, 10)
  check((1 < number) & (number <= 10), 1, 5, 11)
  check((1 < number) & (number < 10), 1, 5, 10)

  print()
  check(interval[1:10], 0, 5, 10)
  check((1 < number) < 10, 1, 5, 10)