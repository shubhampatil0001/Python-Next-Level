# Findind Maximum
numbers = [ 15 , 25 , 35 , 45 , 55] 

maximum = numbers[0]
for num in numbers :
    
    if num > maximum :
        maximum = num
        
print("MAXIMUM :", maximum)


# Finding Minimum
numbers = [ 15 , 25 , 35 , 45 , 55]

minimum = numbers[0]

for num in numbers:
    
    if num < minimum :
        
        minimum = num 
        
print("MINIMUM :", minimum)        


# Finding Both
numbers = [-10, -5, -25, -2, -18]

maximum = numbers [0]
minimum = numbers [0]

for num in numbers :
    
    if num > maximum :
        
        maximum = num 
        
    if num < minimum :
        
        minimum = num 
        
print('MAXIMUM :', maximum )
print("MINIMUM :", minimum)            
