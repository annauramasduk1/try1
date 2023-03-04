# print 1 - 100
# unutk bilanhgan yg habis dibagi 5 print "yey"
# unutk bilanhgan yg habis dibagi 3 print "saddd"
# lainnya print angka

for i in range(0,101):
    if i % 5 == 0:
        print("yeay")
    elif i % 3 == 0 :
        print("sad")
    else:
        print(i)