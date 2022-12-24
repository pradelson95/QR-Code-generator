import webbrowser
from tkinter import *
from tkinter import messagebox
import qrcode
import os

window = Tk()
window.title("My App")
window.geometry("1000x700")
window.configure(background="gray")
window.resizable(False, False)


def help():
    webbrowser.open("https://github.com/pradelson95/QR-Code-generator")


def temp_text_2(e):
    ImageQrCodeName.delete(0, END)


def temp_text(e):
    QrCodelink.delete(0, END)


# dentro de esta funcion se genera el codigo QR al presionar el boton
def save_qr_code_img():
    global ImageQrCodeName
    link = QrCodelink.get()
    save_img_as = ImageQrCodeName.get()

    # mostrar un mensaje de error si el usuario deja los ambos campos vacios
    if link == "Paste your link here o text message" and save_img_as == "Image name":
        messagebox.showerror("Error", "Both fields are empty")
    # crear el codigo QR si los campos estan llenos
    else:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4
        )
        qr.add_data(link)
        qr.make(fit=True)
        set_image_property = qr.make_image(fill_color="black", back_color="red")
        s = set_image_property.save(save_img_as + ".png")

        # poner un texto en la interfaz que le dice al usuario donde esta ubicado la imagen del codigo QR
        Imgpath = Label(window, text=os.path.abspath(save_img_as + ".png"), font=("Arial", 22, "bold"), bg="gray",
                        fg="black")
        Imgpath.place(x=10, y=280)
        messagebox.showinfo("information", "The qr code was generated successfully and you can find it in the "
                                           "following path: " + os.path.abspath(save_img_as) + ".png")


# texto de bienvenida
labelQrCode = Label(window,
                    text="Welcome To Qr Code Generator",
                    font=("Arial", 29, "bold"),
                    fg="black",
                    bg="gray")
labelQrCode.place(x=250, y=50)

labelLink = Label(window,
                  text="Paste link",
                  font=("Arial", 20, "italic"),
                  background="gray",
                  foreground="black")
labelLink.place(x=10, y=130)

variable = StringVar()
ImageQrCodeName = Entry(window,
                        textvariable=variable,
                        width=20,
                        font=("Comic Sans", 18),
                        highlightbackground="black",
                        highlightthickness=2,
                        highlightcolor="black")
ImageQrCodeName.place(x=10, y=235)
ImageQrCodeName.insert(0, "Image name")  # dejar un texto por defecto que le dice al usuario que poner
ImageQrCodeName.bind("<FocusIn>", temp_text_2)

variable2 = StringVar()
QrCodelink = Entry(window,
                   textvariable=variable2,
                   width=40,
                   font=("Comic Sans", 18),
                   highlightbackground="black",
                   highlightthickness=2,
                   highlightcolor="black",
                   border=0)
QrCodelink.insert(0, "Paste your link here o text message")
QrCodelink.bind("<FocusIn>", temp_text)
QrCodelink.place(x=10, y=180)

# boton para generar el codigo QR
ButtonGenerator = Button(window,
                         text="Generate QR Code",
                         font=("Arial", 19),
                         background="black",
                         foreground="red",
                         activebackground="black",
                         border=5,
                         command=save_qr_code_img)

ButtonGenerator.place(x=10, y=330)

Btn_image = Button(window,
                   text="Source Code Proyect",
                   font=("Arial", 19),
                   background="black",
                   foreground="red",
                   activeforeground="black",
                   border=5,
                   command=help)
Btn_image.place(x=295, y=331)

# Mostrar la interfaz hasta que el usuario desida cerrarlo
window.mainloop()
