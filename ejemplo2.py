print("ingrese un valor limite para realizar una suma:")
n=int(input())
s= 0

for i in range(1, n+1):
    print(i)
    s=s+i

print("la suma es:", s)