**環境構築**

```
~/go/src/github.com/pei0804/python-example/sandbox master
❯ python3 -m venv basis

~/go/src/github.com/pei0804/python-example/sandbox master*
❯ ls
basis

~/go/src/github.com/pei0804/python-example/sandbox master*
❯ cd basis
bin        include    lib        pyvenv.cfg

~/go/src/github.com/pei0804/python-example/sandbox/basis master*
❯ source bin/activate

~/go/src/github.com/pei0804/python-example/sandbox/basis master*
(basis) ❯ ls
bin        include    lib        pyvenv.cfg

~/go/src/github.com/pei0804/python-example/sandbox/basis master*
(basis) ❯
```

**対話モード**

```
~/go/src/github.com/pei0804/python-example/sandbox/basis master*
(basis) ❯ python
Python 3.4.4 (default, Apr 16 2018, 21:01:39)
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 1 + 2 * 4
9
>>> 1 + (10 - 1)
10
>>> a = 10 + 2
>>> b = 5
>>> a + b
17
>>> import math
>>> math.sin(1)
0.8414709848078965
>>> math.
math.__class__(         math.__format__(        math.__loader__         math.__reduce_ex__(     math.acos(              math.ceil(              math.erfc(              math.frexp(             math.ldexp(             math.pi                 math.tanh(
math.__delattr__(       math.__ge__(            math.__lt__(            math.__repr__(          math.acosh(             math.copysign(          math.exp(               math.fsum(              math.lgamma(            math.pow(               math.trunc(
math.__dict__           math.__getattribute__(  math.__name__           math.__setattr__(       math.asin(              math.cos(               math.expm1(             math.gamma(             math.log(               math.radians(
math.__dir__(           math.__gt__(            math.__ne__(            math.__sizeof__(        math.asinh(             math.cosh(              math.fabs(              math.hypot(             math.log10(             math.sin(
math.__doc__            math.__hash__(          math.__new__(           math.__spec__           math.atan(              math.degrees(           math.factorial(         math.isfinite(          math.log1p(             math.sinh(
math.__eq__(            math.__init__(          math.__package__        math.__str__(           math.atan2(             math.e                  math.floor(             math.isinf(             math.log2(              math.sqrt(
math.__file__           math.__le__(            math.__reduce__(        math.__subclasshook__(  math.atanh(             math.erf(               math.fmod(              math.isnan(             math.modf(              math.tan(
>>> math.p
math.pi    math.pow(
>>> math.pi
3.141592653589793
>>>
```

**IPython対話モード**

```
~/go/src/github.com/pei0804/python-example/sandbox/basis master* 12s
(basis) ❯ pip install ipython
...
...
...
...

~/go/src/github.com/pei0804/python-example/sandbox/basis master* 12s
(basis) ❯ ipython
zsh: correct 'ipython' to 'python' [nyae]? n
Python 3.4.4 (default, Apr 16 2018, 21:01:39)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.4.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: a = 2

?をつけることで中身を見れる
In [2]: a?
Type:        int
String form: 2
Docstring:
int(x=0) -> integer
int(x, base=10) -> integer

Convert a number or string to an integer, or return 0 if no arguments
are given.  If x is a number, return x.__int__().  For floating point
numbers, this truncates towards zero.

If x is not a number or if base is given, then x must be a string,
bytes, or bytearray instance representing an integer literal in the
given base.  The literal can be preceded by '+' or '-' and be surrounded
by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
Base 0 means to interpret the base from the string as an integer literal.
>>> int('0b100', base=0)
4

!でシェルへのアクセス
In [3]: !echo "Hello World!"
Hello World!

%でマジックコマンド
%timeitの場合、実行時間
In [4]: %timeit 1 + 1

14.4 ns ± 1.36 ns per loop (mean ± std. dev. of 7 runs, 100000000 loops each)

%%でふくすうぎょう
In [5]: %%timeit
   ...: a = 1 + 1
   ...: b = 2
   ...: a + b
   ...:


43.4 ns ± 0.284 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
```

**jupyter**

```
~/go/src/github.com/pei0804/python-example/sandbox/basis master*
(basis) ❯ pip install jupyter
Collecting jupyter
...

~/go/src/github.com/pei0804/python-example/sandbox/basis master*
(basis) ❯ jupyter notebook
[I 22:05:15.069 NotebookApp] Writing notebook server cookie secret to /Users/jumpei/Library/Jupyter/runtime/notebook_cookie_secret
[I 22:05:15.487 NotebookApp] Serving notebooks from local directory: /Users/jumpei/go/src/github.com/pei0804/python-example/sandbox/basis
[I 22:05:15.487 NotebookApp] 0 active kernels
[I 22:05:15.487 NotebookApp] The Jupyter Notebook is running at:
[I 22:05:15.487 NotebookApp] http://localhost:8888/?token=c55030d020933ba26b438815446de18c5c69f96c69e96a85
[I 22:05:15.487 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 22:05:15.489 NotebookApp]

    Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://localhost:8888/?token=c55030d020933ba26b438815446de18c5c69f96c69e96a85&token=c55030d020933ba26b438815446de18c5c69f96c69e96a85
[I 22:05:16.346 NotebookApp] Accepting one-time-token-authenticated connection from ::1
```
