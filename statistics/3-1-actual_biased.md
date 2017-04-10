[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

**Full Jupyter File of Ex. can be found in statistics folder: Think%2BStats-2.ipynb**  


**Exercise 3-1**

Something like the class size paradox appears if you survey children and ask how many children are in their family. Families with many children are more likely to appear in your sample, and families with no children have no chance to be in the sample.

Use the NSFG respondent variable NUMKDHH to construct the actual distribution for the number of children under 18 in the household.

Now compute the biased distribution we would see if we surveyed the children and asked them how many children under 18 (including themselves) are in their household.

Plot the actual and biased distributions, and compute their means. As a starting place, you can use chap03ex.ipynb.


```python
resp = nsfg.ReadFemResp()

pmf = thinkstats2.Pmf(resp.numkdhh, label='actual')

def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)
    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
    new_pmf.Normalize()
    return new_pmf

biased = BiasPmf(pmf, label='biased')

thinkplot.Pmf(pmf)
thinkplot.Text(.5, .55, 'Actual')
thinkplot.Config(xlabel='kids in family', ylabel='pmf')

```


![png](output_20_0.png)



```python
thinkplot.Pmf(biased)
thinkplot.Text(.5, .45, 'Biased')
thinkplot.Config(xlabel='kids in family', ylabel='pmf')
```


![png](output_21_0.png)



```python
mean_actual = pmf.Mean()
mean_biased = biased.Mean()
print('The mean of the actual distribution is ' + str(mean_actual)+ '. The mean of the biased distribution is '+ str(mean_biased)+'.')
```

    The mean of the actual distribution is 1.02420515504. The mean of the biased distribution is 2.40367910066.

