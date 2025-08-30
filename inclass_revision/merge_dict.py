d1 ={1:"A",2:"B"}
d2 ={3:"C", 4:"D"}

def mergedic(d1,d2):
    d1.update(d2)
    return d1
print(mergedic(d1,d2))