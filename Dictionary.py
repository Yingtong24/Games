#defining dictionary
d1={"dog": "beige", "cat": "orange", "duck": "yellow"}
print(d1)
print(type(d1))
print(len(d1))
print(d1["cat"])
print(d1["duck"])
#add element
d1["chicken"]=3
d1["pig"]=4
print(d1)
d1["cat"]="grey"
print(d1)
d1["pig"]="pink"
print(d1)
#deleting
del(d1["dog"])
print(d1)
#printing all keys
print(d1.keys())
#printing all values
print(d1.values())