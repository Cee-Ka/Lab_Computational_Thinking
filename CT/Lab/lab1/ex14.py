def describe_person(*args, **kwargs):
    print("Thông tin cá nhân:")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")
    
    print("\nSở thích:")
    for hobby in args:
        print(f"  - {hobby}")

describe_person("đọc sách", "chạy bộ", "lập trình", name="An", age=25, city="HCM")
