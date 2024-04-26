# Bubble sort program designed to demonstrate how an insertion sort works

items = [90,8,7,102,10]
swap = 0
print ("ORIGINAL LIST")
print (items)
n = len(items) # n is the number of items in the list

for x in range (n-1):
    print("MAIN LOOP PASS ",x)
    for y in range (n-1-x):
        print ("SMALL LOOP PASS ",y)
        if items[y] > items[y+1]:
            swap = 1
            temp = items[y]
            items[y] = items[y+1]
            items [y+1] = temp
        print (items)
    if swap == 0:
        break
    swap = 0

