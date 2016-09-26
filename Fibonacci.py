list1=[]
i=0

def fibo(n):
    if(n==0) or (n==1):
        return 1
    else:
        return list1[n-1] + list1[n-2]
        
while(i<5):
    list1.append(fibo(i))
    i+=1
