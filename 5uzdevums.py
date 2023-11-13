import datetime

laiks = datetime.datetime.now()
stunda = laiks.hour
print("pulkstens:", stunda)
if stunda < 8:
    print("Labrīt")
elif stunda > 8 and stunda < 19:
    print("Labdien")
elif stunda >= 19:
    print("Labvakar")