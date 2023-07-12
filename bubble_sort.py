import time
import random
start=time.time()
sorted_list=[]
nums_to_sort=[55,56, 57,57,55,64,64,3,2,1,3]
count=0
for i t:
    smallest_num=nums_to_sort[count]
    count+1
    print("Sorting beginning...")
    nums_to_sort[count]<nums_to_sort[count+1]
    smallest_num=nums_to_sort[count+1]
    sorted_list.append(smallest_num)
    
print("Sorting end..."+"\n Sorted list: "+sorted_list)
end=time.time()
print("Time to sort is " + str(end-start))