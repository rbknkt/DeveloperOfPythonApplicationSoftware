numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
len_array = len(numbers)
summary = 0
for i in range(0, len_array):
    if (numbers[i] != None):
        summary =  summary + numbers[i]
    if (numbers[i] == None):
        temp = i
numbers[temp]= summary/len_array
print("Измененный список:", numbers)
