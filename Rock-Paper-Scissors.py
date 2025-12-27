n=int(input())
a,b=0,0
for i in range(n):
	p1=input()
	p2=input()
	if p1=="R" and p2=="P":b+=1
	elif p1=="P" and p2=="R":a+=1
	elif p1=="P" and p2=="S":b+=1
	elif p1=="S" and p2=="P":a+=1
	elif p1=="S" and p2=="R":b+=1
	elif p1=="R" and p2=="S":a+=1  
	elif p1==p2:print("Tie")  
	else:print("Invalid Input")
if(a>b):print("p1 wins")
elif(a<b):print("p2 wins")
else:print("Tie")
