# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
a=[4,8,2,6,7,4,32,2]
for i in range(1,len(a)):
    key=a[i]
    j=i-1
    while j>=0 and key<a[j]:
        a[j+1]=a[j]
        j-=1
    a[j+1]=key
    print(a)
print(a)
         
