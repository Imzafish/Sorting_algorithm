import time
import random
start=time.time()
sorted_list=[]
nums_to_sort=[55,56, 57,57,55,64,64,3,2,1,3]


while nums_to_sort:
    smallest = nums_to_sort[0]
    pos = 0
    for i in range(len(nums_to_sort)):
        if nums_to_sort[i]<smallest:
            smallest=nums_to_sort[i]
            pos=i
            
    del nums_to_sort [pos]
    sorted_list.append(smallest)
print(sorted_list)
time.sleep(1)

end=time.time()
print("Time to sort is " + str(end-start))
