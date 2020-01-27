"""
my trading app.

# risk calculator
# stock viewer
"""
import csv
import tkinter

class MainGUI:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Trading")
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
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
        
        self.entry1 = MyEntry(my_frame, 'PHP 50,000.00', True)
        self.entry2 = MyEntry(my_frame, '1%', True)
        self.entry3 = MyEntry(my_frame, 'Amount to Risk')
        self.entry4 = MyEntry(my_frame, 'Stock Name', True)
        self.entry5 = MyEntry(my_frame, 'Cutloss Percentage', True)
        self.entry6 = MyEntry(my_frame, 'Entry Price', True)
        self.entry7 = MyEntry(my_frame, 'Board Lot', True)
        self.entry8 = MyEntry(my_frame, 'Amount to Trade')
        self.entry9 = MyEntry(my_frame, 'No. of Shares to Buy')
        
        self.entry1.grid(row=0, column=1, sticky="nsew")
        self.entry2.grid(row=1, column=1, sticky="nsew")
        self.entry3.grid(row=2, column=1, sticky="nsew")
        self.entry4.grid(row=3, column=1, sticky="nsew")
        self.entry5.grid(row=4, column=1, sticky="nsew")
        self.entry6.grid(row=5, column=1, sticky="nsew")
        self.entry7.grid(row=6, column=1, sticky="nsew")
        self.entry8.grid(row=7, column=1, sticky="nsew")
        self.entry9.grid(row=8, column=1, sticky="nsew")
        
        self.button1 = MyButton(my_frame, text="Calculate", command=self.calculate)
        self.button2 = MyButton(my_frame, text="Save to File", command=self.save_to_file)
        self.button1.grid(row=9, columnspan=2, sticky="nsew")
        self.button2.grid(row=10, columnspan=2, sticky="nsew")
    
    def calculate(self):
        pass
    
    def save_to_file(self):
        pass
        
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
    def __init__(self, parent=None, label='', active=False, **config):
        tkinter.Entry.__init__(self, parent, **config)
        self.grid(sticky="nsew", padx=10, pady=10)
        self.insert(0, label)
        if active:
            self.config(font=("courier", 10, "italic"))
        else:
            self.config(bg="light steel blue")
            self.config(font=("courier", 10, "bold"))
            
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
        higher_val = 10000000000000000000
    
    with open('PH Stocks Financial Data.csv') as stock_list:
        stock_dictionary = csv.DictReader(stock_list)
        for stock in stock_dictionary:
            if int(stock['MARKET CAPITALIZATION'].replace(',','')) < higher_val and int(stock['MARKET CAPITALIZATION'].replace(',','')) > lower_val:
                print(stock['CODE'], stock['COMPANY NAME'])
                
            
if __name__ == '__main__':
    MainGUI()