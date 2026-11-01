a = [12,45,66,80,70]
even = 0
odd = 0
for i in a:
    if i % 2 == 0:
         even = even+1
    else:
         odd = odd+1
print("Even Number :",even)
print("Odd Number :",odd)



b = [24,35,67,89]
for i in b:
     if i % 2 == 0:
          print("Even Number ---->",i)
     else:
          print("Odd Number ---->",i)