import datetime
today=datetime.datetime.today()
dayofweek =today.weekday()
if dayofweek==1:
    print ("Shit still tuesday")
elif dayofweek ==5:
    print("bollox Tueday tomorrow")
else:
    print("nope")