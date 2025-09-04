import calendar
from pystyle import *

print(Box.Lines('[+] Calendar'))
Write.Print('[-] Calendar \n ',Colors.purple_to_red, interval=0.1)
print(Box.Lines("<Program Calendar>"))
y = int(Write.Input('please write the yaer  : ',Colors.red_to_yellow,interval=0.2))
m = int(Write.Input('please write the month : ',Colors.red_to_yellow,interval=0.2))
finall = calendar.month(y,m)
Write.Print(finall , Colors.green_to_white,interval=0.2)
input('\n ------------------- \n')