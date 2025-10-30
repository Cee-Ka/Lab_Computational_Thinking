x = float(input("Nhap tu so: "))
y = float(input("Nhap mau so: "))
try:
    print("Thuong: ", x/y)
except ZeroDivisionError:
    print("Division by zero")
except:
    print("An error occurred")