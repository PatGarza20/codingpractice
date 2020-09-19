## Given a string containing a span from one time to another, calculate the minutes between the two times.
## e.g 10:00 AM - 11:00 AM returns 60
## e.g 1:00 PM - 11:00 AM returns 1320

def calcTime(data):
    # The string is parsed into seperate values and inserted into list "times".
    # e.g "10:00 AM - 11:00 AM" becomes ["10:00", "AM", "-", "11:00", "AM"]
    times = []
    temp = []

    for letter in data:
        if letter != ' ':
            temp.append(letter)
        else:
            tempStr = ''.join(temp)
            times.append(str(tempStr))
            temp = []

    # Have to do this one more time after the loop ends to get the last value into times.
    tempStr = ''.join(temp)
    times.append(str(tempStr))

    # Parsing the strings into integers for calculation.
    # ifElse to account for when there's only one digit in hours.
    if len(times[0]) == 5:
        hoursOne = int(times[0][0] + times[0][1])
        minutesOne = int(times[0][3] + times[0][4])
    
    else:
        hoursOne = int(times[0][0])
        minutesOne = int(times[0][2] + times[0][3])
    
    # By a 24-hour clock, "PM" just means 12 hours ahead of "AM".
    if times[1] == 'PM':
        hoursOne += 12


    if len(times[3]) == 5:
        hoursTwo = int(times[3][0] + times[3][1])
        minutesTwo = int(times[3][3] + times[3][4])

    else:
        hoursTwo = int(times[3][0])
        minutesTwo = int(times[3][2] + times[3][3])

    if times[4] == 'PM':
        hoursTwo += 12

    # Converting hours to minutes and adding them together.
    timeOne = (hoursOne * 60) + minutesOne
    timeTwo = (hoursTwo * 60) + minutesTwo

    # Calculates the difference between both times and uses abs() to return a positive num.
    result = abs(timeOne - timeTwo)

    # If the second time is earlier in the day than the first time, we subtract the result
    # from 24 hours worth of minutes (1440).
    if timeOne >= timeTwo:
        result = 1440 - result

    return result

if __name__ == "__main__":
    span = "10:00 AM - 11:00 AM"
    # prints 60
    print(calcTime(span))

    span = "1:00 PM - 11:00 AM"
    # prints 1320
    print(calcTime(span))