# Python without GIL 🚀🌟🐍
Python community is celebrating a long-awaited milestone — the removal of the Global Interpreter Lock (GIL)! </br>
From lots of years GIL has been bottleneck for CPU bound multithreaded programs. Now python introduced version [3.13](https://docs.python.org/3.13/whatsnew/3.13.html#free-threaded-cpython) and the wait is over, we can use this experimental feature to see the performance of python with GIL removed on multithreaded programs.

## But what the heck is GIL ?
<b>Process : </b>Program is in execution state known as process.<br>
<b>Thread : </b>Thread is single unit of execution.<br>
- A process can have multiple threads.<br>
- Two or more processes cannot share the same memory directly.
- Two or more threads can access the same memory directly.

GIL which stands for Global Interpreter Lock, in simple words it is a mutex lock that allows only one thread at a time to execute.<br>
But it is more than just a mutex lock.<br>
Example: if a thread wants to execute then it will set mutex lock, now once it is set no other thread can execute without mutex lock. so another threads will be in waitng state to get the mutex lock so that they can execute.

## What is the problem with GIL ?
Generally, If your CPU have multiple cores then you can run multiple threads parallely. but GIL doesn't allow that because to make python easy to understand and write code python uses refference counting for memory management.<br>
python keeps track of all refferences pointing to a object in a variable. whenever the refference count is 0 for a particular object then python removes that object from the memory, that's how python manages memory.
</br>Example:
```python
a = "hello"
b = a
```
Here you can see the refference count for String object `"hello"` is 2 pointing by `a` and `b`.<br>
Now assume GIL allowed to run multiple threads at the same time then race conditions will happen because more than one thread will be accessing and modifying memory at the same time which can lead to unexpected behaviour and even program will crash and something bad can happen, to avoid this GIL exist in python.
<br>
Python is their from long time when operating system doesn't even know about threads that's why GIL is included in python, but now in this modern world with multi core cpus where we can run one thread on one cpu core achieving parallelism and to do that we need a way to make python faster for multithreaded programs.<br>
So to make python future proof and more resilient community is working on to remove GIL, for now in 3.13 they introduced experimental feature where devopers can test it in their enviornment.

## How to install python 3.13t in ubuntu ?
Run this commands one by one on your terminal.
```bash
sudo add-apt-repository ppa:deadsnakes
sudo apt-get update
sudo apt-get install python3.13-nogil
```
You can verify your build of CPython itself has the GIL disabled with the following incantation:
```bash
python -VV
```
If you are using Python 3.13b1 or newer, you should see a message like:
```bash
Python 3.13.0b1+ experimental free-threading build (heads/3.13:d93c4f9, May 21 2024, 10:54:14) [Clang 15.0.0 (clang-1500.1.0.2.5)]
```
Verify that the GIL is disabled at runtime with the following command:
```bash
python -c "import sys; print(sys._is_gil_enabled())"
```
if you see the output `False` then you are good to go.

## How can I compare multithreading with GIL and without GIL version ?
Clone this repository with the command :
```bash
git clone https://github.com/ratnapalshende/multithreading-experiments.git
```

```bash
cd multithreading-experiments
```
Run `test.py` with the python version 3.12 or anything you have installed on your machine other than 3.13t.
```bash
python3 test.py
```
Now run `test.py` with the GIL disabled version 3.13t :
```bash
python3.13t test.py
```

### 🛠️ How does it impact performance?
Here’s a comparison based on benchmarks:

| **Scenario**           | **Python 3.12 (With GIL)** | **Python 3.13 (Without GIL)** |
|-------------------------|---------------------------|-------------------------------|
| Single-threaded         | ~3.26 seconds            | ~2.97 seconds                |
| Multi-threaded | ~3.28 seconds            | ~1.04 seconds                |

## Resources 
- [Installing GIL free python](https://py-free-threading.github.io/installing_cpython/)
- [How GIL works in python?](https://www.dabeaz.com/python/GIL.pdf)
- [Official Release](https://docs.python.org/3.13/whatsnew/3.13.html#free-threaded-cpython)
- [PEP 703 – Making the Global Interpreter Lock Optional in CPython](https://peps.python.org/pep-0703/)
