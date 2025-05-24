import time
timestamp = time.strftime('%H')
print(timestamp)

if int(time.strftime('%H')) >= 5 and int(time.strftime('%H')) < 12:
  print("Gm")
elif int(time.strftime('%H')) >= 1 and int(time.strftime('%H')) <= 5:
  print("GA")
else:
  print("GN")
