# Create BMI(Body Mass Index) function that takes weight and height as input and returns BMI value.
var = 0
def bmi(weight, height):
    global var
    var = weight / height ** 2
    return var

var = bmi(70, 1.75)