import time

print(time.time())  # in seconds from win beg time

def send_emails():
    for i in range(10000):
        pass

start = time.time()
send_emails()
end = time.time()
duration = end - start
print(duration)