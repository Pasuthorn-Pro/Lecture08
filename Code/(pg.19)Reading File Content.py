#Using with statement to open and close a file.
with open("example.txt", "r") as file:
    contents = file.read()
    print(contents)
#ไม่ต้องใช้คำสั่ง close() ในการปิดไฟล์