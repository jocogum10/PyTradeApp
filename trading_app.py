"""
my trading app.

# risk calculator
# stock viewer
"""
import csv, tkinter, math
class MainGUI:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Trading Risk Manager")
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.make_menu()
        self.make_widgets()
        self.root.mainloop()
        
    def make_widgets(self):
        my_frame = tkinter.Frame(self.root)
        my_frame.grid(row=0, column=0, sticky="nsew")
        
        my_frame.columnconfigure(1, weight=1)
        
        my_frame.rowconfigure(0, weight=1)
        my_frame.rowconfigure(1, weight=1)
        my_frame.rowconfigure(2, weight=1)
        my_frame.rowconfigure(3, weight=1)
        my_frame.rowconfigure(4, weight=1)
        my_frame.rowconfigure(5, weight=1)
        my_frame.rowconfigure(6, weight=1)
        my_frame.rowconfigure(7, weight=1)
        my_frame.rowconfigure(8, weight=1)
        my_frame.rowconfigure(9, weight=1)
        my_frame.rowconfigure(10, weight=1)
        
        MyLabel(my_frame, text="Capital").grid(row=0, column=0, sticky="nsew")
        MyLabel(my_frame, text="Risk Percentage").grid(row=1, column=0, sticky="nsew")
        MyLabel(my_frame, text="Amount to Risk").grid(row=2, column=0, sticky="nsew")
        MyLabel(my_frame, text="Stock Name").grid(row=3, column=0, sticky="nsew")
        MyLabel(my_frame, text="Cutloss Percentage").grid(row=4, column=0, sticky="nsew")
        MyLabel(my_frame, text="Entry Price").grid(row=5, column=0, sticky="nsew")
        MyLabel(my_frame, text="Board Lot").grid(row=6, column=0, sticky="nsew")
        MyLabel(my_frame, text="Amount to Trade").grid(row=7, column=0, sticky="nsew")
        MyLabel(my_frame, text="No. of Shares to Buy").grid(row=8, column=0, sticky="nsew")
        MyLabel(my_frame, text="Capital Invested").grid(row=9, column=0, sticky="nsew")
        
        self.entry1 = MyEntry(my_frame, 'PHP 50,000.00')
        self.entry2 = MyEntry(my_frame, '1%', )
        self.entry3 = MyText(my_frame)
        self.entry3.write('Amount to Risk')
        self.entry4 = MyEntry(my_frame, 'PSEI')
        self.entry5 = MyEntry(my_frame, '10%')
        self.entry6 = MyEntry(my_frame, '10')
        self.entry7 = MyEntry(my_frame, '100')
        self.entry8 = MyText(my_frame)
        self.entry8.write('Amount to Trade')
        self.entry9 = MyText(my_frame)
        self.entry9.write('No. of Shares to Buy')
        self.entry10 = MyText(my_frame)
        self.entry10.write('Capital Invested')
        
        self.entry1.grid(row=0, column=1, sticky="nsew")
        self.entry2.grid(row=1, column=1, sticky="nsew")
        self.entry3.grid(row=2, column=1, sticky="nsew")
        self.entry4.grid(row=3, column=1, sticky="nsew")
        self.entry5.grid(row=4, column=1, sticky="nsew")
        self.entry6.grid(row=5, column=1, sticky="nsew")
        self.entry7.grid(row=6, column=1, sticky="nsew")
        self.entry8.grid(row=7, column=1, sticky="nsew")
        self.entry9.grid(row=8, column=1, sticky="nsew")
        self.entry10.grid(row=9, column=1, sticky="nsew")
        
        self.button1 = MyButton(my_frame, text="Calculate", command=self.calculate)
        self.button2 = MyButton(my_frame, text="Save to File", command=self.save_to_file)
        self.button1.grid(row=10, columnspan=2, sticky="nsew")
        self.button2.grid(row=11, columnspan=2, sticky="nsew")
    
    def calculate(self):
        capital = float(self.entry1.get().replace('PHP', '').replace(',',''))
        percentage = float(self.entry2.get().replace('%',''))/100.00
        amount_to_risk = capital * percentage
        self.entry3.clear()
        self.entry3.write("PHP {0:,.2f}".format(amount_to_risk))
        
        cut_loss_percentage = float(self.entry5.get().replace('%',''))/100.00
        amount_to_trade = amount_to_risk / cut_loss_percentage
        self.entry8.clear()
        self.entry8.write("PHP {0:,.2f}".format(amount_to_trade))
        
        entry_price = float(self.entry6.get())
        board_lot = int(self.entry7.get())
        shares_to_buy = math.floor((amount_to_trade / entry_price)/board_lot)*board_lot
        self.entry9.clear()
        self.entry9.write("{0:,}".format(shares_to_buy))
        
        capital_invested = shares_to_buy * entry_price
        self.entry10.clear()
        self.entry10.write("{0:,.2f}".format(capital_invested))
    
    def save_to_file(self):
        pass
    
    def information(self):
        window = tkinter.Toplevel(self.root)
        window.title("Information")
        window.resizable(0,0)
        text = MyText(window)
        text.grid(row=0, column=0)
        text.config(height=20, width=30)
        with open('info.txt') as file:
            for info in file:
                text.write(info)
        
        
    def make_menu(self):
        top = tkinter.Menu(self.root)
        self.root.config(menu=top)
        file = tkinter.Menu(top)
        file.add_command(label='Information', command=(lambda: self.information()), underline=0)
        file.add_command(label='Quit', command=(lambda: self.root.destroy()), underline=0)
        top.add_cascade(label='Menu', menu=file, underline=0)
        
