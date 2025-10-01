import numpy as np

my_list=[1,2,3,4]
print(my_list)

my_list=my_list*2
print(my_list)

array=np.array([1,2,3,4,5])
print(array)
print(type(array))

array=array*2
print(array)


array=np.array([[['A','B','C'],['D','E',"F"]],
                [['A','B','C'],['D','E',"F"]]])
print(array.ndim)
print(array.shape)

print(array[0][0][0])

print(array[1,1,0])

word=array[0,0,0]+array[1,1,0]+array[1,1,1]
print("word",word)

array= np.array([[1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12],
                 [13,14,15,16]])

print(array[0:4:3])
print(array[::-1])

#select columns
print("select columns",array[:,1])

print(array[:,1:3:2])
print(array[:,::3])
print(array[:,::-2])

print(array[0:2,0:2])
print(array[2:4,2:4])

#Scalar arithmetic
array=np.array([1,2,3,4])
print("Scaler",array + 1)
print(array - 2)
print(array * 3)
print(array / 4)
print("Scaler",array ** 4)

#Vectorized math funcs
array=np.array([1.1,2.5,3.7])
print(np.sqrt(array))
print(np.round(array))
print(np.ceil(array))

radii=np.array([1,2,3])
print(np.pi * radii **2)

array1=np.array([1,2,3])
array2=np.array([4,5,6])
print(array1+array2)

scores=np.array([91,55,100,73,82,64])
print(scores==100)
print(scores>=60)
print(scores<=60)

scores[scores<60]=0
print("scores",scores)

#Broadcasting

array1=np.array([[1,2,3,4]])
array2=np.array([[1],[2],[3],[4]])
print(array1.shape)
print(array2.shape)

print(array1 * array2 )

array=np.array([[1,2,3,4,5],
                [6,7,8,9,10]])
print(np.std(array))
print(np.var(array))
print(np.sum(array))
print(np.mean(array))
print(np.min(array))
print(np.max(array))
print(np.argmin(array))
print(np.argmax(array))

print(np.sum(array,axis=0))

#filtering






































