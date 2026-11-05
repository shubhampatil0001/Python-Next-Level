marks = [78, 85, 92, 66, 89, 73]

num = int(input("Enter the marks to search: "))

target = num 

found = False

for num in marks:
    
    if num == target:
        
        found = True 
        break
    
if found:
    print("Marks found in the list")
else:
    print("Marks not found in the list")    
