from tkinter import *

root = Tk()

root.title("Coin Master")

# Creating a Lebel widget
Label1 = Label(root, text="!!!!!ยินดีต้อนรับสู่เกมเติมเงิน!!!!!",font=("Helvetica", 30))
Label2 = Label(root, text="<<<<<ได้เวลาสนุกแล้วสิ>>>>>>",font=("Helvetica", 30))
Label3 = Label(root, text="<<<<<<<<<<<<<<<<<<<Player>>>>>>>>>>>>>>>>>>>>>",font=("Helvetica", 12))
Label4 = Label(root, text="<<<<<<<<<<<<<<<<<<<<<AI>>>>>>>>>>>>>>>>>>>>>>>",font=("Helvetica", 12))
Label5 = Label(root, text="[[[COIN]]]",font=("Helvetica", 12))
Label6 = Label(root, text="[[[GOAL]]]",font=("Helvetica", 12))
Label7 = Label(root, text="==================================================",font=("Helvetica", 12))
Label8 = Label(root, text="How To Play : ให้สลับกันเติมเหรียญตามจำนวนปุ่มเหรียญที่กำหนดมาให้ตามใจต้องการ แล้วเมื่อผู้ใดเติมเหรียญครบเป็นจำนวน 10 บาท ผู้นั้นจะเป็นฝ่ายชนะโดยทันที",font=("Helvetica", 12))
Label9 = Label(root, text="10",font=("Helvetica", 30))

#Button
Button1 = Button(root , text="1 บาท", padx=50, pady=20, bg="Red",font=("Helvetica", 20))
Button2 = Button(root , text="2 บาท", padx=50, pady=20, bg="Green",font=("Helvetica", 20))
Button3 = Button(root , text="5 บาท", padx=50, pady=20, bg="Yellow",font=("Helvetica", 20))
Button4 = Button(root , text="Restart", padx=10, pady=10)
Button5 = Button(root , text="Exit", padx=10, pady=10, command=root.quit)

#Grid
Label1.grid(row=0, column=4)
Label2.grid(row=1, column=4)
Label3.grid(row=2, column=1)
Label4.grid(row=2, column=6)
Label5.grid(row=3, column=4)
Label6.grid(row=5, column=4)
Label7.grid(row=7, column=4)
Label8.grid(row=11, column=4)
Label9.grid(row=6, column=4)


Button1.grid(row=4, column=1)
Button2.grid(row=6, column=1)
Button3.grid(row=8, column=1)
Button4.grid(row=9, column=4)
Button5.grid(row=10, column=4)



root.mainloop()