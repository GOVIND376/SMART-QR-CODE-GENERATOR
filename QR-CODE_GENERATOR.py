import qrcode
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, messagebox


def generate_qr():
    data = entry_data.get().strip()
    if not data:
        messagebox.showwarning("Input Error","Please enter some data or URL")
        return

    qr = qrcode.QRCode(version=1,
                       box_size=12,
                       border=5)
    qr.add_data(data)
    qr.make(fit=True)

    img=qr.make_image(fill_color="orange",
                      back_color="white")
    img.save("temp_qr.png")

    qr_img = Image.open("temp_qr.png")
    qr_img = qr_img.resize((150,150))
    qr_photo = ImageTk.PhotoImage(qr_img)
    lbl_qr.config(image=qr_photo)
    lbl_qr.image = qr_photo
    messagebox.showinfo("Success","QR Code generated successfully")

def save_qr():
        file_path = filedialog.asksaveasfilename(defaultextension=".png",
            filetypes=[("PNG files","*.png"),("All files","*.*")])
        if file_path:
            qr = qrcode.make(entry_data.get())
            qr.save(file_path)
            messagebox.showinfo("saved",f"QR Code saved as {file_path}")
root = tk.Tk()
root.title("Smart QR Code Generator")
root.geometry("450x500")
root.resizable(False,False)
root.configure(bg="#00FFFF")

lbl_title = tk.Label(root,text="QR Code Generator", font=("Arial", 20 , "bold"),bg="#ffffff",fg="black")
lbl_title.pack(pady=20)

lbl_data = tk.Label(root , text="Enter text or URL :", bg="#00FFCC",fg="navy blue",font=("impact",14))
lbl_data.pack()
entry_data = tk.Entry(root, width=40 , font =("Arial",12,"bold") ) 
entry_data.pack(pady=5)

btn_generate = tk.Button(root,text="Generate QR",  command=generate_qr,font=("Arial",12,"bold"),bg="#061AFF",fg="white",width=15)
btn_generate.pack(pady=10)
btn_save = tk.Button(root,text="Save QR",
                     command=save_qr,font=("Arial",12,"bold"),bg="#FF00BF",fg="black",width=15)
btn_save.pack(pady=5)
lbl_qr = tk.Label(root, bg = "#f4f4f4")
lbl_qr.pack(pady=20)

lbl_footer = tk.Label(
    root,
    text="Developed by GOVIND",
    bg="#EAFF00",       # background color
    fg="#000000",       # text color (example: orange/red)
    font=("arial", 14, "bold italic")  # bold italic font
)
lbl_footer.pack(side="bottom", pady=10)


root.mainloop()