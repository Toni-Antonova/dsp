[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

**Full Jupyter File of Ex. can be found in statistics folder: Think%2BStats-2.ipynb**  

**Exercise 5-1**

In the BRFSS (see Section 5.4), the distribution of heights is roughly normal with parameters μ = 178 cm and σ = 7.7 cm for men, and μ = 163 cm and σ = 7.3 cm for women.
In order to join Blue Man Group, you have to be male between 5’10” and 6’1” (see http://bluemancasting.com). What percentage of the U.S. male population is in this range? Hint: use scipy.stats.norm.cdf.

Thought Process:

The distribution of heights for men is roughly normal. This means that I need to evaluate the normal cdf for male heights 5'10" and 6'1". The difference between these two evaluations should be the percentage of the male population in this range. This is because the CDF shows the percentage of men at the height specified and lower. 


```python
import scipy.stats
scipy.stats.norm.cdf(0)

def EvalNormalCdf(x, mu=0, sigma=1):
    return scipy.stats.norm.cdf(x, loc=mu, scale=sigma)

maleone = 5*12*2.54+10*2.54 
maletwo = 6*12*2.54 +1*2.54
diff = EvalNormalCdf(maletwo, 178, 7.7) - EvalNormalCdf(maleone, 178, 7.7)
print(diff)
```

    0.342746837631


Approxmately 34.3% of the male population fall within the range that the Blue Man Group casting specifications require. 
