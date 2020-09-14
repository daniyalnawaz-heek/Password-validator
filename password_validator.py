#Password validator

#Taking input 
input=input("enter your password")

#intitilizing the counter to zero       
l,u,d,s=0,0,0,0   

#runing loop to check uppercase letter, lowercase letter, digit and symbol for validation
if len(input)>=8:
  for x in input:
    if x.isupper():
      u+=1
    if x.islower():
      l+=1
    if x.isdigit():
      d+=1
    if x=='@'or x=='!' or x=='$' or x=='*':
      s+=1
    if x== '%' or x=='^'or x=='&'or x=='#':
      pass

#checking for counters, if zero then not valid otherwise valid
if l==0 or u==0 or d==0 or s==0 :

#if valid
  print("password invalid")
  #if not valid
else:
  print("password valid")

    



























