# Insertion sort program designed to demonstrate how an insertion sort works

items = [90,8,75,4,2]
print ("ORIGINAL LIST")
print (items)
n = len(items) # n is the number of items in the list

print ("ITEM 0 HAS NO ITEMS TO THE LEFT")
print ("SO WE START WITH ITEM 1")
for x in range (1,n):
    print ("CHECKING ITEM ",x)
    item = items[x]
    y = x-1
    while y>=0 and item <items[y]:
        items[y+1] = items[y]
        y = y-1
        print("SHIFT",items)
    items [y+1] = item
    print ("ITEM INSERTED AT CORRECT POSITION")
    print (items)
