import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

N=int(4)
def newRound(value, N):
    exponent = np.ceil(np.log10(value))
    return 10**exponent*np.round(value*10**(-exponent), N)
print(np.repeat(['none', 'nylon','twine'], 9))
df = pd.DataFrame({'rifling': np.repeat(['none', 'nylon','twine'], 9),
                   'projectile': ['dart', 'dart', 'dart', 'tau', 'tau', 'tau', 'phi', 'phi', 'phi','dart', 'dart', 'dart', 'tau', 'tau', 'tau', 'phi', 'phi', 'phi','dart', 'dart', 'dart', 'tau', 'tau', 'tau', 'phi', 'phi', 'phi',],
                   'velocity': [43.5, 39.7, 41.1, 33.6, 29.8, 32.3, 21.1, 27.2, 28.4, 19.8, 23.6, 20.4, 5.5, 6.1, 7.7, 6.3, 7.2, 7.3, 20.8, 22.2, 24.6, 8.6, 7.7, 7.5, 5.2, 8.1, 7.6]})
print(df)

model = ols('velocity ~ C(rifling) + C(projectile) + C(rifling):C(projectile)', data=df).fit()
aa=sm.stats.anova_lm(model, typ=2)
print(aa)



