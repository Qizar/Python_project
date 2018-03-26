while True:
    try:
        a = float(input("Enter the yearly salary: "))
        b = a/12
        c = b/22
        d = c/8
        print("Monthly salary: ",b)
        print("Per day salary: ",c)
        print("Per hour salary is: ",d,'\n')
    except:
        print("You can't enter anything, other than numbers.\n")
        
