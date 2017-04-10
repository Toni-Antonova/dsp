[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

**Exercise 2-4**


```python
preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]
```

I was playing around with the chapter content and curious to look at what the histogram of the babies total weight looked like. 


```python
hist = thinkstats2.Hist(live.totalwgt_lb, label='totalwgt_lb')
thinkplot.Hist(hist)
thinkplot.Config(xlabel='Birth weight (pounds)', ylabel='Count')
```


![png](output_5_0.png)


I was also curious to see what the histograms of first babies' to the rest of the babies' histograms looked like side-by-side. 

Was there any obvious difference? It seems not.


```python
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

first_hist = thinkstats2.Hist(firsts.totalwgt_lb, label='first')
other_hist = thinkstats2.Hist(others.totalwgt_lb, label='other')
```


```python
width = 0.02
thinkplot.PrePlot(2)
thinkplot.Hist(first_hist, align='right', width=width)
thinkplot.Hist(other_hist, align='left', width=width)
thinkplot.Config(xlabel='weight', ylabel='Count', xlim=[6, 9])
```


![png](output_8_0.png)


Then I calculated the Cohen's d to quantify the difference between the first born babies and the other babies weights, and the difference between the first born babies and other babies preganancy lengths. 


```python
first_wgt = firsts.totalwgt_lb
others_wgt = others.totalwgt_lb
```


```python
def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()
    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return d
```


```python
wgt_cohen = CohenEffectSize(first_wgt, others_wgt)
```


```python
first_length = firsts.prglngth
others_length = others.prglngth
```


```python
length_cohen = CohenEffectSize(first_length, others_length)
```


```python
diff = abs(wgt_cohen)-length_cohen
```


```python
print ('cohen wgt: ' + str(wgt_cohen))
print ('cohen length: ' + str(length_cohen))
print ('difference: ' + str(diff))
```

    cohen wgt: -0.088672927072602
    cohen length: 0.028879044654449883
    difference: 0.059793882418152124


The difference between the two cohen's d calculations is not very big. It's around .06. 

Both cohen's d are very small - meaning there is a small effect size. 

This suggests there is most likely no significant difference between pregnancy length in first born babies vs. other babies, as well as no significant difference between total weight of first born babies vs. other babies.

______________________________________________________________________________________________________
