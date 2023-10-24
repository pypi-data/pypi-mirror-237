from yamaplotutil import dtypes
import math

def fit_lin(x: dtypes.numeric, m: dtypes.numeric, b: dtypes.numeric):
    """This returns the result of m*x+b and can be used as a function for fitting
     
    numeric is int, float or complex"""
    return m*x+b

def fit_quad(x: dtypes.numeric, a: dtypes.numeric, b: dtypes.numeric, c: dtypes.numeric):
    """This returns the result of a*x²+b*x+c and can be used as a function for fitting
     
    numeric is int, float or complex"""
    return a*x**2+b*x+c

def fit_cube(x: dtypes.numeric, a: dtypes.numeric, b: dtypes.numeric, c: dtypes.numeric, d: dtypes.numeric):
    """This returns the result of a*x³+b*x²+c*x+d and can be used as a function for fitting
     
    numeric is int, float or complex"""
    return a*x**3+b*x**2+c*x+d

def fit_exp(x: dtypes.real, a: dtypes.numeric, b: dtypes.real, c: dtypes.numeric):
    """This returns the result of a*e^(x*b)+c and can be used as a function for fitting
     
    numeric is int, float or complex; real is int or float"""
    return a*math.exp(x*b)+c

def fit_ln(x: dtypes.real, a: dtypes.numeric, b: dtypes.numeric):
    """This returns the result of a*ln(x)+b and can be used as a function for fitting
     
    numeric is int, float or complex; real is int or float"""
    return a*math.log(x)+b

def fit_sin(x: dtypes.real, a: dtypes.numeric, b: dtypes.real, c: dtypes.real, d: dtypes.numeric):
    """This returns the result of a*sin(b*x+c)+d and can be used as a function for fitting
     
    numeric is int, float or complex; real is int or float"""
    return a*math.sin(b*x+c)+d

def fit_cos(x: dtypes.real, a: dtypes.numeric, b: dtypes.real, c: dtypes.real, d: dtypes.numeric):
    """This returns the result of a*cos(b*x+c)+d and can be used as a function for fitting
     
    numeric is int, float or complex; real is int or float"""
    return a*math.cos(b*x+c)+d