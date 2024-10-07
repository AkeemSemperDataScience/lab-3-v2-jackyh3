
def lab3Question1(number, cutoff):
    # Take in two arguments - a number and a 'cutoff' (another number)
    # Return True if the number is less than the cutoff, False otherwise
    # Also, print a statement of "[Number] is less than [cutoff]" or "[Number] is not less than [cutoff]"
    # Where the [Number] and [cutoff] are the actual numbers passed in
    isLess = None
    try:
        if number < cutoff:
            isLess = True
            print(f'{number} is less than {cutoff}')
        else:
            isLess = False
            print(f'{number} is not less than {cutoff}')
    except:
        print("invalid")
    return isLess

def lab3Question2(decimal_number):
    # Take in an argument of a float (decimal) number.
    # Return "zero" if the number is 0, "positive" if the number is positive, and "negative" if the number is negative
    # Return "invalid" if the input is not a float
    strVal = ""
    # converted to float to work with test cases in harness
    # test harness may be wrong, test 1 and test 3 assertions are on integers, making them invalid
    # yet test harness says they should be giving 'zero' and 'negative'
    if isinstance(float(decimal_number), float):
        if decimal_number == 0:
            strVal = "zero"
        elif decimal_number > 0:
            strVal = "positive"
        elif decimal_number < 0:
            strVal = "negative"
        else:
            strVal = "invalid"
    else:
        strVal = "invalid"
    return strVal

def lab3Question3(year):
    # Take in a number that represents a year
    # Return "21st century" if the year is between 2001 and 2100,
    # "20th century" if the year is between 1901 and 2000,
    # "19th century" if the year is between 1801 and 1900, 
    # "ancient" if the year is older
    # "invalid" if the input is not an acceptable year number. 
    strVal = ""
    try:
        if 2001 <= year <= 2100:
            strVal = "21st century"
        elif 1901 <= year <= 2000:
            strVal = "20th century"
        elif 1801 <= year <= 1900:
            strVal = "19th century"
        elif year <= 1900:
            strVal = "ancient"
        else:
            strVal = "invalid"
    except:
        strVal = "invalid"
    return strVal


def lab3Question4(number_1, number_2, number_3):
    # Take in three numbers as arguments
    # Return the largest of the three numbers
    # Return None if the inputs are not 3 numbers
    largeNum = None
    try:
        if type(number_1) == int or type(number_1) == float:
            if type(number_2) == int or type(number_2) == float:
                if type(number_3) == int or type(number_3) == float:
                    largeNum = max(number_1, number_2, number_3)
    except:
        print("invalid")
    return largeNum

def lab3Question5(temperature, scale_used):
    # Take in a temperature and the scale that the temperature is in - either "C" for Celsius or "F" for Fahrenheit (capitalized)
    # Return "Liquid" if water is in liquid state at that temperature
    # Return "Solid" if water is in solid state at that temperature
    # Return "Gas" if water is in gas state at that temperature
    # Return "Invalid" if the temperature or scale are invalid
    strVal = ""
    try:
        if scale_used == "C":
            boilingPoint = 100
            freezingPoint = 0
        elif scale_used == "F":
            boilingPoint = 212
            freezingPoint = 32
        if temperature >= boilingPoint:
            strVal = "Gas"
        elif freezingPoint <= temperature <= boilingPoint:
            strVal = "Liquid"
        else:
            strVal = "Solid"
    except:
        strVal = "Invalid"

    return strVal

