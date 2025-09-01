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
        """
        Initializes the SuperstoreDashboardApp class, setting up the main application components.
        """
        self.root = tb.Window()
        self.df = load_data()
        self.visualizations = Visualizations(self.df)
        self.dashboard = Dashboard(self.root)
        
        # Control panel configuration
        self.dashboard.add_control_panel(self.update_visualizations)
        
        self.update_visualizations()  # Initial visualization update
        
    def update_visualizations(self):
        """
        Updates the visualizations in the dashboard based on the current filter selections.
        """
        filters = self.dashboard.get_filters()
        
        # Create and add visualizations
        sales_fig = self.visualizations.create_sales_profit_trend(
            filters['category'], filters['year']
            )
        self.dashboard.add_chart(sales_fig, 'sales trend', "Sales and Profit Trend")
        
        category_fig = self.visualizations.create_category_analysis(filters['year'])
        self.dashboard.add_chart(category_fig, 'category analysis', "Analysis by Category")
        
        region_fig = self.visualizations.create_regional_analysis(
            filters['category'], filters['year']
        )
        self.dashboard.add_chart(region_fig, 'regional_analysis', "Regional Analysis")
        
        segment_fig = self.visualizations.create_segment_analysis(filters['year'])
        self.dashboard.add_chart(segment_fig, 'segment_analysis', "Segment Analysis")
        
    def run(self):
        """
        Starts the main application loop.
        """
        self.root.mainloop()
        
if __name__ == "__main__":
    app = SuperstoreDashboardApp()
    app.run()
        