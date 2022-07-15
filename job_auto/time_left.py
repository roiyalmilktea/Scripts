from datetime import datetime


a, b, c, d, e, f = list(map(int, input('sleep:').split()))
u, v, w, x, y, z = list(map(int, input('wake:').split()))

sleep_t = datetime(a, b, c, d, e, f)
wakeup_t = datetime(u, v, w, x, y,)

delta = wakeup_t - sleep_t

print(type(delta))
sec = delta.seconds
hours = sec / (60*60)

print('late '+str(hours)+'.')
