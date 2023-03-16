f = "example.txt"
cnt = 0
with open(f, "r") as file:
    for line in file:
        cnt += 1
print("Number of lines in", f, ":", cnt)
