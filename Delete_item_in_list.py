list1=['ali:123232' , 'majid:456464' , 'sara:5464565' , 'reza:343543' , 'maryam:5646']

x = input('type your name: ')

for i in list1:
    if  x == i.split(":")[0]:
        # y=list1.index(i)
        list1.pop(list1.index(i))
        print(list1)
        break
    else:
        print('sorry')
