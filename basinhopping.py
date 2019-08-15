#In present version scipy.optimize.minimize is replaced by basinhopping,
#Indeed, new version is improved and find enough good result

import numpy as np
import scipy
from scipy.optimize import basinhopping
%matplotlib inline



def fun(x):
    
    f=x[0]**2 + x[1]**2
    df = np.zeros(2)
    return f,df

# optimization process
x_start = np.array ([- 5.0, 12.0])
minimizer_kwargs = {"method": "L-BFGS-B","jac":True}
result = basinhopping(fun, x_start, niter=500, T=1.0, stepsize=0.5, minimizer_kwargs=minimizer_kwargs,interval=100, disp=True,niter_success=None)
print("global minimum: x = [%.4f, %.4f], f(x) = %.4f" % (result.x[0],result.x[1],result.fun))

