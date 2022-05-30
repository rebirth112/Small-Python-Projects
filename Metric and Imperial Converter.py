#metric and imperial conversion

def metricToImperial(length, width):
    length = length / 2.54
    width = width / 2.54
    print("The length is " + str(length) + " inches and the width is " + str(width) + " inches.")

def imperialToMetric(length, width):
    length = length * 2.54
    width = width * 2.54
    print("The length is " + str(length) + " cm and the width is " + str(width) + " cm.")

while True:
    userChoice = input('Are you converting from metric to imperial? If so, press "y". For reverse press "n".\n')
    if (userChoice == "y"):
        length = input('enter length in cm\n')
        length = float(length)
        width = input('enter width in cm\n')
        width = float(width)
        metricToImperial(length, width)
    else:
        length = input('enter length in inches\n')
        length = float(length)
        width = input('enter width in inches\n')
        width = float(width)
        imperialToMetric(length, width)
    userRepeat = input('convert again? Enter n to end program\n')
    if userRepeat == 'n':
        break; 
