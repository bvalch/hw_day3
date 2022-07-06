import numbers


def return_10():
    return 10

def add(number1,number2):
    return(number1+number2)

def subtract(number1,number2):
    return (number1-number2)

def multiply(number1,number2):
    return(number1*number2)

def divide(num1,num2):
    return(num1/num2)

def length_of_string(string):
    return(len(string))

def join_string(str1,str2):
    return(str1+str2)

def add_string_as_number(str1,str2):
    return(int(str1)+int(str2))

def number_to_full_month_name(num):
    calendar=['January','February','March','April','may','june','july','august','September','October','November','December']
    return calendar[num-1]

def number_to_short_month_name(num):
    calendar=['January','February','March','April','may','june','july','august','September','October','November','December']

    month=str(calendar[num-1])
    return month[0:3]

def side_cubed(lenght):
    return lenght**3

def string_reverse(string):
    reverse=string[::-1]
    return reverse
def fahrenheit_conversion(fahrenheit):
    celsius=(fahrenheit-32)*5/9
    return celsius
