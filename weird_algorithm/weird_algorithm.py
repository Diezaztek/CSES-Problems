# -*- coding: utf-8 -*-
n = int(input())
final_result = f"{n}"

while n != 1:
    if n%2 == 0:
        n = int(n/2)
    else:
        n = (n*3) + 1
    
    final_result += f' {n}'
    
print(final_result)
    
