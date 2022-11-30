# data = set('hello')
data = {5, 3, 6, 7, 5}

data.add(32)
data.update(['21', True, 4, 6])
data.remove(True)
data.pop()
# data.clear()
nums = [5, 3, 6, 7, 5, 4]
newNums = set(nums)

print(data)

# frozenset

newData = frozenset([3, 5, 6, 3, 3, 5, 5, 4, 4, 6, 6])
# newData.add(4) or add([3]) nu functioneaza
print(newData)
