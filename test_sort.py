# Author: Jamal Huraibi, fh1328
# Assignment 2
# Testing .sort()


if __name__ == '__main__':
    myList = [[20, 10, 30], [30, 20, 10]]

    # Index 0 (i.e. first sublist)
    print("[ First sublist: UNSORTED ]")
    for i in myList[0]:
        print("[{}] ".format(i))
    
    myList[0].sort()

    print("[ First sublist: SORTED ]")
    for i in myList[0]:
        print("[{}] ".format(i))
  
    # Index 1 (i.e. second sublist)
    print("[ Second sublist: UNSORTED ]")
    for i in myList[1]:
        print("[{}] ".format(i))
    
    myList[1].sort()

    print("[ Second sublist: SORTED ]")
    for i in myList[1]:
        print("[{}] ".format(i))
