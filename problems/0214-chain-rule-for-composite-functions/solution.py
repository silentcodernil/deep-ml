import numpy as np

def compute_chain_rule_gradient(functions: list[str], x: float) -> float:
    """
    Compute derivative of composite functions using chain rule.
    
    Args:
        functions: List of function names (applied right to left)
                  Available: 'square', 'sin', 'exp', 'log'
        x: Point at which to evaluate derivative
    
    Returns:
        Derivative value at x
    
    Example:
        ['sin', 'square'] represents sin(x²)
        ['exp', 'sin', 'square'] represents exp(sin(x²))
    """
    value = x
    values = []

    for f in reversed(functions):
        values.append((f, value))

        if f == 'square':
            value = value ** 2
        elif f == 'sin':
            value = np.sin(value)
        elif f == 'exp':
            value = np.exp(value)
        elif f == 'log':
            if value <= 0:
                return float('nan')
            value = np.log(value)

    grad = 1.0

    for f, v in values:
        if f == 'square':
            grad *= 2 * v
        elif f == 'sin':
            grad *= np.cos(v)
        elif f == 'exp':
            grad *= np.exp(v)
        elif f == 'log':
            if v <= 0:
                return float('nan')
            grad *= 1 / v

    return grad