def is_triangle(side1,side2,side3):
  if side1==0 or side2==0 or side3==0:
    return ValueError("not a triangle")
  elif side1+side2>=side3 and side2+side3>=side1 and side1+side3>=side2:
    return True
  elif side1<0 or side2<0 or side3<0:
    raise ValueError("not a triangle")
#print(is_triangle(float(input()),float(input()),float(input())))
def is_equilateral(side1,side2,side3):
  if side1==0 and side2==0 and side3==0:
    return False
  if is_triangle(side1,side2,side3) and side1==side2==side3:
    return True
  return False
#print(is_equilateral(float(input()),float(input()),float(input())))
def is_isosceles(side1,side2,side3):
  if side1==0 and side2==0 and side3==0:
    return False
  if is_triangle(side1,side2,side3) and ((side1==side2)or (side2==side3) or (side1==side3)):
    return True
  return False
#print(is_isosceles(float(input()),float(input()),float(input())))
def is_scalene(side1,side2,side3):
  if is_triangle(side1,side2,side3) and not is_equilateral(side1,side2,side3) and not is_isosceles(side1,side2,side3):
    return True
  return False
#print(is_scalene(float(input()),float(input()),float(input())))
def is_degenerate(side1,side2,side3):
  if side1==0 and side2==0 and side3==0:
    return False
  if is_triangle(side1,side2,side3) and (side1+side2==side3 or side2+side3==side1 or side1+side3==side2):
    return True
  return False
print(is_degenerate(int(input()),int(input()),int(input())))
