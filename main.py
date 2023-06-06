import customtkinter
from PIL import Image
import random

import totem

def initializeui():
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(padx=20, pady=20, fill="both", expand=True)

    l_title = customtkinter.CTkLabel(master=frame, text="Totem Minecraft Tools", font=("Roboto", 30))
    l_title.pack(padx=12, pady=12)

    i_totem = customtkinter.CTkImage(light_image=Image.open("Assets/totem_skin.png"),
                                     dark_image=Image.open("Assets/totem_skin.png"),
                                     size=(32,32))
    b_totem = customtkinter.CTkButton(master=frame, width=350, height=50, text="Skin to Totem", command=totem.start, image=i_totem)
    b_totem.pack(padx=12, pady=15)


    b_exit = customtkinter.CTkButton(master=root, width=50, height=35, text="Quit", command=root.destroy)
    b_exit.pack(pady=10)


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")
root = customtkinter.CTk()
root.geometry("400x500")
root.title("Totem Minecraft Tools")
root.after(0, lambda :root.iconbitmap("totemtools.ico"))
initializeui()
root.mainloop()