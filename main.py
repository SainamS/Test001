# main.py
import myfunc

# รับค่าจากผู้ใช้
A = float(input("กรอกค่า A: "))
B = float(input("กรอกค่า B: "))

# เรียกใช้ฟังก์ชันจาก myfunc
ผลลัพธ์ = myfunc.add_numbers(A, B)

# แสดงผลลัพธ์
print("ผลลัพธ์ของ A + B =", ผลลัพธ์)
