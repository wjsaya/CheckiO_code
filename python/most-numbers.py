#传入一个数组，取最大，取最小，然后最大最小之间差值
#https://py.checkio.org/mission/most-numbers/
def checkio(*args):
    if ( len(args) == 0 ):
        return 0
    max=args[0]
    min=args[0]
    cha=args[0]
    for i in args:
        if (i>max):
            max=i
        elif (i<min):
            min=i

    cha =max-min
    if (cha < 0):
        cha = -cha
    return (cha)
	
if __name__ == '__main__':
	c = checkio()
	print (c)
#Precondition: 0 ≤ len(args) ≤ 20
#all(-100 < x < 100 for x in args)
#all(isinstance(x, (int, float)) for x in args) 
