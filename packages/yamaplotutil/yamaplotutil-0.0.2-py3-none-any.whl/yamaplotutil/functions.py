import math
from yamaplotutil import dtypes

def make_fitted_polynom_values(x: dtypes.numericArray, coefficients: dtypes.numericArray):
    """This returns a list of all y values for the passed x-values calculated with with a*x**(n)+b*x**(n-1)+...+z, where n is the degree of the polynom and
    and len(coefficients)-1
     
    numeric is int, float or complex, numericArray is a list of numeric"""
    _deg = len(coefficients)-1
    yFit: dtypes.numericArray = []
    for _x in range(len(x)):
        deg = _deg
        y = 0.0
        for coeff in range(len(coefficients)):
            y = y + coefficients[coeff] * x[_x]**deg
            deg -= 1
        yFit.append(y)
    return yFit

def make_fitted_sin_values(x: dtypes.realArray, a: dtypes.numeric, b: dtypes.real, c: dtypes.real, d: dtypes.numeric):
    """This returns a list of all y values for the passed x-values calculated with with a*sin(b*x+c)+d
     
    numeric is int, float or complex; numericArray is a list of numeric; real is int or float; realArray is a list of real"""
    yFit: dtypes.numericArray = []

    for _x in x:
        yFit.append(a*math.sin(b*_x+c)+d)
    
    return yFit

def make_fitted_cos_values(x: dtypes.realArray, a: dtypes.numeric, b: dtypes.real, c: dtypes.real, d: dtypes.numeric):
    """This returns a list of all y values for the passed x-values calculated with with a*cos(b*x+c)+d
     
    numeric is int, float or complex; numericArray is a list of numeric; real is int or float; realArray is a list of real"""
    yFit: dtypes.numericArray = []

    for _x in x:
        yFit.append(a*math.cos(b*_x+c)+d)
    
    return yFit

def make_fitted_ln_values(x: dtypes.realArray, a: dtypes.numeric, b: dtypes.numeric):
    """This returns a list of all y values for the passed x-values calculated with with a*ln(x)+b
     
    numeric is int, float or complex; numericArray is a list of numeric; real is int or float; realArray is a list of real"""
    yFit: dtypes.numericArray = []
    for _x in x:
        yFit.append(a*math.log(_x) + b)
    return yFit

def make_fitted_exp_values(x: dtypes.realArray, a: dtypes.numeric, b: dtypes.real, c: dtypes.numeric):
    """This returns a list of all y values for the passed x-values calculated with with a*exp(x*b)+c
     
    numeric is int, float or complex; numericArray is a list of numeric; real is int or float; realArray is a list of real"""
    yFit: dtypes.numericArray = []
    for _x in x:
        yFit.append(a*math.exp(_x*b)+c)
    return yFit

def make_fitted_function_values(x, parameters, f):
    """This returns a list of all y values for the passed x-values calculated with with f(x, parameters[0], parameters[1], ... , parameters[len(parameters)-1])"""
    yFit = []

    for _x in x:
        yFit.append(f(_x, *parameters))
    return yFit