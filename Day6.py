# Decorator for div(a,b)

def mod_div(fun):
  def swap(a, b):
    if(a < b):
      a, b = b, a 
    return fun(a, b)
  
  return swap

@mod_div
def div(a, b):
  return a//b

a, b = (int(i) for i in input('Enter two numbers: ').split())
# div = mod_div(div)
print(div(a, b))