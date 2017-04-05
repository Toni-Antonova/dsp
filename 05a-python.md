# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Both tuples and lists are sequences. Tuples, unlike lists, are immutable. Because of this, tuples will work as keys in dictionaries. Dictionaries only accept immutable types as keys.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> A set behaves like a collection of dictionary keys with no values. This means that an element can only appear in a set once, much like a key in a dictionary. This is not the case for lists. Because of this characteristic, the use of sets over lists can often simplify code and reduce run-time. 

On the other hand, lists provide users more control. A list is an ordered sequence of elements whereas a set is a distinct list of elements that is unordered. Lists therefore allow the user precise control over where in the list each element is inserted using integer indexes. Programmers don't have this kind of positional access when dealing with sets.

Here is an example of a function written two ways. Lists are used in the first code, whereas sets are used in the second. The fuction takes a list as an argument, returns True if any object appears in the list more than once, and returns False otherwise.
 
def has_duplicates(t):
    d = {}
    for x in t:
        if x in d:
            return True
        d[x] = True
return False

def has_duplicates(t):
    return len(set(t)) < len(t)

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> The lambda function is a way to create anonymous functions, aka function definitions without a name/ identifier. These function are typically only needed where they have been created and nowhere else. They are often used as arguments being passed to higher-order function or for constructing the result of a higher-order function that returns a function type. 

This function sorts a list of numbers by the sum of their last two digits: 

sorted (numbers, key = lambda x: (sum  ([int(y) for y in str (x%100)])))

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions can be used to write mapping and filtering functions that are more concise than functions that use other loops to iterate through lists. List comprehensions also usually run faster. On the downside, they are often harder to debug because you can't put a print statement inside their loop.

The textbook gave examples that showed how list comprehensions can shorten both mapping and filter functions. 

Mapping Function without List Comprehensions 

def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
return res

Mapping Function with List Comprehensions 
def capitalize_all(t):
    return [s.capitalize() for s in t]
    
Filtering Function without List Comprehensions    
def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res

Filtering Function with List Comprehension
def only_upper(t):
    return [s for s in t if s.isupper()]

Example of Set Comprehension:

Not Using Set Comprehension ---> s = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ])

Using Set Comprehension ----> s = {x for x in range(10)}

Example of Dictionary Comprehension

Not using Dict Comprehension ---> d = dict([(i, chr(65+i)) for i in range(4)])

Using Dict Comprehension --> d = {i : chr(65+i) for i in range(4)}


---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





