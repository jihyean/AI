print('-----'*5)
#int func(int a, int b, float c)
def func(a, b, c):
    _a = a
    _b = b
    _c = c
    print(_a)
    print(_b)
    print(_c)

if __name__=="__main__" :
    print('call main()')

func(1,2,3)
func(1,[1,2,3,4,5,6], "string")
 
