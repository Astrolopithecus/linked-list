from linkedlist import LinkedList

checkAll = True
def checkValue(actual, expected):
    if (checkAll):
        assert(actual == expected)

def confirmValueFoundAt(lyst, value, index ):
    ''' FUnction to confirm that value is found at given index in the lyst'''
    indexActual = lyst.index(value)
    print(f"{value} found at index: {indexActual}")
    checkValue(indexActual, index)
    

def confirmValueAfterPop(lyst, value, index):
    '''Function to confirm value is returned when pop(index) is called on lyst'''
    popValue = lyst.pop(index) 
    print(f"pop({index}) returned {popValue}")
    checkValue(popValue, value)
    

def main():
    myList =LinkedList()
    print("Empty linked list:" + str(myList))
    

    numbers = [54,26,93,17,77,31]
    # Build a linked list with these numbers
    for i in range (len(numbers)):
        myList.add(numbers[i])

    length = myList.size()
    checkValue(length, 6)
    print(f"Initial linkedlist setup with {myList.size()} elements: " + str(myList))
    print()    
    
##    confirmValueFoundAt(myList, 54, 0)
##    confirmValueFoundAt(myList, 31, 5)
##    confirmValueFoundAt(myList, 93, 2)
##
##    index100 = myList.index(100)
##    print(f"Trying index(100) ...{index100}")
##    checkValue(index100, -1)
##    print()
##    
##
##    print(f"Inserting 100 at index 2")
##    myList.insert(2, 100)
##    confirmValueFoundAt(myList, 100,2)
##
##    print("Inserting 101 at index 0") 
##    myList.insert(0,101)
##    confirmValueFoundAt(myList, 101,0)
##
##    try:
##        print("Trying inserting 103 at index -1")
##        myList.insert(-1,103)
##    except Exception as e:
##        print("Error: " + str(e))
##    
##
##    listsize = myList.size()     
##    print(f"Inserting 99 at index {listsize-1}") 
##    myList.insert(listsize-1,99)
##    confirmValueFoundAt(myList, 99,listsize-1)
##
##    print("linkedlist after multiple insertions.." + str(myList))
##    print()
##    
##
##    print("Removing 101...")
##    myList.remove(101)
##    listsize = myList.size()
##    print(f"Current size of the list: {listsize}")
##    checkValue(listsize,8 )
##    
##
##    try:
##        print("Removing 101 again...")
##        myList.remove(101)
##    except Exception as e:
##        print("Error: " + str(e))
##    
##    
##
##    print("Removing 93...")
##    myList.remove(93)
##    listsize = myList.size()
##    print(f"Current size of the list: {listsize}")
##    checkValue(listsize,7)
##    
##
##    print("Removing 31...")
##    myList.remove(31)
##    listsize = myList.size()
##    print(f"Current size of the list: {listsize}")
##    checkValue(listsize,6)
##    
##
##    print("linkedlist after multiple removals.." + str(myList))
##    print()
##    
##
##
##    confirmValueAfterPop(myList, 54, 0)
##    confirmValueAfterPop(myList, 100, 1)
##
##    try:
##        print("Trying pop(5)...")
##        myList.pop(5)
##    except Exception as e:
##        print(f"Error: {e}")
##    
##
##
##    lastIndex = myList.size() -1
##    confirmValueAfterPop(myList, 99, lastIndex)
##
##    print("linkedlist after multiple pop operations.." + str(myList))
##    print()
    

    print("Thanks for your patience. Goodbye!")
   
if (__name__ == "__main__"):
    main()
    
