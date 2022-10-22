# code adapted from prof. A O
import numpy as np

def l1grad(y, a):
  # this returns the gradient of |x-a| evaluated at y
  if y > a:
      return 1
  if y < a:
      return -1
  if y == a:
      return 0

def l1gradvec(y, a):
  toreturn = np.zeros(len(a))
  for i in range(len(a)):
    toreturn[i] = l1grad(y[i], a[i])
  return toreturn
