from PyQt5.QtCore import QDateTime, QDate,QTime,Qt


datetime = QDateTime.currentDateTime()

print(datetime.toString())
print(datetime.toString(Qt.ISODate))
print(datetime.toString(Qt.DefaultLocaleLongDate))

date = QDate.currentDate()

print(date.toString())
print(date.toString(Qt.ISODate))
print(date.toString(Qt.DefaultLocaleLongDate))

time = QTime.currentTime()
print(time.toString())
print(time.toString(Qt.DefaultLocaleLongDate))

# find days in month and year
d = QDate(2017, 8, 23)
print('Days in a month: {0}: '.format(d.daysInMonth()))
print('Days in an year: {0}:'.format(d.daysInYear()))

# adding days month years and seconds 
print("Todays date and time is: "+ datetime.toString(Qt.ISODate))
# adding 12 dates to my current date  
nextdate = datetime.addDays(12)
print('Adding 12 days to the date : {0} '.format(nextdate.toString(Qt.ISODate)))

# subracting 12 days from the nextdate 
prevdate = nextdate.addDays(-12)
print('Substracting 12 days: {0}'.format(prevdate.toString(Qt.ISODate)))

# adding 50 seconds 
add50sec = datetime.addSecs(50)
print('Adding 50 seconds on the current time is: {0} '.format(add50sec.toString(Qt.ISODate)))

# adding 3 months from current time 
add3months = datetime.addMonths(3)
print('Adding 3 months: {0} '.format(add3months.toString(Qt.ISODate)))

# adding 12 years from our current date  
next12years = datetime.addYears(12)
print('Adding 12 years from our current time is: {0} '.format(next12years.toString(Qt.ISODate)))