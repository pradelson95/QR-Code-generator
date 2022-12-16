# Importamos las librerías necesarias
from tkinter import *
from tkinter import messagebox
import qrcode
import os

# Creamos la ventana principal de la aplicación con Tkinter
window = Tk()
window.title("My App")  # Establecemos el título de la ventana
window.geometry("1000x700")  # Establecemos el tamaño de la ventana
window.configure(background="gray")  # Establecemos el color de fondo de la ventana
window.resizable(False, False)  # Deshabilitamos la opción de redimensionar la ventana

# Creamos una función para eliminar el texto de placeholdet al hacer clic en el campo de nombre de la imagen del código QR
def temp_text_2(e):
    ImageQrCodeName.delete(0, END)

# Creamos una función para eliminar el texto de placeholdet al hacer clic en el campo de enlace del código QR
def temp_text(e):
    QrCodelink.delete(0, END)

# Creamos una función para generar y guardar el código QR cuando se hace clic en el botón
def save_qr_code_img():
    global ImageQrCodeName
    link = QrCodelink.get()  # Obtenemos el enlace o mensaje de texto ingresado por el usuario
    save_img_as = ImageQrCodeName.get()  # Obtenemos el nombre de la imagen ingresado por el usuario

    # Si ambos campos están vacíos, mostramos un mensaje de error
    if link == "" and ImageQrCodeName == "":
        messagebox.showerror("Error", "The link field is empty")
    # Si ambos campos están llenos, creamos el código QR
    else:
        # Creamos un objeto QR con qrcode y le asignamos algunas propiedades
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4
        )
        qr.add_data(link)  # Añadimos el enlace o mensaje de texto al objeto QR
        qr.make(fit=True)  # Creamos el código QR
        set_image_property = qr.make_image(fill_color="black", back_color="red")  # Establecemos algunas propiedades de la imagen
        s = set_image_property.save(save_img_as + ".png") 

        # poner un texto en la interfaz que le dice al usuario donde esta ubicado la imagen del codigo QR
        Imgpath = Label(window, text=os.path.abspath(save_img_as + ".png"), font=("Arial", 22, "bold"), bg="gray",
                        fg="black")
        Imgpath.place(x=10, y=280)
        messagebox.showinfo("information", "The qr code was generated successfully and you can find it in the following path: " + os.path.abspath(save_img_as) + ".png")

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
ImageQrCodeName.insert(0, "Image name")
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

window.mainloop()
