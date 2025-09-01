import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import pandas as pd
import numpy as np

class Visualizations:
    def __init__(self, df):
        """
        Initializes the Visualizations class with the provided DataFrame.

        Args:
            df (pd.DataFrame): The DataFrame containing the dataset to be used for generating visualizations.
        """
        self.df = df.copy()
        self.prepare_data()
        
        def prepare_data(self):
            """
            Prepares the data for analysis by adding necessary columns and formatting.
            """
            # Convert dates
            self.df['Order Date'] = pd.to_datetime(self.df['Order Date'])
            self.df['Year'] = self.df['Order Date'].dt.year
            self.df['Month'] = self.df['Order Date'].dt.month
            
        def filter_data(self, category_filter = "Everything", year_filter = "Everything"):
            """
            Filters the DataFrame based on the provided category and year filters.

            Args:
                category_filter (str, optional): Category to filter by. Defaults to "Everything".
                region_filter (str, optional): Year to filter by. Defaults to "Everything".
                
            Returns:
                pd.DataFrame: The filtered DataFrame according the selected filters.
            """
            filtered_df = self.df.copy()
            
            if category_filter != "Everything":
                filtered_df = filtered_df[filtered_df['Category'] == category_filter]
                
            if year_filter != "Everything":
                year = int(year_filter)
                filtered_df = filtered_df[filtered_df['Year'] == year_filter]
                
            return filtered_df
        
        def create_sales_profit_trend(self, category_filter = "Everything", year_filter = "Everything"):
            """
            Creates a line chart showing the sales and profit trend over time.

            Args:
                category_filter (str, optional): Category to filter by. Defaults to "Everything".
                year_filter (str, optional): Year to filter by. Defaults to "Everything".
            Returns:
                matplotlib.figure.Figure: The generated matplotlib figure.
            """
            filtered_df = self.filter_data(category_filter, year_filter)
            
            # Data preparation
            monthly_data = filtered_df.groupby(filtered_df['Order Date'].dt.to_period('M')).agg({
                'Sales': 'sum', 
                'Profit': 'sum'
                }).reset_index()
            monthly_data['Order Date'] = monthly_data['Order Date'].dt.to_timestamp()
            
            # Plotting
            fig, ax = plt.subplots(figsize = (6, 4))
            ax.plot(monthly_data['Order Date'], monthly_data['Sales'], label = 'Ventas', linewidth = 2)
            ax.plot(monthly_data['Order Date'], monthly_data['Profit'], label = 'Beneficio', linewidth = 2)
            
            # Formatting axis
            ax.yaxis.set_major_locator(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))
            plt.xticks(rotation = 45)
            plt.tight_layout()
            
            return fig

        def create_category_analysis(self, year_filter = "Everything"):
            """
            Creates a bar chart showing sales and profit by category for a selected year.

            Args:
                year_filter (str, optional): Year to filter by. Defaults to "Everything".

            Returns:
                matplotlib.figure.Figure: The generated matplotlib figure.
            """
            filtered_df = self.filter_data("Everything", year_filter)
            
            # Data preparation
            category_data = filtered_df.groupby('Category').agg({
                'Sales': 'sum', 
                'Profit': 'sum'
                }).reset_index()
            
            # Plotting
            fig, ax = plt.subplots(figsize = (6, 4))
            x = np.arange(len(category_data['Category']))
            width = 0.35
            
            ax.bar(x - width / 2, category_data['Sales'], width, label = 'Sales', alpha = 0.8)
            ax.bar(x + width / 2, category_data['Profit'], width, label = 'Profit', alpha = 0.8)
            
            ax.set_title('Sales and Profit pe Category')
            ax.set_xlabel('Category')
            ax.set_ylabel('Amount ($)')
            ax.set_xticks(x)
            ax.set_xticklabels(category_data['Category'])
            ax.legend()
            ax.grid(True, alpha = 0.3)
            
            # Formatting y-axis
            ax.yaxis.set_major_locator(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))
            plt.tight_layout()
            
            return fig
        
        def create_regional_analysis(self, category_filter = "Everything", year_filter = "Everything"):
            """
            Creates a bar chart showing sales by region.

            Args:
                category_filter (str, optional): Category to filter by. Defaults to "Everything".
                year_filter (str, optional): Year to filter by. Defaults to "Everything".

            Returns:
                matplotlib.figure.Figure: The generated matplotlib figure.
            """
            filtered_df = self.filter_data(category_filter, year_filter)
            
            # Data preparation
            region_data = filtered_df.groupby('Region').agg({
                'Sales': 'sum', 
                'Profit': 'sum'
                }).reset_index()
            
            # Plotting
            fig, ax = plt.subplots(figsize = (6, 4))
            ax.bar(region_data['Region'], region_data['Sales'], alpha=0.7, 
               color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
            
            ax.set_title('Sales by Region')
            ax.set_xlabel('Region')
            ax.set_ylabel('Sales ($)')
            
            # Formatting y-axis
            ax.yaxis.set_major_locator(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))
            plt.xticks(rotation = 45)
            plt.tight_layout()
            
            return fig
        
        def create_segment_analysis(self, category_filter = "Everything", year_filter = "Everything"):
            """
            Creates a pie chart and bar chart showing sales and unique customers by segment.

            Args:
                category_filter (str, optional): Category to filter by. Defaults to "Everything".
                year_filter (str, optional): Year to filter by. Defaults to "Everything".

            Returns:
                matplotlib.figure.Figure: The generated matplotlib figure.
            """
            filtered_df = self.filter_data(category_filter, year_filter)
            
            # Data preparation
            segment_data = filtered_df.groupby('Segment').agg({
                'Sales': 'sum', 
                'Profit': 'sum',
                'Customer ID': 'nunique'
                }).reset_index()
            
            # Plotting
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (10, 4))
            
            # Sales graphic
            ax1.pie(segment_data['Sales'], labels = segment_data['Segment'], autopct = '%1.1f%%')
            ax1.set_title('Sales by Segment')
            
            # Clients graphic
            ax2.bar(segment_data['Segment'], segment_data['Segment ID'],
                    color = ['#1f77b4', '#ff7f0e', '#2ca02c'])
            ax2.set_title('Unique Customers by Segment')
            ax2.set_xlabel('Number of Customers')
            plt.xticks(rotation = 45)
            
            plt.tight_layout()
            
            return fig
            
            