for digits in range (4 , 9) :
 PIN = 10 ** digits
 minutes = int(( PIN / 10 ) // 60)
 days = int((minutes // 60) // 24 )
 print ((f"{digits} digits : {PIN} PINs, {minutes} minutes, {days} days"))