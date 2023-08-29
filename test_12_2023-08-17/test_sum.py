
def sum_recursive1(n):
  if n <= 1:
    return 1
  return n + sum_recursive1(n - 1)

print(sum_recursive1(10))

def test_sum_recursive1():
  result = sum_recursive1(10)
  assert(result) == 55, 'Incorrect'

