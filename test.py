from time import perf_counter
import threading
import sys

no_of_workers = 6

print(f"{sys.version}")

def factorial(n):
    total = 1
    for i in range(1, n+1):
        total *=i
    
    return total 

# single threaded
start = perf_counter()
for i in range(no_of_workers):
    factorial(50000)
end = perf_counter()

print("_"*50)
print(f"single thread : {end - start} seconds")

# multi threaded
start = perf_counter()
threads = []
for i in range(no_of_workers):
    t = threading.Thread(target=factorial, args=[50000])
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"multi thread : {perf_counter() - start} seconds")
print("_"*50)
