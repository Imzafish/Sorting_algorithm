import time
import random
start=time.time()
sorted_list=[]
nums_to_sort=[55,56, 57,57,55,64,64,3,2,1,3]
count=0
print("Sorting beginning...")
nums_to_sort_length=len(nums_to_sort)
for i in range(nums_to_sort_length):                           
    if nums_to_sort[i-1]<nums_to_sort[i]:
        smallest_num=nums_to_sort[i]
        sorted_list.append(smallest_num)       
    

print("Sorting ended..."+"\n Sorted list: "+str(sorted_list))
end=time.time()
print("Time to sort is " + str(end-start))