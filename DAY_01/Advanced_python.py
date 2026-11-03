#Addition of condition elements

numbers = [10 , 20 , 30 , 40 , 50 ]

total = 0

for num in numbers :
    
    if num > 25 :
        
        total += num
        
print("TOTAL SUM: ",total)        



# Addition of all list elements 

numbers = [ 10 , 30 , 39, 34, 39, 100]

total = 0

for num in numbers :
    
    total = total + num 
    
print("TOTAL : ", total)


# Addition of even numbers in list
numbers = [ 2 , 5 , 8 , 11 , 14 , 17]

total = 0 

for num in numbers :
    
    if num %2 == 0 :
        
        total += num 
        
print("TOTAL ADD EVEN NO :" ,total)        



# Counting positive numbers in list

numbers = [ -3, 5 , 0 , 8 , -1 , 4 ,]

count = 0
      
for num in numbers :
    
    if num > 0 :
        
        count +=1
        
print("TOTAL POSITIVE NO : ", count)


# largest number using list

numbers = [ 10 , 20 , 30 , 40 , 50 , 89]

largest = numbers[0]

for num in numbers :
    
    if num > largest :
        
        largest = num 
        
print("LARGEST NUMBER :",largest) 
