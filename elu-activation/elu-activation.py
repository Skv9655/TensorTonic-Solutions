def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    # Write code here
    alph = 1.0
    import numpy as np

    x = np.array(x,dtype = float)

    result = list(np.where(x > 0, x, alpha*(np.exp(x)-1)))

    return result