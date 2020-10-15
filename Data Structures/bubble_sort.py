def bubble_sort(arr):
  """Bubble sort"""
  n = len(arr) 
  for k in range(n-1):
    for j in range(n-k-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j] 
  
  return arr

arr = [1,9,2,6,4,3,0]
print("Bubble sort")
print(bubble_sort(arr))
