import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import boto3
import os
import sys
from tempfile import gettempdir
from contextlib import closing

# Create a ThemedTk window
root = ThemedTk(theme="breeze")  # You can try other themes like 'arc', 'radiance', 'yaru', etc.
root.geometry("500x300")
root.title("T2S-Converter Amazon Polly")

# Main frame
main_frame = ttk.Frame(root, padding=(10, 10, 10, 10))
main_frame.pack(expand=True, fill='both')

# Label for Text Entry
text_label = ttk.Label(main_frame, text="Enter your text here:")
text_label.pack(anchor='w', pady=(0, 5))

# Text entry
textExample = tk.Text(main_frame, height=10, wrap='word', font=("Helvetica", 12))
textExample.pack(expand=True, fill='both', padx=(0, 0), pady=(0, 10))

# Frame for buttons and options
button_frame = ttk.Frame(main_frame)
button_frame.pack(fill='x')

# Dropdown for voice selection
voice_label = ttk.Label(button_frame, text="Select Voice:")
voice_label.pack(side='left', padx=(0, 5))
voice_options = ttk.Combobox(button_frame, values=["Joanna", "Matthew", "Ivy"], state="readonly")
voice_options.set("Joanna")
voice_options.pack(side='left', padx=(0, 15))

# Button to read text
def getText():
    aws_mag_console = boto3.session.Session(profile_name='boto3_user')
    client = aws_mag_console.client(service_name='polly', region_name='us-east-1')
    result = textExample.get("1.0", "end").strip()
    print(result)
    selected_voice = voice_options.get()
    response = client.synthesize_speech(VoiceId=selected_voice, OutputFormat='mp3', Text=result, Engine='neural')
    print(response)
    if "AudioStream" in response:
        with closing(response['AudioStream']) as stream:
            output = os.path.join(gettempdir(), "speech.mp3")
            try:
                with open(output, "wb") as file:
                    file.write(stream.read())
            except IOError as error:
                print(error)
                sys.exit(-1)
    else:
        print("Could not find the stream")
        sys.exit(-1)
    if sys.platform == 'win32':
        os.startfile(output)

btnRead = ttk.Button(button_frame, text="Read", command=getText)
btnRead.pack(side='left', padx=(0, 5))

# Run the application
root.mainloop()
