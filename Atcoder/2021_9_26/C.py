n=int(input())#3
a=list(map(int,input().split()))#3 5 2
x=int(input())#26
s=sum(a)#10
res=(x//s)*n#6
t=(x//s)*s#20
i=0
while t<=x:
	t+=a[i]
	res+=1
	i+=1
print(res)






