def selection_sort(arr):
  """Selection sort"""
  for k in range(len(arr)-1):
    min_index = k # smallest
    for j in range(k+1, len(arr)):
      if arr[min_index] > arr[j]:
        min_index = j
    arr[k], arr[min_index] = arr[min_index], arr[k]
  
  return arr

arr = [1,9,2,6,4,3,0]
print("Selection sort")
print(selection_sort(arr))
