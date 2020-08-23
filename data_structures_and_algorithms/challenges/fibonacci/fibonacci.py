def fibonacci(n):
  if n <= 0:
      return 0
  if n == 1:
    return n
  return fibonacci(n - 1) + fibonacci(n- 2)

def fibonacci_in_loop(n):
    f = []
    for i in range(n + 1):
        if i == 0:
            f.append(i)
        elif i == 1:
            f.append(i)
        else:
            f.append(f[-1] + f[-2])
    return f[-1]

def sum_list_values(list):
    list1 = []
    for i in range(len(list)):
        sum = 0
        for j in range(len(list1)):
            sum += 1
        list1.append(sum)
    return list1    
print(sum_list_values([ [1, 2, 3], [3, 5, 7], [1, 7, 10] ]))