def FizzBuzz(i):

    begin = 1
    end = 1000

    for i in range(begin, end+1):

        if (i % 3 == 0 and i % 5 != 0):
            print ('Fizz')
        else: 
            print (i)    

        if (i % 5 == 0 and i % 3 != 0):
            print ('Buzz')
        else: 
            print (i)       

        if (i % 3 == 0 and i % 5 == 0):
            print ('FizzBuzz')
        else: 
            print (i)   

