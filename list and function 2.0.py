# nums = [1, 3, 5, True, "20"]
#
# for el in nums:
#     el *= 2
#     print(el)

# program
n = int(input("Enter length: "))

userList = []

i = 0
while i < n:
    string = "Enter element #" + str(i + 1) + "; "
    userList.append(input(string))
    i += 1

    print(userList)
