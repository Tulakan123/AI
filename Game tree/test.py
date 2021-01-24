import tkinter as tk
from tkinter import *
root = tk.Tk()

#Title
root.title("GAME OF THE COIN LEADER")


greeting = tk.Label(text="ยินดีต้อนรับสู่เกมเติมเงิน") 
greeting.pack()

# Creaing Label
label1 = tk.Label(text="Player 1")
label1.place(x=160, y=20)

label2 = tk.Label(text="เลือกเหรียญที่คุณต้องการเติมเงิน")
label2.place(x=120, y=50)

label3 = tk.Label(text="AI")
label3.place(x=800, y=20)

label4 = tk.Label(text="How To Play : ให้สลับกันเติมเหรียญตามจำนวนปุ่มเหรียญที่กำหนดมาให้ตามใจต้องการ แล้วเมื่อใครต้องเหรียญครบเป็นจำนวน 10 บาท ผู้นั้นจะเป็นฝ่ายชนะโดยทันที")
label4.place(x=200, y=400)

# Creating Button
MyButton = Button(root, text="Exit", command=root.destroy)
MyButton.pack(pady=400)


# Canvas
canvas = tk.Canvas(root, height=200, width=1000 )
canvas.pack()





root.mainloop()

