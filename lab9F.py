def rotate(list):
  # list[:] = list[-1:] + list[:-1]
  for i, n in enumerate(list):
    if len(list) == 1:
      return list
      
    if i != 0:
      tmp = list[i]
      tmp2 = list[i - 1]
      list[i - 1] = tmp
      list[i] = tmp2
  return list
