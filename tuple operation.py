tuplex = ("tuple", False, 3.2, )
print(tuplex)
tuplex = (4,6,2,8,3,1)
print(tuplex)
#tuples ar immutable, so you can not add new elements
#using merg of tuples with the +operator you can add an element and it will create a tuple
tuplex = tuplex + (9,)
print(tuplex)


#counts the number of occurences of item 50 from a tulple
tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(50))

#create a tuple
tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1,)
_slice = tuplex[3:5]
print(_slice)
_slice = tuplex[:6]
print(_slice)