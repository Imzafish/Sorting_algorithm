import random
import time
start=time.time()
nums=[55,56, 57,57,55,64,64,3,2,1,3]
print ("Sorting Nums...")
for a in range(len(nums)):
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            temp = nums[i]
            nums[i] = nums[i+1]
            nums[i+1] = temp
print("Sorting ended..."+"\n Sorted list: "+str(nums))
end=time.time()
print("Time to sort is " + str(end-start))