lower = 10
upper = 100

input("Enter a number ( {} - {}): ".format(lower,upper))
for i in range(10,  120,  11):    #  make  sure  we  have  integers  of  different  'length'
    print("{}  {}".format(i,  chr(i)))