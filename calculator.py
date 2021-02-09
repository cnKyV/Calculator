print("Enter numbers (+,x,-,/ for opeations) ('exit' to exit)")
x=[]
while(True):
    inpt = input()
    val = 0
    if inpt=='exit': 
        break
    elif(inpt=='+'):
        for numero in x:
            val+=numero
        print(val)
        val=0 
        x.clear()
    elif(inpt=='-'):
        val=x.pop(0)
        for numero in x:
            val-=numero
        print(val)
        val=0 
        x.clear()
    elif(inpt=='x'):
        val=x.pop(0)
        for numero in x:
            val*=numero
        print(val)
        val=0
        x.clear()
    elif(inpt=='/'):
        val = x.pop(0)
        for numero in x:
            val/=numero
        print(val)
        val=0 
        x.clear()
    else:
        x.append(int(inpt))



#if (inpt == '+'):
