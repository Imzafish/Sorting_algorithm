import time
import random

nums=[55,56, 57,57,55,64,64,3,2,1,3]
half = len(nums) // 2
first_half = nums[:half]
second_half = nums[half:]
print("First half:", first_half)
print("Second half:", second_half)

def split_1():
    crunch=len(first_half) // 2
    crunch_1= first_half[:crunch]
    crunch_2= second_half[:crunch]
    print("First Half:", crunch_1)
    print("Second Half:", crunch_2)
    
def split_2():
    crunchy=len(second_half) // 2
    crunch_A= first_half[:crunchy]
    crunch_B= second_half[:crunchy]
    print("Crunchy 1:", crunch_A)
    print("Crunchy 2:", crunch_B)


