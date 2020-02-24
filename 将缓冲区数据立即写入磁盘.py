import time
fd = open("a.txt", "w")
i = 0
while 1:
    buf = "a\n"
    fd.write(buf)
    time.sleep(1)
    i = i + 1
    if i > 10:
        fd.close()
        break
    fd.flush()
