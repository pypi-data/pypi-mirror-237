# ipython-autotime-pst
Time everything in IPython

## Installation:

```console
$ pip install -i https://pypi.org/project ipython-autotime-pst
```

## Examples

```python
In [1]: %load_ext autotime
time: 264 µs (started: 2020-12-15 11:44:36 +07:00)

In [2]: x = 1
time: 416 µs (started: 2020-12-15 11:44:45 +07:00)

In [3]: x / 0
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-3-034eb0c6102b> in <module>
----> 1 x/0

ZeroDivisionError: division by zero
time: 88.7 ms (started: 2020-12-15 11:44:53 +07:00)
```

## Want to turn it off?

```python
In [4]: %unload_ext autotime
```
