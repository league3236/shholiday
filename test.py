from shholiday import holiday2020 as hd

daytuple = (1,1)
nowholiday = hd.holiday2020()
print(nowholiday.is_holiday(daytuple))