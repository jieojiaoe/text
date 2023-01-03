i = 0
while i < 10:
    f = open(f"E:/test/test{i}.txt", "w", encoding="UTF-8")
    f.write("hello world")
    i += 1


