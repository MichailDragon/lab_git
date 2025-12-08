# Задание 1
r=int(input("введите целое число: ")) 
for r in range(1, r+1,2):
    print(r) 

    #if r%2==0:
        #print(r)
#proba
#while r>=1:
    #print(r)
    #r-=1
    
# Задание 2
#float - не только целые, но и не целые
a=float(input("ввведите a: ")) 
b=float(input("ввведите b: ")) 
if a==b:
    print('одинаковые')
else:
    print("наибольшее число:", max(a, b))