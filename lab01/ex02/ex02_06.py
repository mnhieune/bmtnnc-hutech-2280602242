input_str = input("Nhập X, Y: ")
dimensions = [int(x) for x in input_str.split(",")]
rownum = dimensions[0]
colnum = dimensions[1]
multilist = [[0 for col in range(colnum)] for row in range(rownum)]
for row in range(rownum) :
    for col in range(colnum) :
        multilist[row][col] = row * col
print (multilist)