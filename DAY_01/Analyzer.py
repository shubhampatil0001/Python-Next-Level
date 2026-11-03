numbers = [1, -1, 30, 40, 23, 12, -4, 5, 67]

total_sum = 0 
even_count = 0
odd_count = 0
positive_count = 0

if len(numbers) > 0:
    max_num = numbers[0]
else:
    max_num = None

for num in numbers:
    
   
    total_sum += num 
    
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
        
    if num > max_num:
        max_num = num
        
    if num > 0:
        positive_count += 1    

print("___RESULTS___")
print("TOTAL SUM : ", total_sum)
print("TOTAL EVEN COUNT : ", even_count)
print("TOTAL ODD COUNT : ", odd_count)
print("TOTAL POSITIVE COUNT : ", positive_count)
print("LARGEST NUMBER : ", max_num)
