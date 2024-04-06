'''n=int(input("Enter no:"))
sum=0
i=1
while i<=n:
    sum=sum+i
    
    i=i+1
print("the sum is ",sum)'''
'''
n=int(input("Enter no :"))
i=1
print("Print noi upto",n)
while i<=n:
    print(i)
    i=i+1
'''
'''
n=int(input("Enyter no :"))
i=1
print("Printing even no upto",n)
while i<=n:
    if i%2==0:
        print(i)
    i=i+1
    '''

#create table
number=int(input("Enter the number:"))
count=1
print("The Multiplication Table of:",number)
while count<=10:
   # number=number*1
    print(number,'x',count,'=',number*count)
    count+=1