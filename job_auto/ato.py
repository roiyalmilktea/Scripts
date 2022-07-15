from datetime import datetime

y, m, d = list(map(int, input('year,month,day:').split()))
schdate = datetime(y, m, d)

now = datetime.now()

delta = schdate - now

print('remaining '+str(delta.days+1)+' day.')
