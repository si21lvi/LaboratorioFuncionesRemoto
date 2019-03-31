def is_prime (n):
  cont=0
  for i in range (1, n+1):
    if n%i==0:
      cont+=1
  if cont<=2:
    print("Is a prime number")
  else:
    print("Is NOT a prime number")
n=int(input("Digite el número"))
is_prime (n)