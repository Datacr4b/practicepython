def comma(argument):
    var=''
    for index, item in enumerate(argument):
        if index < (len(argument)-1):
            var = var+str(item)+','
        else:
            var = var+'and '+str(item)
    print(var)

comma([2,5,7,'cats','dogs'])
