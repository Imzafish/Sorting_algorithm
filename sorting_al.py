import time
import random
nums_to_sort=[12,24,6,8,9,64738,64,3,2,2,1]
count=0
print(nums_to_sort)
smallest_num=1
def sort(sort_function):
    if nums_to_sort<0:
        print(nums_to_sort)
        nums_to_sort[1]=smallest_num
        
    if nums_to_sort [2]< smallest_num:
        print ("New Smallest Number is "+str(smallest_num))
        smallest_num= nums_to_sort [2]
        count+1
sorted_nums=[]