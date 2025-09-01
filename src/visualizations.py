import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import pandas as pd
import numpy as np

class Visualizations:
    def __init__(self, df):
        """_summary_

        Args:
            df (_type_): _description_
        """
        self.df = df.copy()
        self.prepare_data()
        
        def prepare_data(self):
            """_summary_
            """
            # Convert dates
            self.df['Order Date'] = pd.to_datetime(self.df['Order Date'])
            self.df['Year'] = self.df['Order Date'].dt.year
            self.df['Month'] = self.df['Order Date'].dt.month
            
        def filter_data(self, category_filter = "Everything", year_filter = "Everything"):
            """_summary_

            Args:
                category_filter (str, optional): _description_. Defaults to "Everything".
                region_filter (str, optional): _description_. Defaults to "Everything".
            """
            filtered_df = self.df.copy()
            
            if category_filter != "Everything":
                filtered_df = filtered_df[filtered_df['Category'] == category_filter]
                
            if year_filter != "Everything":
                year = int(year_filter)
                filtered_df = filtered_df[filtered_df['Year'] == year_filter]
                
            return filtered_df