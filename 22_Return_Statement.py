# Return Statement = Functions send Python values /objects back to the caller.
#                    These values/objects are known as the function's return value.

def multiply(number1,number2):
    return number1 * number2  # Send the processed value back to the caller

x = multiply(6,8)             # The Caller

print(x)