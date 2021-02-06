print("Enter numbers (type 'exit' to exit.)")
x=0
while(True):
    inpt = input()
    if inpt=='exit': 
        break
    else:      
        x+=int(inpt) 
print(x)