import time
import random
running=True
smallest_num=1
nums_to_sort=[12,24,6,8,9,64738,64,3,2,2,1]

count=(nums_to_sort.length)
for i in range(nums_to_sort.length):
    print("FILLER")



print(nums_to_sort)

def sort(sort_function):
    for i in range(1):
        print(nums_to_sort)
        nums_to_sort[1]=smallest_num
        count=2
      
    if nums_to_sort [count]< smallest_num:
        print ("New Smallest Number is "+str(smallest_num))
        smallest_num= nums_to_sort [2]
        count+1
        
sorted_nums=[]