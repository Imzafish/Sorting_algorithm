import time
import random

nums=[55,56, 57,57,55,64,64,3,2,1,3]
half = len(nums) // 2
first_half = nums[:half]
second_half = nums[half:]

print("First half:", first_half)
print("Second half:", second_half)
crunch=len(first_half) // 2
crunch_1= first_half[:crunch]
crunch_2= second_half[:crunch]
print("Crunch 1:", crunch_1)
print("Crunch 2:", crunch_2)


