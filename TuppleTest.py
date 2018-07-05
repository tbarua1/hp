new_tuple = ('foo', 'bar', 'zoo', 'loo')
test=type(new_tuple)
print(type(str(type(new_tuple))))
print(test)
print(type(new_tuple))
test_tuple=new_tuple + ('blah', 'blah')
third_tuple=new_tuple+test_tuple
print(third_tuple)
print(test_tuple)