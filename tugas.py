def bubblesort(data):
    for i in range(len(data)-1,0,-1):
        for j in range(i):
            if data[j] > data[j+1]:
                # tempat = data[j]
                # data[j] = data[j+1]
                # data[j+1] = tempat
                data[j], data[j+1] = data[j+1], data[j]
        print(f"pass {len(data)-i}: {data}")
        # print(data)   
        
# data = [8,5,4,1,2]   
                
data = input ("masukan angka: ")
data = list(map(int, data.split()))
bubblesort(data)
print("hasilnya")
print(data)

def binary_search(array, velue, low, high):
    if high < low:
        return -1
    else:
        mid = (low + high) // 2
        
        if velue > array[mid]: 
            return binary_search(array, velue, mid +1, high)
        elif velue < array[mid]:
            return binary_search(array, velue, low, mid -1)
        else:
            return mid
        
array = [1,2,3,4,5,6,7,8,9,90] 
print(binary_search(array, 2, 0, len(array) -1))