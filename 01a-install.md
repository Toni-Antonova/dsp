# Install software on your computer


### Install [git](http://git-scm.com/).

You have it installed if you can run `git --version` at the command
line and get output like `git version 2.3.5`.


### Install [Anaconda](http://continuum.io/downloads).

There are two things you can verify to check your install.

First, from the command line, all of the following should start up
some kind of Python interpreter:

```bash
python
ipython
ipython notebook
spyder
```

Second, inside any of those Python interpreters, you should be able to
do all of these without error:

```python
import numpy
import scipy
import matplotlib
import pandas
import statsmodels
import sklearn
```

### Install [Homebrew](http://brew.sh/) on Mac

If you use a Mac, install Homebrew if you don't
have it yet. You could use Homebrew to manage your `git` and `python`
installs as well, but the methods given above are very good and more
cross-platform.

---

###Q1. Python Version 2 or 3

**Course material for the bootcamp is compatible with Python versions 2.7 and 3.0. Python 3 is recommended and encouraged.**  

Did you install Python 2 or 3? Why?  

>> I installed Python 3 because it was recommended by the bootcamp.  However, if I were to reason through it, I would most likely install 3 anyways. Python 3 has more features and is on track to become the standard language used in the future because Python 2 is not going to be maintained after 2020. Python 3 documentation also says that the language has been made more consistent so it’s a bit easier to learn. It also seems that writing good, clean code can help someone avoid 2 vs. 3 backwards compatibility issues. If at any point I do need to program in Python 2, the differences between the two languages shouldn't be too hard to navigate.

###Q2. Which Python Version Installed   

How can you check the version of Python installed if you happen to be on an unfamiliar computer?

>> Open the Terminal window and type python --version.

 


