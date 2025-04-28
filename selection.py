def selectionsort(arr):
    for i in range(len(arr)):
        min=i
        for j in range(i+1,len(arr)):
            if arr[min]>arr[j]:
                min=j
        arr[min],arr[i]=arr[i],arr[min]
    return arr
print(selectionsort([1,4,2,6,3,9]))
            