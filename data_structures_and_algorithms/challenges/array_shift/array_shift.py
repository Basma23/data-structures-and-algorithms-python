# def shift_array(shift, n):
#     for i in range(len(shift)):
#         if shift[i] > n:
#             break
#         shift = shift[:i] + [n] + shift[i:]
#         return shift
def shift_array(shift, n):
  shifted = []
  i = 0
  for i in range(len(shift)):
  
    if shift[i] < n and shift[i+1] > n:
      shifted.append(shift[i]) 
      shifted.append(n)
    else:
      shifted.append(shift[i])  
    i += 1
  return shifted
print(shift_array([2,4,6,8], 5))            
print(shift_array([4,8,15,23,42], 16))        
    