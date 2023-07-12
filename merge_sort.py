import time
import random
start=time.time()
nums=[55,56, 57,57,55,64,64,3,2,1,3]
half = len(nums) // 2
first_half = nums[:half]
second_half = nums[half:]
sorted_list=[]

print("First half:", first_half)
print("Second half:", second_half)
count=1

def split_list(list): 
    if len(list) == 1: return


    half1 = list[:len(list)//2]
    half2 = list[len(list)//2:]
    print(half1)
    print(half2)

    split_list(half1)
    split_list(half2)
 



split_list(nums) 

def split_1(array_to_split):
    crunch=len(first_half) // 2
    crunch_1= first_half[:crunch]
    crunch_2= second_half[:crunch]
    print("Crunch 1:", crunch_1)
    print("Crunch 2:", crunch_2)
    count+1
    print(" Count:", count)




print("Sorting ended..."+"\n Sorted list: "+str(sorted_list))
end=time.time()
print("Time to sort is " + str(end-start))