def second_large():
    a = []
    while True:
        number = input("Your number:")
        if number.lower() == 'q':
            break
        try:
            val = int(number)
            a.append(val)
        except ValueError:
            print("Not a number")

    if len(set(a)) < 2:
        print("Not enough number")
            
    else:
        a.sort()
        a.pop()
        print(a[-1])
    

second_large()
            
        
                
