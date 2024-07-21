from tkinter import *
from tkinter import filedialog, simpledialog
from PIL import Image, ImageTk
from collections import Counter


FONT = ('Times New Roman', 10, 'italic')
FONT_1 = ('Times New Roman', 12, 'bold')


def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(*rgb)


def upload_file():
    # Open file dialog and allow the user to choose a file
    file_path = filedialog.askopenfilename()

    image = Image.open(file_path)

    # Convert the image to RGB mode (if not already in RGB)
    image = image.convert('RGB')
    
    # Get the pixel data
    pixels = list(image.getdata())
    
    # Count the frequency of each color
    color_count = Counter(pixels)
    
    # Get the most common color
    most_common_color = color_count.most_common(1)[0][0]
    
    hexcode = rgb_to_hex(most_common_color)
    # Convert the image to a format that Tkinter can display
    tk_image = ImageTk.PhotoImage(image)
    
   
    # Display the image in a Tkinter label
    image_label = Label(image=tk_image)
    image_label.pack(expand=True, pady=30)
    image_label.image = tk_image  # Keep a reference to avoid garbage collection
    
    
    def watermark():
        win_width = tk_image.width()
        win_height = tk_image.height()
        
        user_input = simpledialog.askstring('Input', 'Enter text here')
        
        txt_clr = simpledialog.askstring('Input', 'Enter color here')
        
        
        xx = 0
        yy = 190
        while True:
            if xx <= win_width:
                while True:
                    if yy <= win_height + 145:
                        new_label = Label(text=user_input, bg=hexcode, fg=txt_clr, font=FONT)
                        new_label.place(x=xx, y=yy)
                        new_label.config(padx=40)
                        yy += 50
                    
                    else:
                        xx += 100
                        yy = 190
                        break
            else:
                break
            
    
    # Watermark Button:
    add_watermrk = Button(window, text='Add Watermark', command=watermark, bd=8, bg='#7A6363', fg='white', font=FONT_1)
    add_watermrk.pack(expand=True)
    

# Create the main window
window = Tk()
window.title("Image WaterMark")
window.config(width=400, height=400, bg='white')


# Create a button that triggers the file upload dialog
upload_img = PhotoImage(file='upload.png')
upload_button = Button(window, image=upload_img, command=upload_file)
upload_button.pack(expand=True)


# Run the Tkinter event loop
window.mainloop()