
def convertor(x):
    celcius = round((x - 32)* (5/9), 2)
    return celcius


try:
    temp = float(input("Please enter the temperature in Fahrenheit: "))
    temp_celcius = convertor(temp)

except ValueError:
    print("Pleaes enter a valid number for temperature")

else:
    print(f"{temp} degrees Farenheit is {temp_celcius} degrees celcius.")

finally:
    print("Thank you for using temperature converter application.")

