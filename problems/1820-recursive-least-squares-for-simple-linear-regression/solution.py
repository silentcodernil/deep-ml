import numpy as np

def online_simple_regression(xs, ys):
    # return (N, 2) array of (w0, w1) after each point
    n=0
    mean_x=0.0
    mean_y=0.0

    Mxx=0.0
    Mxy=0.0

    result=[]

    for x,y in zip(xs,ys):
        n+=1
        dx=x-mean_x
        dy=y-mean_y

        mean_x+=dx/n 
        mean_y+=dy/n 
        Mxx += dx * (x - mean_x)
        Mxy += dx * (y - mean_y)

        w1 = Mxy / Mxx if Mxx != 0 else 0.0
        
        w0=mean_y - (w1*mean_x)

        result.append([w0,w1])
    return np.array(result, dtype=float).reshape(-1, 2)