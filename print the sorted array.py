def print Distinct(array,n)
   for i in range(0,n)
      d=0
      for i in range(0,1):
          if(arr[i]==arr[j]):
              d=1
              break
          if(d==0):
              print(arr[i])
arr=[1,2,45,89,]
n=len(arr)
printDistinct(arr,n)
