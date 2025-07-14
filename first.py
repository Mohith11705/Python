import numpy as np
n1=np.array([5,4,3,6])
n=np.prod(n1)
print(n)
print(n1)
n2=np.zeros([3,5],dtype='int32')
print(n2)
n3=np.arange(0,30,5)
print(n3)
# it gives linearly spaced values at interval of 8
n4=np.linspace(0,20,8)
print(n4)
# its like np.ones and np.zeros fill array full with values 
n5=np.full([2,5],99)
print(n5)
n6=np.empty(3,dtype='int32')
n6.fill(4)
print(n6)
# it shows the dimension of array
print(n6.ndim)
print(n6.shape)
print(n6.size)
# it shows how many size is wanted to store each elememt it will bytes      
print(n6.itemsize)
print(np.sort(n1))
# if you want to sort row and column give arrayname with axis=0 for column , axis =1 for row
