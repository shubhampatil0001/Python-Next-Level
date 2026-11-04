marks = [78, 85, 92, 66, 89, 73]

total = 0
count = 0
maximum = marks[0]
minimum = marks[0]

for num in marks:
    
    total += num 
    count += 1
    
    if num > maximum:
        
        maximum = num
        
    if num < minimum:
        
        minimum = num
    
    average = total / count
        
print("TOTAL :", total)
print("ALL SUBJECTS: ",count)
print("MAXIMUM MARKS :",maximum)
print("MINIMUM MARKS :",minimum)            
print("AVERAGE MARKS :", average)
