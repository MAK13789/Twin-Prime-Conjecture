def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True
count1 = 0
count2 = 0
count3 = 0
count4 = 0
for i in range(3, 1000):
    if (i < 999):
        a = isPrime(i)
        b = isPrime(i + 2)
        if (i <= 250) & (a == True) & (b == True):
            count1 = count1 + 1
        if (250 < i <= 500) & (a == True) & (b == True):
            count2 = count2 + 1
        if (500 < i <= 750) & (a == True) & (b == True):
            count3 = count3 + 1
        if (750 < i <= 998) & (a == True) & (b == True):
            count4 = count4 + 1
print ("0-250")
print (count1)
print ("250-500")
print (count2)
print ("500-750")
print (count3)
print ("750-1000")
print (count4)
            
    
    
    
