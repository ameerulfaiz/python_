from sre_parse import State
import tkinter as tk
import CustomTkinter as ctk
import tkinter.messagebox
import math

ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

app =math.ctk()  # create CTk window like you do with the Tk window
app.geometry("400x240")

class Window_CheckOut(ctk.CTkToplevel):
    def __init__(self, text):
        super().__init__() 

        self.columnconfigure(0, minsize=100)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, minsize=100)
        middle_frame = ctk.CTkFrame(self, fg_color=self.fg_color)

        middle_frame.grid(row=0, column=1, sticky="ns", padx=20, pady=10)
        tajuk = ctk.CTkLabel(master=middle_frame, text="CHECKOUT", text_font=("Arial", 25))
        tajuk.grid(row=0, column=0, sticky="ew")

        self.receipt = tkinter.Text(master=middle_frame, highlightthickness=0, font=("Consolas", 27), height=5, width=40)
        self.receipt.grid(row=1, column=0, sticky="nsew", pady=15)
        self.receipt.insert(tkinter.END, text)

        self.bottom_frame = ctk.CTkFrame(self, fg_color=self.fg_color)
        button_1 = ctk.CTkButton(  master=self.bottom_frame, 
                                            fg_color = "light blue",
                                            text="Cash", width=200, height=60,
                                            text_font=("Arial", 25), pady=10, padx=10,
                                            text_color="black"
                                            )
        button_2 = ctk.CTkButton(  master=self.bottom_frame, 
                                            fg_color = "yellow",
                                            text="Debit", width=200, height=60,
                                            text_font=("Arial", 25), pady=10, padx=10,
                                            text_color="black")
        button_3 = ctk.CTkButton(  master=self.bottom_frame, 
                                            fg_color = "brown",
                                            text="HUTANG(555)", width=200, height=60,
                                            text_font=("Arial", 25), pady=10, padx=10,
                                            text_color="white")

        
        
        self.bottom_frame.grid(row=1, column=1)
        button_1.grid(row=0, column=0)         
        button_2.grid(row=0, column=1)                                         
        button_3.grid(row=0, column=2)



