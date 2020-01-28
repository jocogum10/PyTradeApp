"""
PyTradeApp - my trading application which has a risk management calculator and
            a PH stock viewer and filter using a provided CSV file.

# risk calculator
# stock viewer

CSV file source: reddit.com /r/phinvest: PH Stocks Financial Data.csv
"""

import csv, tkinter, math

class MainGUI(tkinter.Frame):
    def __init__(self, parent=None):
        tkinter.Frame.__init__(self, parent)
        self.root = parent
        self.root.title("Trading Application")
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.make_menu()
        
    def make_menu(self):
        my_frame = tkinter.Frame(self.root)
        my_frame.grid(row=0, column=0, sticky="nsew")
        # configure frame to be expandable
        my_frame.columnconfigure(0, weight=1)
        my_frame.rowconfigure(0, weight=1)
        my_frame.rowconfigure(1, weight=1)
        # widgets
        self.button1 = MyButton(my_frame, text="Risk Management Calculator", command=(lambda:self.calculator()))
        self.button2 = MyButton(my_frame, text="PH Stock Search", command=(lambda:self.stock_search()))
        
        self.button1.grid(row=0, column=0, sticky="nsew")
        self.button2.grid(row=1, column=0, sticky="nsew")
        
    def calculator(self):
        self.root.destroy()
        root = tkinter.Tk()
        window = CalculatorGUI(root)
        root.mainloop()
    
    def stock_search(self):
        self.root.destroy()
        root = tkinter.Tk()
        window = StockSearchGUI(root)
        root.mainloop()


class StockSearchGUI(tkinter.Frame):
    def __init__(self, parent=None):
        tkinter.Frame.__init__(self, parent)
        self.root = parent
        self.root.title("Trading Calculator")
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.make_menu()        # building the menu
        self.make_widgets()     # building the gui interface
    
    def make_menu(self):
        top = tkinter.Menu(self.root)
        self.root.config(menu=top)
        file = tkinter.Menu(top)
        file.add_command(label='Main Menu', command=(lambda: self.main_menu()), underline=0)
        file.add_command(label='Information', command=(lambda: self.information()), underline=0)
        file.add_command(label='Quit', command=(lambda: self.root.destroy()), underline=0)
        top.add_cascade(label='Menu', menu=file, underline=0)
        
    def main_menu(self):
        self.root.destroy()
        root = tkinter.Tk()
        window = MainGUI(root)
        root.mainloop()
        
    def make_widgets(self):
        my_frame = tkinter.Frame(self.root)
        my_frame.grid(row=0, column=0, sticky="nsew")
        # configure frame to be expandable
        my_frame.columnconfigure(0, weight=1)
        my_frame.columnconfigure(1, weight=1)
        my_frame.rowconfigure(0, weight=1)
        my_frame.rowconfigure(1, weight=1)
        # row 0 widgets
        self.button1 = MyButton(my_frame, text="View Stocks", command=(lambda: self.view_stocks()))
        self.button1.grid(row=0, columnspan=2, sticky="nsew")
        # row 1 widgets
        MyLabel(my_frame, text="Filter Stocks").grid(row=1, columnspan=2, sticky="nsew")
        # row 2 widgets
        self.button2 = MyButton(my_frame, text="Filter Stock", command=(lambda: self.filter_cap()))
        self.button2.grid(row=2, column=0, sticky="nsew")
        self.entry1 = MyEntry(my_frame, 'micro, small, mid, big')
        self.entry1.grid(row=2, column=1, sticky="nsew")
    
    def information(self):
        window = tkinter.Toplevel(self.root)
        window.title("Information")
        window.columnconfigure(0, weight=1)
        window.rowconfigure(0, weight=1) 
        text = MyScrolledText(window, height=15, width=100)
        text.grid(row=0, column=0, sticky="nsew")
        with open('info.txt') as file:
            for info in file:
                text.write(info)
                
    def view_stocks(self):
        window = tkinter.Toplevel(self.root)
        window.title("Information")
        window.columnconfigure(0, weight=1)
        window.rowconfigure(0, weight=1) 
        text = MyScrolledText(window,height=15, width=100)
        text.grid(row=0, column=0, sticky="nsew")
        with open('PH Stocks Financial Data.csv') as stock_list:
            stock_dictionary = csv.DictReader(stock_list)
            for stock in stock_dictionary:
                text.write("\n{0:>7s} - {1}".format(stock['CODE'], stock['COMPANY NAME']))
        
    def filter_cap(self):
        cap = self.entry1.get()
        window = tkinter.Toplevel(self.root)
        window.title("Information")
        window.columnconfigure(0, weight=1)
        window.rowconfigure(0, weight=1) 
        text = MyScrolledText(window,height=15, width=100)
        text.grid(row=0, column=0, sticky="nsew")
        if cap == 'micro':
            lower_val = 0
            higher_val = 10000000000
        elif cap == 'small':
            lower_val = 10000000000
            higher_val = 40000000000
        elif cap == 'mid':
            lower_val = 40000000000
            higher_val = 100000000000
        elif cap == 'big':
            lower_val = 100000000000
            higher_val = float('inf')
    
        with open('PH Stocks Financial Data.csv') as stock_list:
            stock_dictionary = csv.DictReader(stock_list)
            for stock in stock_dictionary:
                if int(stock['MARKET CAPITALIZATION'].replace(',','')) < higher_val and int(stock['MARKET CAPITALIZATION'].replace(',','')) > lower_val:
                    text.write("{0:>7s} - {1}".format(stock['CODE'], stock['COMPANY NAME']))


