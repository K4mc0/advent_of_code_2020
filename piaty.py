with open('input.txt') as f:
    lines = f.read().splitlines()
pole = []
for line in lines:
    x = int (line[0:7].replace('B','1').replace('F','0'),2)
    y = int (line[7:10].replace('R','1').replace('L','0'),2)
    #if (x*8+y) in pole:
    #    print (f'text: {x*8+y}, x: {x}, y: {y}')
    pole.append(x*8+y)
pole.sort()
print (pole)
print ("max hodnota je ", pole[-1])
i=11
for prvok in pole:
    if i != prvok:
        print (prvok-1)
        break
    i += 1

    
#with open('input.txt') as f:
#lines = f.read().split('\n\n')
