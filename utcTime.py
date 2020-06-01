from PyQt5.QtCore import QDateTime,Qt

datetime = QDateTime.currentDateTime()

print('local date and time is '+ datetime.toString(Qt.DefaultLocaleLongDate))
print("universal date and time is "+ datetime.toUTC().toString())

print('the offset from utcis {0} : seconds'.format(datetime.offsetFromUtc()))