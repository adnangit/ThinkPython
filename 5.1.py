import time


time_since = time.time()

days_since = time_since//(3600*24)
print('Days since epoch: ',int(days_since))

time_left = time_since%(3600*24)
current_hr = time_left//3600
current_min = (time_left%3600)//60
current_sec = time_left-((current_hr*3600)+(current_min*60))

print('Hr: ',int(current_hr),' Min: ', int(current_min), ' Sec: ', int(current_sec))
