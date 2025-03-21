tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableList):
    longest,longest2,longest3=0,0,0
    colWidths = [0] * len(tableData)
    list1,list2,list3 = tableData[0],tableData[1],tableData[2]
    for word in list1:
        if len(word) > longest:
            longest=len(word)
            print(longest)
    for word in list2:
        if len(word) > longest2:
            longest2=len(word)
            print(longest2)
    for word in list3:
        if len(word) > longest3:
            longest3=len(word)
            print(longest3)
    for i in range(len(list1)):
        print(list1[i].rjust(longest) + ' ' + list2[i].rjust(longest2) + ' ' + list3[i].rjust(longest3))

printTable(tableData)
