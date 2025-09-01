"""
    Main module to run the dashboard application.
    It includes the main loop to keep the application running.
"""
import tkinter as tk
import ttkbootstrap as tb
from data_loader import load_data
from dashboard import Dashboard
from visualizations import Visualizations

class SuperstoreDashboardApp:
    def __init__(self):
        self.root = tb.Window(themename = "darkly")
    

