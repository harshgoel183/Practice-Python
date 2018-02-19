#tune = int(input("hey ur number?\n"))
#print(tune)

while True:
    try:
        number = int(input("what ur number\n"))
        print(2/number)
        break
    except ValueError:
        print("Make sure to enter a number")
    except ZeroDivisionError:
        print("Dont take 0")
    #except: this is the general expecption,avoid it
     #   break
    finally:
        print("Loop ends here")
