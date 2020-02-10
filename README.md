# fuzzkill

JSON API Fuzzer in python3

# Installing

```
$ git clone https://github.com/dosisod/fuzzkill
$ cd fuzzkill
$ pip3 install -r requirements.txt
```

# Testing

Install additional requirements:

```
$ pip3 install -r test-requirements.txt
```

Check for type errors with [mypy](https://github.com/python/mypy):

```
$ ./mypy.sh
```

Make sure tests are passing with [pytest](https://pypi.org/project/pytest/):

```
$ pytest testing/
```
