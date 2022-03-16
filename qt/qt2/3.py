file = open("test.txt", "r")
print(list(map(str.strip, file.readlines())))
file.close()

"""
file_w = open("test_w.txt", "w")
print("123", file=file_w)
print("456", file=file_w)
print("456", file=file_w)
print("456", file=file_w)
"""
with open("test_w.txt", "w") as file_w:
    print("123", file=file_w)
    print("456", file=file_w)
    print("456", file=file_w)
    print("456", file=file_w)
    print("123", file=file_w)
