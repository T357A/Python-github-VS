import pandas as pd
import os
import sqlite3
import openpyxl as opx
import os

class Products:
    def __init__(self, Barcode, Size, Item, Location, Price, Quantity):
        self.Barcode = Barcode
        self.Item = Item
        self.Size = Size
        self.Location = Location
        self.Price = Price
        self.Quantity = Quantity

    def Barcode():
        pass
        #Barcode = input("Scan item to be counted")

    def Item(self):
        return self.Item

    def Dept_ID(self):
        return self.Dept_Id

    def Size(self):
        return self.Size
        pass

    # cannot and will been seen by inventory staff, only for the Entry app and reporting.
    def Price(self):
        pass

    def Quantity():
        pass
