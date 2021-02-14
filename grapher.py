import pandas as pd
import matplotlib.pyplot as plt

import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()

ROOT.withdraw()
# the input dialog

USER_INP = simpledialog.askstring(title="Company Name",
                                  prompt="What's ticker symbol of the company you want to look at? (AAPL, GOOG, GOOGL, TSLA, AMZN, MSFT")      
company = USER_INP

USER_INP = simpledialog.askstring(title="Start Date",
                                  prompt="What date do you want the stock graph to start?")
firstDate = USER_INP

USER_INP = simpledialog.askstring(title="End Date",
                                  prompt="What date do you want the stock graph to end?")
secondDate = USER_INP
