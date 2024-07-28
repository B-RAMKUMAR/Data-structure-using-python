a=[4,2,7,4,32,2]
for i in range(len(a)-1):
    j=i+1
    if(a[i]>a[j]):
         temp=a[j]
         a[j]=a[i]
         a[i]=temp
    #steps to print
    print(a)
#sorted list
print(a)
