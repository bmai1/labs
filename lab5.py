# Lab5A Sum 
def s(a, b):
  if a + b >= 40 and a + b <= 49:
    return 50
  else:
    return a + b

# Lab5B Sum/Diff == 7
def check(x, y):
  if x == 7 or y == 7 or x + y == 7 or abs(x - y) == 7:
    return True
  return False

# Lab5C Threesome
def threesum(a, b, c):
  if a == b and a == c:
    return 0
  if a == b:
    return c
  if a == c:
    return b
  if b == c:
    return a
  return a + b + c

# Lab5D Fraction addition
# recursion naive solution to find gcd
def g(b, d):
  if (d == 0):
    return abs(b)
  else:
    return g(d, b % d)

def add_fraction(a, b, c, d):
  # if denominator(s) equal zero
  if b == 0 and d == 0:
    return '0'
  elif b == 0: 
    return ' '.join((str(c), '/', str(d)))
  elif d == 0:
    return ' '.join((str(a), '/', str(b)))
  else:
    numerator = a * d + b * c
    denominator = b * d
    gcd = g(numerator, denominator)
    # reduce fraction using gcd and 3 in case gcd is even
    while (numerator % gcd == 0 and denominator % gcd == 0):
      if gcd == 1:
        break
      numerator /= gcd
      denominator /= gcd
    
    # if divide by 1
    if denominator == 1:
      return int(numerator)
    
    # simplify improper fractions
    if numerator > denominator:
      return ''.join((str(int(numerator / denominator)), ' ', str(int(numerator % denominator)), '/', str(int(denominator))))

    return ' '.join((str(int(numerator)), '/', str(int(denominator)))) 
