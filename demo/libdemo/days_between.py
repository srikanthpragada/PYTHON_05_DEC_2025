from datetime import datetime

while True:
    try:
        first = input("Enter first date of birth (dd-mm-yyyy) or enter to exit : ")
        if first == "":
            exit()

        fd = datetime.strptime(first, "%d-%m-%Y")
        break
    except Exception:
        print('Sorry! Invalid Date. Please give date in dd-mm-yyyy format!')

while True:
    try:
        second = input("Enter second date of birth (dd-mm-yyyy) : ")
        if second == "":
            exit(0)

        sd = datetime.strptime(second, "%d-%m-%Y")
        diff = sd - fd
        print(f"No. of days =  {diff.days}")
        break
    except:
        print('Sorry! Invalid Date. Please give date in dd-mm-yyyy format!')
