def sum_recursive(n):
    if n <= 1:
        return 1
    return n + sum_recursive(n - 1)

#print(sum_recursive(10))


def fibanacci_reccursive(n):
      if n <= 1:
           return n
      return fibanacci_reccursive(n - 1) + fibanacci_reccursive(n - 2)

#print(fibanacci_reccursive(5))

def fibanacci_by_for(n):
     a, b = 0, 1

     for index in range(n):
          a, b = b, a + b
     return (a)

print(fibanacci_by_for(5))
