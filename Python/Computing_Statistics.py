import os
import math
#Statistics is important in our field. 
#When measuring response times or rendering times. 
#It's helpful to collect data so you can easily spot abnormalities.
print("Type 'done' to finish.\n")
data = []

user_num = ""
while user_num != "done":
    user_num = input("Enter a number: ")
    try:
        data.append(int(user_num))
    except:
        TypeError
os.system("cls")

str_data = []
for n in data:
    str_data.append(str(n))
print(f"Numbers: {", ".join(str_data)}\n")

#computing average number
avg = sum(data) / (len(data))
print(f"The average is {avg :.0f}")

#computing minimum number
min_n = min(data)
print(f"The minimum is {min_n}")

#computing maximum number
max_n = max(data)
print(f"The maximum is {max_n}")

#computing standard deviation
squared_nums = []
for n in data:
    diff = n - avg
    squared_nums.append(diff * diff)
    
#Standart deviation from the average(mean) number as population
std_deviation = math.sqrt(sum(squared_nums) / len(squared_nums))
print(f"Standart population deviation is {std_deviation:.2f}")

##Standart deviation from the average(mean) number as sample
std_deviation_s = math.sqrt(sum(squared_nums) / (len(squared_nums) - 1))
print(f"Standart sample deviation is {std_deviation_s:.2f}")