class MyLabel(tkinter.Label):
    def __init__(self, parent=None, **config):
        tkinter.Label.__init__(self, parent, **config)
        self.grid(sticky="nsew")
        self.config(font=("courier", 10, "bold"))
        
class MyButton(tkinter.Button):
    def __init__(self, parent=None, **config):
        tkinter.Button.__init__(self, parent, **config)
        self.grid(sticky="nsew", padx=10, pady=10)
        self.config(bg="steel blue")
        self.config(font=("courier", 10, "bold"))
    
class MyEntry(tkinter.Entry):
    def __init__(self, parent=None, label='', **config):
        tkinter.Entry.__init__(self, parent, **config)
        self.grid(sticky="nsew", padx=10, pady=10)
        self.insert(0, label)
        self.config(font=("courier", 10, "italic"))
        self.config(bg="light steel blue")
            
class MyText(tkinter.Text):
    def __init__(self, parent=None, **config):
        tkinter.Text.__init__(self, parent, **config)
        self.grid(sticky="ne", padx=10, pady=10)
        self.config(relief="sunken", height=1, width=15)
    
    def write(self, text):
        self.insert("end", text)
        self.see("end")
        self.update()
        
    def clear(self):
        self.delete("1.0", "end")
        self.update()
           
           
def filter_cap(cap):
    if cap == 'micro cap':
        lower_val = 0
        higher_val = 10000000000
    elif cap == 'small cap':
        lower_val = 10000000000
        higher_val = 40000000000
    elif cap == 'mid cap':
        lower_val = 40000000000
        higher_val = 100000000000
    elif cap == 'big cap':
        lower_val = 100000000000
        higher_val = float('inf')
    
    with open('PH Stocks Financial Data.csv') as stock_list:
        stock_dictionary = csv.DictReader(stock_list)
        for stock in stock_dictionary:
            if int(stock['MARKET CAPITALIZATION'].replace(',','')) < higher_val and int(stock['MARKET CAPITALIZATION'].replace(',','')) > lower_val:
                print(stock['CODE'], stock['COMPANY NAME'])
                
            
if __name__ == '__main__':
    MainGUI()