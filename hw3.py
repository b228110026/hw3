def QuickSort(array, start, end):
 if (len(array) == 1):
  return
 if (start > end):
  return
 pivot = start
 left = start
 right = end
 while (left != right):
  while(array[right] >= array[pivot] and left != right):
    right = right - 1
  while(array[left] <= array[pivot] and left != right):
    left = left + 1
  
  tmp = array[left]
  array[left] = array[right]
  array[right] = tmp

  
 tmp = array[pivot]
 array[pivot] = array[right]
 array[right] = tmp
 print(array)
 pivot = right

 if(pivot > 0):
  QuickSort(array, start, pivot - 1)
 if(pivot < len(array)-1):
  QuickSort(array, pivot + 1, end)

array = [33,67,8,13,54,119,3,84,25,41]
print('原始陣列:')
print(array)
print('流程:')
QuickSort(array, 0, len(array)-1)
print('結果:')
print(array)