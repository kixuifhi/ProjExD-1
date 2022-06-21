import tkinter as tk
import tkinter.messagebox as tkm
def button_click(event):
    btn = event.widget
    num = btn["text"]
    entry.insert(tk.END, num)
    #tkm.showinfo("", f"{num}のボタンがクリックされました")
if __name__ == "__main__":

    
    r,c = 1, 0
    root = tk.Tk()
    root.title("超高機能電卓")
    root.geometry("300x500")

    entry = tk.Entry(root, justify="right",width=10,font=("Times New Roman",40))
    entry.grid(row=0,column=0,columnspan=3)
    for num in range(9, -1, -1):
        btn = tk.Button(root,text=f"{num}",width=4,height=2,font=("Times New Roman", 30))
        btn.bind("<1>", button_click)
        btn.grid(row=r,column=c)
        c+=1
        if (num-1)%3 == 0:
            r += 1
            c = 0



    root.mainloop()
        