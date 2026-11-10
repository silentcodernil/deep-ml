import math
def orthogonal_projection(v, L):
    """
    Compute the orthogonal projection of vector v onto line L.

    :param v: The vector to be projected
    :param L: The line vector defining the direction of projection
    :return: List representing the projection of v onto L
    """
    numerator=0
    denomintor=0
    for i in range(len(v)):
        numerator+=v[i]*L[i]
        denomintor+=L[i]*L[i]
    
    cos=numerator/(denomintor)
    ans=[]
    for i in range(len(v)):
        ans.append(L[i]*cos)

    return ans

