def shift_array(shift, n):
    for i in range(len(shift)):
        if shift[i] > n:
            break
    shift = shift[:i] + [n] + shift[i:]
    return shift


if __name__ == "__main__":  
  print(shift_array([2,4,6,8], 5))            
  print(shift_array([4,8,15,23,42], 16))        
  print(shift_array([0,1,3,23,42], 0))        
  print(shift_array([-10,0,1,3,23,42], -5))        
    