class Window_CustomerBayar(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()    

        self.total_harga = 0
        self.makanan_dict = {
            "Chicken Chop" : 20,
            "Nasi Lemak" : 17,
            "Nasi Goreng" : 15,
            "Roti Canai" : 15,
            "Kambing Golek":7,
            "Nasi USA" : 6.5,
            "Lamb Shank" : 50,
            "Sate" : 1.2,
            "Nasi Penyet":18,
            "Tomyam Campur":13
        }
        self.senarai_makanan = ""
        self.senarai_makanan_dict = dict()

        self.create_middle_frame().grid(row=0, column=1, sticky="ns", padx=20, pady=10)

        self.button_clear = ctk.CTkButton(  master=self, 
                                            fg_color = "green",
                                            text="Clear All", width=200, height=60,
                                            text_font=("Arial", 25), pady=10, padx=10,
                                            command = self.clearAll)            

        last_row, last_column = self.grid_size()
        self.button_clear.grid(row=last_row, column = 1)
        self.pay_button = ctk.CTkButton(  master=self, 
                                            fg_color = "green",
                                            text="Pay", width=200, height=60,
                                            text_font=("Arial", 25), pady=10, padx=10,
                                            command = self.open_pay_window)  
        self.pay_button.grid(row=last_row+1, column = 1)
    
    def open_pay_window(self):
        window = Window_CheckOut(self.text_purchase.get("1.0",'end-1c'))

    def create_left_frame(self):
        left_frame = ctk.CTkFrame(self)
        return left_frame

    def create_middle_frame(self):
        # ----------- MAIN FRAME -------------
        main_middle_frame = ctk.CTkFrame(self, fg_color=self.fg_color)
        main_middle_frame.rowconfigure(0, weight=1)
        main_middle_frame.rowconfigure(1, weight=1)
        main_middle_frame.columnconfigure(0, minsize=500)

        # ----------- TOP HALF OF MAIN FRAME -------------
        top_middle_frame = ctk.CTkFrame(master=main_middle_frame, fg_color=self.fg_color)
        top_middle_frame.grid(row=0, column=0, sticky="nsew")
        top_middle_frame.columnconfigure(0, weight=1)
        main_label = ctk.CTkLabel(master=top_middle_frame, text="Customer Bayar", text_font=("Consolas", 25))
        main_label.grid(row=0, column=0, sticky="ew")
        # Total Price Entry
        self.entry_total_price = ctk.CTkEntry(top_middle_frame, placeholder_text="Total Harga", text_font=("Arial", 30))
        self.entry_total_price.grid(row=1, column=0, sticky="ew")
        # List Of Food TextArea with scrollbar
        self.text_purchase = tkinter.Text(master=top_middle_frame, highlightthickness=0, font=("Consolas", 27), height=5, width=12)
        self.text_purchase.grid(row=2, column=0, sticky="nsew", pady=15)
        ctk_textbox_scrollbar = ctk.CTkScrollbar(master=top_middle_frame, command=self.text_purchase.yview, fg_color=self.fg_color, scrollbar_color="yellow")
        ctk_textbox_scrollbar.grid(row=2, column=0, sticky="ens")
        self.text_purchase.configure(yscrollcommand=ctk_textbox_scrollbar.set)

        # ----------- BOTTOM HALF OF MAIN FRAME -------------
        bottom_middle_frame = ctk.CTkFrame(master=main_middle_frame, fg_color=self.fg_color)
        bottom_middle_frame.grid(row=1, column=0)

        buttons_per_row = 2

        self.makanan_customer_dict = dict()
        self.total_harga = 0

        for index, food in enumerate(self.makanan_dict):
            harga = self.makanan_dict[food]
            row = math.floor(index/buttons_per_row)
            col = index%buttons_per_row*2
            button_food_name = ctk.CTkButton(master=bottom_middle_frame, 
                                             command= lambda harga=harga, food=food: self.kiraHargaMakanan(harga, food), 
                                             text=food, text_font=("Terminal", 25))
            button_food_name.grid(row=row, column=col, sticky="ew", padx=10, pady=10)
            button_minus = ctk.CTkButton(master=bottom_middle_frame, text_font=("Arial", 20), text="-", fg_color="red", width=10, height=0,
            command = lambda food=food, harga=harga: self.buang_satu_makanan(food, harga))
            button_minus.grid(row=row, column=col+1)

        return main_middle_frame

    def buang_satu_makanan(self, nama_makanan, harga_makanan):
        
        if nama_makanan not in self.makanan_customer_dict:
            return

        self.total_harga -= harga_makanan
        self.entry_total_price.delete(0, tkinter.END)
        self.entry_total_price.insert(0, "RM " + str(self.total_harga))

        if self.makanan_customer_dict[nama_makanan] == 1:
            self.makanan_customer_dict.pop(nama_makanan)
        else :
            self.makanan_customer_dict[nama_makanan] -= 1

        self.text_purchase.delete("1.0", tkinter.END)

        senarai_makanan_cantik = ""

        for food in self.makanan_customer_dict:
            bil = self.makanan_customer_dict[food]
            senarai_makanan_cantik += f"{food:<20} x{bil:>2}\n"

        self.text_purchase.insert(tkinter.END, senarai_makanan_cantik)

    def kiraHargaMakanan(self, harga_makanan, nama_makanan):

        self.total_harga += harga_makanan
        #self.total_harga += round(self.total_harga, 2)
        self.entry_total_price.delete(0, tkinter.END)
        self.entry_total_price.insert(0, "RM " + str(self.total_harga))

        if nama_makanan not in self.makanan_customer_dict:
            self.makanan_customer_dict[nama_makanan] = 1
        else:
            self.makanan_customer_dict[nama_makanan] += 1

        self.text_purchase.delete("1.0", tkinter.END)

        senarai_makanan_cantik = ""

        for food in self.makanan_customer_dict:
            bil = self.makanan_customer_dict[food]
            current_harga = round(self.makanan_dict[food]*bil, 2)
            senarai_makanan_cantik += f"{food:<20} x{bil:>2} (RM {current_harga})\n"

        self.text_purchase.insert(tkinter.END, senarai_makanan_cantik)
        
    def clearAll(self) :
        self.total_harga = 0
        self.entry_total_price.delete(0, tkinter.END)
        self.text_purchase.delete("1.0", tkinter.END)
        self.makanan_customer_dict.clear()

    def tambahHargaMakanan(self, harga_makanan, nama_makanan):

        self.total_harga += harga_makanan
        self.senarai_makanan += nama_makanan + "\n"
        if nama_makanan in self.senarai_makanan_dict:
            self.senarai_makanan_dict[nama_makanan] += 1
        else :
            self.senarai_makanan_dict[nama_makanan] = 1
        self.entry_harga_makanan.delete(0, tkinter.END)
        self.entry_harga_makanan.insert(0, self.total_harga)

        self.senarai_makanan = ""

        for food in self.senarai_makanan_dict:
            harga = self.senarai_makanan_dict[food]
            x = 'x'
            self.senarai_makanan += f'{food:<15}{x+str(harga):>6}\n'

        try:
            self.tk_textbox.delete("1.0", tkinter.END)
        except Exception as e:
            pass
        self.tk_textbox.insert(tkinter.END, self.senarai_makanan)
        # self.label_senarai_bayaran.configure(text=self.senarai_makanan)

class App(ctk.CTk):

    WIDTH = 800
    HEIGHT = 600

    def __init__(self):
        super().__init__()

        self.title("Cafe System")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        #self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        self.main_label = ctk.CTkLabel(master=self, text="CAFE SYSTEM", text_font=("Arial", 25))
        self.main_label.grid(row=0, column = 1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=9)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        button_1 = ctk.CTkButton(master=self, text="Bayar", width=200, height=60, text_font=("Arial", 25), command=Window_CustomerBayar)
        button_1.grid(row=1, column = 1)


if __name__ == "__main__":
    app = App()
    app.mainloop()