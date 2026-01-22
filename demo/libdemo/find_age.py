from datetime import datetime

try:
    dobstr = input("Enter your date of birth (yyyymmdd) : ")
    dob = datetime.strptime(dobstr, "%Y%m%d")
    now = datetime.now()
    diff = now - dob
    years = diff.days // 365
    months = diff.days % 365 // 30
    days = diff.days - (years * 365 + months * 30)
    print(f"{years} y {months} m {days} d")
except:
    print('Sorry! Invalid Date. Please give date in yyyymmdd format!')
