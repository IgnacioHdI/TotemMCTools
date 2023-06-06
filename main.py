import customtkinter
from PIL import Image

import totem

def opentool():
    totem.start()

def initializeui():
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(padx=20, pady=20, fill="both", expand=True)

    i_totem = customtkinter.CTkImage(light_image=Image.open("Assets/totem_skin.png"),
                                     dark_image=Image.open("Assets/totem_skin.png"),
                                     size=(32,32))
    b_totem = customtkinter.CTkButton(master=frame, width=250, height=50, text="Skin to Totem", command=opentool, image=i_totem)
    b_totem.pack(padx=12, pady=15)

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")
root = customtkinter.CTk()
root.geometry("300x500")
root.title("Totem Minecraft Tools")
root.after(0, lambda :root.iconbitmap("totemtools.ico"))
initializeui()
root.mainloop()