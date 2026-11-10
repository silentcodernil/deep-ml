import math

PI = 3.14159

def power_grid_forecast(consumption_data):
    # 1) Subtract the daily fluctuation (10 * sin(2π * i / 10)) from each data point.
    # 2) Perform linear regression on the detrended data.
    # 3) Predict day 15's base consumption.
    # 4) Add the day 15 fluctuation back.
    # 5) Round, then add a 5% safety margin (rounded up).
    # 6) Return the final integer.
    n=len(consumption_data)
    x=list(range(1,n+1))

    base=[]
    for i in range(n):
        function=10*math.sin((2*math.pi*x[i])/10)
        base.append(consumption_data[i]-function)

    mean_x=sum(x)/n 
    mean_y=sum(base)/n 

    numerator = 0
    denominator = 0
    for i in range(n):
        numerator += (x[i] - mean_x) * (base[i] - mean_y)
        denominator += (x[i] - mean_x) ** 2

    slope = numerator / denominator

    intercept = mean_y - slope * mean_x
    base_prediction = intercept + slope * 15
    return math.ceil(base_prediction * 1.05)

