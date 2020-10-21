myList = ['apple', 4, 'mango', 66.6, 'pear']
print("original list:", myList)
myList.insert(2, 'apple')
print("inserted apple in list:", myList)
myList.reverse()
print("reversed list:", myList)
x = myList.count('apple')
print("how many times is apple in my list? ", x, "times")