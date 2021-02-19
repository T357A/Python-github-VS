import openpyxl as opx
import sqlite3
import pandas as pd
import PyQt6


def New_Item(self, Barcode, Item, Size, Price, Dept_Id, Quantity):
    def __init__(self, Barcode, Size, Item, Location, Price, Quantity):
        self.Barcode = Barcode
        self.Item = Item
        self.Size = Size
        self.Price = Price
        self.Dept_Id = Dept_Id
        self.Quantity = Quantity

    def Barcode():
        pass
 #      Barcode = input('Scan NEW item to be added to the inventory: ')

    def Item():
        pass
#        Item = input('Item description being added to the inventory: ')

    def Size():
        pass
#        Size = input('Please indicate the size/weight or amount of the item')
#       Is there an information window that the above information can be put in?

    def Dept_Id():
        pass
        Is_It_New = input()
        if Is_It_New is Y or y:
            New_Dept = str(input('What is the new department called? :'))
        else:
            pass

    def Price():
        pass
#        Price = float(input('Please add the price of the item: $'))

    def Quantity():
        pass
        qty = input('Would you like to add a count to this entry?: (Y/N)')
        if qty is Y or y:
            quantity = (int('Please enter the amount: '))
        else:
            pass  # Need to decide if loop back to more input or break I.E. If N or N
