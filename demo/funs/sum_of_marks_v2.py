def getmarks(s):
    if s.isdigit():
        return int(s)
    else:
        return 0

data = "56,89,a,70"
marks = data.split(",")
total = sum(map(getmarks, marks))
print(total)
