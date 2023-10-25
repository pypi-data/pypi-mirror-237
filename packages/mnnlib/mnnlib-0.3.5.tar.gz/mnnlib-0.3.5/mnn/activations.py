import math

#just activation functions
#they are passed as a paramater to the layers

def relu(inp:float):
  __name__ = "relu"
  if inp < 0:
    return 0
  else:
    return inp


def sigmoid(inp:float):
  __name__ = "sigmoid"
  return 1 / (1 + math.exp(-inp))


def straight(inp:float):
  __name__ = "straight"
  return inp


def binary(inp:float):
  __name__ = "binary"
  if inp < 0.5:
    return 0
  else:
    return 1


def leakyrelu(inp:float):
  __name__ = "leakyrelu"
  if inp < 0:
    return inp * 0.01
  else:
    return inp
