def bubblesort(data):
    for i in range(len(data)-1,-1,-1):
        for j in range(i):
            if data[j] > data[j+1]:
                tempat = data[j]
                data[j] = data[j+1]
                data[j+1] = tempat
        print(data)          
                
data = [2,1,4,7,3]
bubblesort(data)
print("******")
print(data)