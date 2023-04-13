# All Code has been written 100% by ChatGPT V3. No modifications execpt for this comment line. 
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk

class TournamentGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Video Game Tournament")

        # Set up the main frame and grid
        main_frame = tk.Frame(self.master)
        main_frame.grid(column=0, row=0, sticky="nsew")

        # Create three vertical frames to display images or videos
        left_frame = tk.Frame(main_frame)
        left_frame.grid(column=0, row=0, padx=10, pady=10, sticky="nsew")
        center_frame = tk.Frame(main_frame)
        center_frame.grid(column=1, row=0, padx=10, pady=10, sticky="nsew")
        right_frame = tk.Frame(main_frame)
        right_frame.grid(column=2, row=0, padx=10, pady=10, sticky="nsew")

        # Set up the three vertical frames
        self.create_vertical_frame(left_frame)
        self.create_vertical_frame(center_frame)
        self.create_vertical_frame(right_frame)

    def create_vertical_frame(self, frame):
        # Set up the vertical frame
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)
        frame.rowconfigure(2, weight=1)

        # Add a button to add player image or video
        add_player_button = ttk.Button(frame, text="Add Player", command=lambda: self.add_player(frame))
        add_player_button.grid(column=0, row=0, sticky="nsew", padx=5, pady=5)

        # Add a canvas to display the image or video
        canvas = tk.Canvas(frame, bg="black")
        canvas.grid(column=0, row=1, sticky="nsew", padx=5, pady=5)

        # Add a label to display the player name
        player_name_label = tk.Label(frame, text="Player Name", font=("Arial", 12))
        player_name_label.grid(column=0, row=2, sticky="nsew", padx=5, pady=5)

    def add_player(self, frame):
        # Open a file dialog to choose the player image or video
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png"), ("Video files", "*.mp4;*.avi")])

        # Display the player image or video on the canvas
        if file_path:
            player_image = Image.open(file_path)
            player_image = player_image.resize((200, 300))
            player_image = ImageTk.PhotoImage(player_image)
            canvas = frame.winfo_children()[1]
            canvas.delete("all")
            canvas.create_image(0, 0, anchor="nw", image=player_image)
            canvas.image = player_image

    def run(self):
        self.master.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    gui = TournamentGUI(root)
    gui.run()