class CalculatorGUI(tkinter.Frame):
    def __init__(self, parent=None):
        tkinter.Frame.__init__(self, parent)
        self.root = parent
        self.root.title("Trading Calculator")
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.make_menu()        # building the menu
        self.make_widgets()     # building the gui interface
    
    def make_widgets(self):
        my_frame = tkinter.Frame(self.root)
        my_frame.grid(row=0, column=0, sticky="nsew")
        # configure frame to be expandable
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
        # column 0 widgets
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
        # column 1 widgets
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
        # bottom side widgets
        self.button1 = MyButton(my_frame, text="Calculate", command=self.calculate)
        self.button2 = MyButton(my_frame, text="Save to File", command=self.save_to_file)
        self.button1.grid(row=10, columnspan=2, sticky="nsew")
        self.button2.grid(row=11, columnspan=2, sticky="nsew")
    
    def make_menu(self):
        top = tkinter.Menu(self.root)
        self.root.config(menu=top)
        file = tkinter.Menu(top)
        file.add_command(label='Main Menu', command=(lambda: self.main_menu()), underline=0)
        file.add_command(label='Information', command=(lambda: self.information()), underline=0)
        file.add_command(label='Quit', command=(lambda: self.root.destroy()), underline=0)
        top.add_cascade(label='Menu', menu=file, underline=0)
    
    def main_menu(self):
        self.root.destroy()
        root = tkinter.Tk()
        window = MainGUI(root)
        root.mainloop()
    
    def calculate(self):
        # data formatting
        capital = float(self.entry1.get().replace('PHP', '').replace(',',''))
        percentage = float(self.entry2.get().replace('%',''))/100.00
        cut_loss_percentage = float(self.entry5.get().replace('%',''))/100.00
        entry_price = float(self.entry6.get())
        board_lot = int(self.entry7.get())
        # data calculation
        amount_to_risk = capital * percentage
        amount_to_trade = amount_to_risk / cut_loss_percentage
        shares_to_buy = math.floor((amount_to_trade / entry_price)/board_lot)*board_lot
        capital_invested = shares_to_buy * entry_price
        # data printing
        self.entry3.clear()
        self.entry3.write("PHP {0:,.2f}".format(amount_to_risk))
        self.entry8.clear()
        self.entry8.write("PHP {0:,.2f}".format(amount_to_trade))
        self.entry9.clear()
        self.entry9.write("{0:,}".format(shares_to_buy))
        self.entry10.clear()
        self.entry10.write("{0:,.2f}".format(capital_invested))
    
    def save_to_file(self):
        pass
    
    def information(self):
        window = tkinter.Toplevel(self.root)
        window.title("Information")
        window.columnconfigure(0, weight=1)
        window.rowconfigure(0, weight=1) 
        text = MyScrolledText(window, height=15, width=100)
        text.grid(row=0, column=0, sticky="nsew")
        with open('info.txt') as file:
            for info in file:
                text.write(info)
  
  
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
        
class MyScrolledText(tkinter.Frame):
    def __init__(self, parent=None, text='', height=0, width=0, **config):
        tkinter.Frame.__init__(self, parent, **config)
        self.grid(sticky="nsew")
        sbar = tkinter.Scrollbar(self)
        self.height = height
        self.width = width
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        text = tkinter.Text(self, relief="sunken", height=self.height, width=self.width)
        sbar.config(command=text.yview)
        text.config(yscrollcommand=sbar.set)
        sbar.grid(row=0, column=1, sticky="nsew")
        text.grid(row=0, column=0, sticky="nsew")
        text.rowconfigure(0, weight=1)
        text.columnconfigure(0, weight=1)
        self.text = text
        
    def write(self, text):
        self.text.insert("end", str("\n"+text))
        self.text.see("end")
        self.text.update()
        
    def clear(self):
        self.text.delete("1.0", "end")
        self.text.update()


if __name__ == '__main__':
    root = tkinter.Tk()
    window = MainGUI(root)
    root.mainloop()