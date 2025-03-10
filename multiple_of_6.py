def get_multiple():
    """
    Return a multiple of 6 that was entered by the user
    :return: int a number
    """
    while True:
        try: #lets me test a block of code for errors
            n = input("Please give me a multiple of 6:")
            n = int(n) #converts to int
            # how to check if it is a multiple of 6?
            if n% 6 == 0: #checks that the remainder is 0
                return n #return and break do the same thing
            #another way to check:
            if n/6 == n//6: #floating point division (decimal) must be the same as integer division (whole number)
                return n
            else:
                print("The is not a multiple of 6")
        except ValueError:
            print("you have not entered an integer")

get_multiple()