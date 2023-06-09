from PIL import Image
from tkinter import StringVar
import customtkinter
import shutil
import os
import random


def start():
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("dark-blue")
    root = customtkinter.CTk()
    root.geometry("300x400")
    root.title("Totem to Skin")
    root.after(0, lambda :root.iconbitmap("totem_skin.ico"))
    name_en = StringVar()
    name_es = StringVar()
    edition = StringVar()
    res = Image.new('RGBA', (16,16))
    #initializeui()

    def getpixelcolor(i, x, y):
        img = i
        r,g,b,a = img.getpixel((x,y))
        c=(r,g,b,a)
        return c

    def colortransformed(r,g,b,a,r2,g2,b2):
        r3 = round(((1-(a/255))*r2) + ((a/255)*r))
        g3 = round(((1-(a/255))*g2) + ((a/255)*g))
        b3 = round(((1-(a/255))*b2) + ((a/255)*b))
        return (r3, g3, b3, 255)

    def gethead(skin):
        for x in range(8):
            for y in range(8):
                px = x+8
                py = y+8
                p = getpixelcolor(skin,px,py)
                if(not ((y==0 and x == 0) or (y==0 and x==7))):
                    res.putpixel((x+4,y+1), p)
        for x in range(8):
            for y in range(8):
                px = x+40
                py = y+8
                p = getpixelcolor(skin,px,py)
                f = getpixelcolor(res, x+4, y+1)
                if(not ((y==0 and x == 0) or (y==0 and x==7))):
                    if(p[3] == 255):
                        res.putpixel((x+4,y+1), p)
                    elif(p[3] < 255 and p[3] > 0):
                        color = colortransformed(p[0], p[1], p[2], p[3], f[0], f[1], f[2])
                        res.putpixel((x+4, y+1), color)
                
    def getbody(skin):
        for x in range(8):
            for y in range(4):
                px = x+20
                py = y*3+20
                p = getpixelcolor(skin,px,py)
                res.putpixel((x+4,y+9), p)
        for x in range(8):
            for y in range(4):
                px = x+20
                py = y*3+36
                p = getpixelcolor(skin,px,py)
                f = getpixelcolor(res, x+4, y+9)
                if(p[3] == 255):
                    res.putpixel((x+4,y+9), p)
                elif(p[3] < 255 and p[3] > 0):
                    color = colortransformed(p[0], p[1], p[2], p[3], f[0], f[1], f[2])
                    res.putpixel((x+4, y+9), color)
                        
    def getarms(skin, side, style):
        if side == 'L':
            if style == 'S':
                for x in range(3):
                    for y in range(3):
                        px = x+44
                        py = y*4+20
                        p = getpixelcolor(skin,px,py)
                        if (3-y, x+9) != (1,11):
                            res.putpixel((3-y,x+9), p)
                for x in range(3):
                    for y in range(3):
                        px = x+44
                        py = y*4+36
                        p = getpixelcolor(skin,px,py)
                        f = getpixelcolor(res, 3-y, x+9)
                        if (3-y, x+9) != (1,11):
                            if(p[3] == 255):
                                res.putpixel((3-y,x+9), p)
                        elif(p[3] < 255 and p[3] > 0):
                            color = colortransformed(p[0], p[1], p[2], p[3], f[0], f[1], f[2])
                            res.putpixel((3-y,x+9), color)
            if style == 'L':
                for x in range(4):
                    for y in range(3):
                        px = x+44
                        py = y*4+20
                        p = getpixelcolor(skin,px,py)
                        if (3-y, x+9) != (1,11):
                            res.putpixel((3-y,x+9), p)
                for x in range(4):
                    for y in range(3):
                        px = x+44
                        py = y*4+36
                        p = getpixelcolor(skin,px,py)
                        f = getpixelcolor(res, 3-y, x+9)
                        if (3-y, x+9) != (1,11):
                            if(p[3] == 255):
                                res.putpixel((3-y,x+9), p)
                            elif(p[3] < 255 and p[3] > 0):
                                color = colortransformed(p[0], p[1], p[2], p[3], f[0], f[1], f[2])
                                res.putpixel((3-y,x+9), color)
        if side == 'R':
            if style == 'S':
                for x in range(3):
                    for y in range(3):
                        px = x+36
                        py = y*4+52
                        p = getpixelcolor(skin,px,py)
                        if (y+12, x+9) != (14,11):
                            res.putpixel((y+12,x+9), p)
                for x in range(3):
                    for y in range(3):
                        px = x+52
                        py = y*4+52
                        p = getpixelcolor(skin,px,py)
                        f = getpixelcolor(res, y+3, x+9)
                        if (y+12, x+9) != (14,11):
                            if(p[3] == 255):
                                res.putpixel((y+12,x+9), p)
                            elif(p[3] < 255 and p[3] > 0):
                                color = colortransformed(p[0], p[1], p[2], p[3], f[0], f[1], f[2])
                                res.putpixel((y+12,x+9), color)
                        
    def getlegs(skin):
        for x in range(3):
            for y in range(2):
                px = x+5
                py = y*4+20
                p = getpixelcolor(skin,px,py)
                res.putpixel((x+5,y+13), p)
        for x in range(3):
            for y in range(2):
                px = x+20
                py = y*4+52
                p = getpixelcolor(skin,px,py)
                res.putpixel((x+8,y+13), p)
        for x in range(3):
            for y in range(2):
                px = x+5
                py = y*4+36
                p = getpixelcolor(skin,px,py)
                f = getpixelcolor(res, x+5, y+13)
                if(p[3] == 255):
                    res.putpixel((x+5,y+13), p)
                elif(p[3] < 255 and p[3] > 0):
                    color = colortransformed(p[0], p[1], p[2], p[3], f[0], f[1], f[2])
                    res.putpixel((x+5, y+13), color)
        for x in range(3):
            for y in range(2):
                px = x+20
                py = y*4+52
                p = getpixelcolor(skin,px,py)
                f = getpixelcolor(res, x+8, y+13)
                if(p[3] == 255):
                    res.putpixel((x+8,y+13), p)
                elif(p[3] < 255 and p[3] > 0):
                    color = colortransformed(p[0], p[1], p[2], p[3], f[0], f[1], f[2])
                    res.putpixel((x+8, y+13), color)                      
    def getboots(skin):
        for x in range(2):
            for y in range(1):
                px = x+5
                py = y*4+31
                p = getpixelcolor(skin,px,py)
                res.putpixel((x+6,y+15), p)
        for x in range(2):
            for y in range(1):
                px = x+21
                py = y*4+63
                p = getpixelcolor(skin,px,py)
                res.putpixel((x+8,y+15), p)
        for x in range(2):
            for y in range(1):
                px = x+5
                py = y*4+31
                p = getpixelcolor(skin,px,py)
                f = getpixelcolor(res, x+6, y+15)
                if(p[3] == 255):
                    res.putpixel((x+6,y+15), p)
                elif(p[3] < 255 and p[3] > 0):
                    color = colortransformed(p[0], p[1], p[2], p[3], f[0], f[1], f[2])
                    res.putpixel((x+6, y+15), color)
        for x in range(2):
            for y in range(1):
                px = x+21
                py = y*4+63
                p = getpixelcolor(skin,px,py)
                f = getpixelcolor(res, x+8, y+15)
                if(p[3] == 255):
                    res.putpixel((x+8,y+15), p)
                elif(p[3] < 255 and p[3] > 0):
                    color = colortransformed(p[0], p[1], p[2], p[3], f[0], f[1], f[2])
                    res.putpixel((x+8, y+15), color)

    def maketotem(skin, style, ed):
        if ed == "Bedrock Edition":
            gethead(skin)
            getbody(skin)
            getarms(skin, 'L', style)
            getarms(skin, 'R', style)
            getlegs(skin)
            getboots(skin)
            en = open("Pack/texts/en_US.lang", "w", encoding="utf-8")
            es = open("Pack/texts/es_ES.lang", "w", encoding="utf-8")
            engb = open("Pack/texts/en_GB.lang", "w", encoding="utf-8")
            esmx = open("Pack/texts/es_MX.lang", "w", encoding="utf-8")
            en.write("item.totem.name="+name_en.get())
            es.write("item.totem.name="+name_es.get())
            engb.write("item.totem.name="+name_en.get())
            esmx.write("item.totem.name="+name_es.get())
            res.save("Pack/pack_icon.png")
            res.save("Pack/textures/items/totem.png")
            shutil.make_archive("totempack", "zip", "Pack")
            os.rename("totempack.zip", "Totem_Pack_"+str(random.randint(0, 9999))+".mcpack")
        if ed == "Java Edition":
            gethead(skin)
            getbody(skin)
            getarms(skin, 'L', style)
            getarms(skin, 'R', style)
            getlegs(skin)
            getboots(skin)
            res.save("Pack_2/pack.png")
            res.save("Pack_2/assets/minecraft/textures/item/totem_of_undying.png")
            shutil.make_archive("java_totempack", "zip", "Pack_2")
            os.rename("java_totempack.zip", "Java_Edition_Totem_Pack_"+str(random.randint(0, 9999))+".zip")

    def chooseskin():
        path = customtkinter.filedialog.askopenfilename()
        sk = Image.open(path).convert("RGBA")
        maketotem(sk, 'S', edition.get())


    frame = customtkinter.CTkFrame(master=root)
    frame.pack(padx=20, pady=20, fill="both", expand=True)
    label = customtkinter.CTkLabel(master=frame, text="Skin to Totem", font=("Roboto", 30))
    label.pack(padx=12, pady=12)
    ed_sel_label = customtkinter.CTkLabel(master=frame, text="Select edition")
    ed_sel_label.pack(pady=0)
    edition_select = customtkinter.CTkComboBox(master=frame, values=["Java Edition", "Bedrock Edition"], variable=edition)
    edition_select.pack(pady=10)
    en_label = customtkinter.CTkLabel(master=frame, text="English item name")
    en_label.pack(pady=0)
    text_en = customtkinter.CTkEntry(master=frame, placeholder_text="English name", textvariable=name_en)
    text_en.pack(pady=10)
    es_label = customtkinter.CTkLabel(master=frame, text="Spanish item name")
    es_label.pack(pady=0)
    text_es = customtkinter.CTkEntry(master=frame, placeholder_text="Spanish name", textvariable=name_es)
    text_es.pack(pady=10)
    skinButton = customtkinter.CTkButton(master=frame, text="Choose skin file", command=chooseskin)
    skinButton.pack(padx=12,pady=12)
    root.mainloop()
start()