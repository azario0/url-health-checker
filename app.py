import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont
import requests
import threading
import queue

class URLCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("URL Health Checker")
        self.root.geometry("500x350")
        self.root.resizable(False, False)
        
        # --- Color and Font Scheme ---
        self.BG_COLOR = "#2E3B4E"
        self.FG_COLOR = "#FFFFFF"
        self.ENTRY_BG = "#4A5A70"
        self.BUTTON_BG = "#4A90E2"
        self.BUTTON_HOVER = "#4281CB"
        self.SUCCESS_COLOR = "#7ED321"
        self.ERROR_COLOR = "#D0021B"
        
        self.title_font = tkfont.Font(family="Segoe UI", size=24, weight="bold")
        self.label_font = tkfont.Font(family="Segoe UI", size=12)
        self.result_font = tkfont.Font(family="Segoe UI", size=14, weight="bold")
        
        self.root.configure(bg=self.BG_COLOR)
        
        # --- Queue for thread communication ---
        self.result_queue = queue.Queue()

        self.setup_styles()
        self.create_widgets()
        self.process_queue() # Start the queue checker loop

    def setup_styles(self):
        """Configure custom ttk styles for a modern look."""
        style = ttk.Style(self.root)
        style.theme_use('clam')

        # Style for the Entry widget
        style.configure('TEntry', 
                        fieldbackground=self.ENTRY_BG,
                        foreground=self.FG_COLOR,
                        insertcolor=self.FG_COLOR,
                        borderwidth=0,
                        padding=10)

        # Style for the Button widget
        style.configure('Modern.TButton', 
                        background=self.BUTTON_BG,
                        foreground=self.FG_COLOR,
                        font=self.label_font,
                        padding=10,
                        borderwidth=0,
                        relief='flat')
        
        # Map style changes for different states (e.g., mouse hover)
        style.map('Modern.TButton',
                  background=[('active', self.BUTTON_HOVER), 
                              ('pressed', self.BUTTON_HOVER)],
                  relief=[('pressed', 'flat')])

    def create_widgets(self):
        """Create and place all the widgets in the window."""
        # --- Main Frame ---
        main_frame = tk.Frame(self.root, bg=self.BG_COLOR, padx=40, pady=30)
        main_frame.pack(expand=True, fill='both')

        # --- Title Label ---
        title_label = tk.Label(main_frame, text="URL Health Checker", 
                               font=self.title_font, bg=self.BG_COLOR, fg=self.FG_COLOR)
        title_label.pack(pady=(0, 20))

        # --- URL Entry ---
        self.url_entry = ttk.Entry(main_frame, style='TEntry', font=self.label_font, width=40)
        self.url_entry.pack(fill='x')
        self.url_entry.insert(0, "e.g., https://www.google.com")
        self.url_entry.bind("<FocusIn>", self.on_entry_focus_in)
        self.url_entry.bind("<FocusOut>", self.on_entry_focus_out)
        self.url_entry.bind("<Return>", lambda event: self.start_check_thread()) # Bind Enter key

        # --- Check Button ---
        check_button = ttk.Button(main_frame, text="Check Status", 
                                  style='Modern.TButton', command=self.start_check_thread)
        check_button.pack(pady=20)

        # --- Result Label ---
        self.result_label = tk.Label(main_frame, text="Enter a URL to check its status",
                                     font=self.result_font, bg=self.BG_COLOR, fg=self.FG_COLOR,
                                     wraplength=400) # Wraps text if it's too long
        self.result_label.pack(pady=(10, 0))

    def on_entry_focus_in(self, event):
        """Clear placeholder text on focus."""
        if self.url_entry.get() == "e.g., https://www.google.com":
            self.url_entry.delete(0, tk.END)
            self.url_entry.config(foreground=self.FG_COLOR)

    def on_entry_focus_out(self, event):
        """Restore placeholder text if entry is empty."""
        if not self.url_entry.get():
            self.url_entry.insert(0, "e.g., https://www.google.com")
            self.url_entry.config(foreground=self.FG_COLOR)

    def start_check_thread(self):
        """Starts the URL check in a separate thread to avoid freezing the GUI."""
        url = self.url_entry.get().strip()
        if not url or url == "e.g., https://www.google.com":
            self.update_result("Please enter a valid URL.", self.ERROR_COLOR)
            return
        
        # Provide immediate feedback to the user
        self.update_result(f"Checking {url}...", self.FG_COLOR)
        
        # Create and start the background thread
        thread = threading.Thread(target=self.perform_check, args=(url,), daemon=True)
        thread.start()

    def perform_check(self, url):
        """
        The actual network request function. This runs in the background.
        Puts the result into a queue for the main thread to process safely.
        """
        # Prepend 'https://' if no scheme is present
        if not url.startswith(('http://', 'https://')):
            url = f"https://{url}"

        try:
            headers = {
                'User-Agent': 'Python-URL-Checker/1.0'
            }
            # A timeout is crucial to prevent the thread from hanging indefinitely
            response = requests.get(url, timeout=10, headers=headers)
            
            if 200 <= response.status_code < 300:
                result_message = f"✅ Online!\nStatus Code: {response.status_code}"
                self.result_queue.put(("success", result_message))
            else:
                result_message = f"❌ Error!\nStatus Code: {response.status_code}"
                self.result_queue.put(("error", result_message))
        
        except requests.exceptions.RequestException as e:
            result_message = f"❌ Offline or Invalid URL\nError: Could not connect."
            self.result_queue.put(("error", result_message))

    def process_queue(self):
        """
        Checks the queue for results from the background thread and updates the GUI.
        This runs in the main thread.
        """
        try:
            status, message = self.result_queue.get_nowait()
            if status == "success":
                self.update_result(message, self.SUCCESS_COLOR)
            else:
                self.update_result(message, self.ERROR_COLOR)
        except queue.Empty:
            pass
        finally:
            # Schedule itself to run again after 100ms
            self.root.after(100, self.process_queue)

    def update_result(self, message, color):
        """Updates the result label with a given message and color."""
        self.result_label.config(text=message, fg=color)


if __name__ == "__main__":
    root = tk.Tk()
    app = URLCheckerApp(root)
    root.mainloop()