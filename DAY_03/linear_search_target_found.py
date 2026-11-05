#Linear search is a simple search algorithm that checks every element in a list sequentially until the desired element is found or the list ends.

numbers = [12 , 34, 45, 67, 89]

target = 67

found = False  

for num in numbers:
    
    if num == target:
        
        found = True
        
        break
    
if found :
        print("Target found in the list")
        
else:
        print("Target not found in the list")   
        

#numbers in linear search 
numbers = [10 ,20 , 30 , 40 , 50 ]

target = 100

found = False

for num in numbers:
    
    if num == target:
        
        found = True
        
        break
    
if found:
    print("Element found !")
    
else:
    print("Element is not found")    
    
   
   # 3 Marks in linear search
   
marks = [78, 85, 92, 66, 89, 73]

target = 92

found = False

for num in marks:
    
    if num == target:
        
        found = True 
        break
    
if found:
    print("Marks found in the list")
else:
    print("Marks not found in the list")                
