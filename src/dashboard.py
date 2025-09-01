import tkinter as tk
import ttkbootstrap as tb
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 

class Dashboard:
    def __init__(self, root):
        """
        Initializes the Dashboard class and sets up the main user interface.

        Args:
            root (tk.Tk or tb.Window): The main application window where the dashboard will be displayed.
        """
        self.root = root
        self.style = tb.Style("darkly")
        self.setup_ui()
    
    # UI configuration
    def setup_ui(self):
        """
        Configures the main user interface of the dashboard.
        """
        
        # Main windows configuration
        self.root.title("Superstore Dashboard")
        self.root.geometry("1200x800")
        
        # Main frame
        self.main_frame = tb.Frame(self.root, padding = 10)
        self.main_frame.pack(fill = tk.BOTH, expand = True)
        
        # Title label
        title_label = tb.Label(self.main_frame, text = "Superstore Analysis", font = ("Helvetica", 24))
        title_label.pack(pady = 10)
        
        # Graphics frame
        self.graphics_frame = tb.Frame(self.main_frame)
        self.graphics_frame.pack(fill = tk.BOTH, expand = True, padx = 10, pady = 10)
        
        # Grid configuration
        self.graphics_frame.rowconfigure(0, weight = 1)
        self.graphics_frame.rowconfigure(1, weight = 1)
        self.graphics_frame.columnconfigure(0, weight = 1)
        self.graphics_frame.columnconfigure(1, weight = 1)
        
        # Frame for charts
        self.graphics_frames = {
            'sales trend': tb.Frame(self.graphics_frame),
            'category analysis': tb.Frame(self.graphics_frame),
            'regional_analysis': tb.Frame(self.graphics_frame),
            'segment_analysis': tb.Frame(self.graphics_frame)
        }
        
        # Frame placement
        self.graphics_frames['sales trend'].grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "nsew")
        self.graphics_frames['category analysis'].grid(row = 0, column = 1, padx = 5, pady = 5, sticky = "nsew")
        self.graphics_frames['regional_analysis'].grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "nsew")
        self.graphics_frames['segment_analysis'].grid(row = 1, column = 1, padx = 5, pady = 5, sticky = "nsew")
        
    def add_chart(self, figure, frame_key, title = None):
        """
        Adds a matplotlib figure to the specified frame in the dashboard.

        Args:
            figure (matplotlib.figure.Figure): The matplotlib figure to embed in the dashboard.
            frame_key (str): The key identifying which dashboard frame to use (e.g., 'sales trend', 'category analysis').
            title (str, optional): Title to display above the chart. Defaults to None.

        Raises:
            ValueError: If the specified frame_key does not exist in the dashboard.
        """
        if frame_key not in self.graphics_frames:
            raise ValueError(f"Frame '{frame_key}' does not exist.")
        
        # Clear previos content in the frame
        for widget in self.graphics_frames[frame_key].winfo_children():
            widget.destroy()
            
        # Add a title if provided
        if title:
            title_label = tb.Label(self.graphics_frames[frame_key], text = title, font = ("Helvetica", 16))
            title_label.pack(pady = 5)
            
        # Embed the matplotlib figure
        canvas = FigureCanvasTkAgg(figure, self.graphics_frames[frame_key])
        canvas.draw()
        canvas.get_tk_widget().pack(fill = tk.BOTH, expand = True)
        
        # Saves a reference
        self.figures[frame_key] = (figure, canvas)

    def add_control_panel(self, control_callback):
        """
        Adds a control panel with filters to the dashboard.

        Args:
            control_callback (callable): Function to be called when the user applies filters.
        """
        control_frame = tb.Frame(self.main_frame)
        control_frame.pack(fill = tk.X, padx = 10, pady = 5)
        
        # Category filter
        tb.Label(control_frame, text = "Category:").pack(side = tk.LEFT, padx = 5)
        self.categry_var = tk.StringVar(value = "Everything")
        categories = ["Everything", "Furniture", "Office Supplies", "Technology"]
        category_dropdown = tb.Combobox(control_frame, textvariable = self.categry_var, values = categories, width = 15)
        category_dropdown.pack(side = tk.LEFT, padx = 5)
        
        # Year filter
        tb.Label(control_frame, text = "Year:").pack(side = tk.LEFT, padx = 5)
        self.year_var = tk.StringVar(value = "Everything")
        years = ["Everything", "2014", "2015", "2016", "2017"]
        year_dropdown = tb.Combobox(control_frame, textvariable = self.year_var, values = years, width = 10)
        year_dropdown.pack(side = tk.LEFT, padx = 5)
        
        # Apply filters button
        apply_btn = tb.Button(control_frame, text = "Apply Filters", command = control_callback)
        apply_btn.pack(side = tk.LEFT, padx = 10)
        
    def get_filters(self):
        """
        Returns the current filter selections from the control panel.
        
        Returns:
            dict: Dictionary containing selected 'category' and 'year' values.
        """
        return {
            'category': self.category_war.get(),
            'year': self.year_var.get()
        }