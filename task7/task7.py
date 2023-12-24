def chain_sum(x, *args):

  total = x
  for arg in args:
    total += arg
  return total


print(chain_sum(5)())  # 5
print(chain_sum(5)(2)())  # 7
print(chain_sum(5)(100)(-10)())  # 95


