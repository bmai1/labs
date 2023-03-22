def s_p(list):
  product = 1
  for i, n in enumerate(list):
    product *= n
    if n == 99:
      product /= 99
      if i != 0:
        product /= list[i - 1]
      if i != len(list) - 1:
        product /= list[i + 1]
  return product

print(int(s_p([15, 2, 99])))
print(int(s_p([99, 1, 2, 3])))
print(int(s_p([24, 99, 7, 2, 6, 15, 99])))
  