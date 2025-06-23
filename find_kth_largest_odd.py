'''Given a list of integers and an integer k,\
find the k-th largest odd number in the list. \
If there are not enough odd numbers, return "Not enough odd numbers".
'''



def find_kth_largest_odd():
    a =[]
    oddlist = []
    evenlist = []
    n = int(input("Enter which larger odd number you choose"))
    print("Enter number or 'k' to stop")
    while True:
        number = input("Number:")
        if number.lower()=='k':
            break
        else:
            try:
                num = int(number)
                a.append(num)
            except ValueError:
                print("Please enter a number")
    if not a:
        print("No number")

        
    for  i in a:
        if i %2 !=0:
            oddlist.append(i)
        else:
            evenlist.append(i)
    oddlist.sort(reverse = True)

    if len(list(oddlist)) < n:
        print("No enough number")
    print("output :",oddlist[n-1])
        
        
    

find_kth_largest_odd()
            
        
                
