# for tuple use (), tuple se foloseste la transmiterea datelor pentru economisirea memoriei

# data = ( 5, 7, 3, 3, 6, True, 6.2, "Hey")
# data[0] = 5 - no
# print(data[3:6:2])
# print(len(data))
# print(data)


data = (5, 4, 6, 3, 3, 5, True)

for el in data:
    print(el)
# list - lista compusa din mai multe simboluri
# transformam list in tuple
nums = [3, 5, 2]
newItem = tuple(nums)

print(nums)

word = tuple("Hello world")
print(word)