student = ["An", "Binh", "Cuong", "Dung", "Ha"]
with open("data.txt", "w") as f:
    for s in student:
        f.write(s)
        f.write("\n")
with open("data.txt") as f:
    for line in f:
        print(line.strip())