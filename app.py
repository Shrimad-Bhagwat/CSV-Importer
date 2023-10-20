# All the imports
import tkinter as tk
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from tkinter import filedialog
import webbrowser
import time
from tkinter import *
from dotenv import load_dotenv
import os

# Load variables from the .env file
load_dotenv()

# Constants
fontSize = 10
fontStyle = "Open Sans"
kPc = "#6DB5CA"
kSc = "#B8D8E0"
kBg = "#FCF5EF"
kDc = "#FF7235"

# Create the main window
root = tk.Tk()

# Create a frame 
frame = tk.Frame(root, bg= kPc)
frame.pack()

# Define the scope of the API access
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

# Access the API path
creds_path = os.getenv("api_path")

# Authenticate with Google Sheets
creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)
client = gspread.authorize(creds)

# Custom pop up
def show_custom_message(title, message, color):
    popup = tk.Tk()
    popup.title(title)
    popup.geometry(f"{250}x{100}")
    label = tk.Label(popup, text=message, foreground=color, font=(fontStyle, fontSize))
    label.pack(padx=10, pady=10)

    button = tk.Button(popup, text="OK", command=popup.destroy)
    button.pack(pady=10)

    popup.mainloop()

# Ask User to select option
def create_new_gui():
    global spreadsheet_url
    def create_new():
        global spreadsheet_url
        file_name = file_name_entry.get()
        access_email = access_email_entry.get()

        if not file_name or not access_email:
            print("Warning Please enter both file name and access email.")
            return

        try:
            spreadsheet = client.create(file_name)
            spreadsheet.share(access_email, perm_type='user', role='writer')
            spreadsheet_url = spreadsheet.url

            # Show the link
            link_label = tk.Label(frame, text="Spreadsheet Link:", bg=kPc,  font=(fontStyle, fontSize))
            link_label.pack(pady=(20, 0))

            # Open Link Button
            link_button = tk.Button(frame, text="Open Link", command=open_link, background=kSc,  font=(fontStyle, fontSize))
            link_button.pack(padx=5, pady=5)

            root.quit()
        except gspread.exceptions.APIError as e:
            if "exceeded your sharing quota" in str(e):
                show_custom_message("Error", f"You have exceeded your sharing quota. \nPlease try again later.", "red")
            else:
                raise e

    def open_link():
        global spreadsheet_url
        if spreadsheet_url:
            webbrowser.open(spreadsheet_url)
        else:
            print("No spreadsheet link available.")
    
    spreadsheet_url = None

    # Entry for file name
    file_name_label = tk.Label(frame, text="File Name:", bg= kPc,  font=(fontStyle, fontSize))
    file_name_label.pack()

    # Name of the file to create
    file_name_entry = tk.Entry(frame,width=40,  font=(fontStyle, fontSize))
    file_name_entry.pack(padx=5, pady=5)

    # Entry for access email
    access_email_label = tk.Label(frame, text="Access Email:", bg= kPc,  font=(fontStyle, fontSize))
    access_email_label.pack()

    # Email to access the sheet
    access_email_entry = tk.Entry(frame, width=40,  font=(fontStyle, fontSize))
    access_email_entry.pack(padx=5,pady=5)

    # Button to create
    create_button = tk.Button(frame, text="Create", command=create_new,  font=(fontStyle, fontSize))
    create_button.pack(pady=5, padx=10)
    
# Use Existing Google sheet
def create_existing():
    global spreadsheet_url
    spreadsheet_url = entry.get()
    if spreadsheet_url != "":
        root.quit()
    else :
        show_custom_message("Warning", "No spreadsheet link available.","red")

# Create a New File 
def create_new():
    create_new_gui()

def select_columns():

    label = tk.Label(frame,  font=(fontStyle, fontSize), text="Select columns to import:", bg= kPc)
    label.pack(padx=10, pady=10)

    column_names = csv_df.columns.values

    def select_all():
        for var in checkbox_vars:
            var.set(1)

    def submit_selection():
        selected_columns = [col for col, var in zip(column_names, checkbox_vars) if var.get() == 1]
        root.quit()
        return selected_columns

    column_names = csv_df.columns.values

    checkbox_vars = []
    for col in column_names:
        var = tk.IntVar()
        checkbox_vars.append(var)
        checkbox = tk.Checkbutton(frame, font=(fontStyle, fontSize), text=col, variable=var, onvalue=1, offvalue=0, bg= kPc)
        checkbox.pack(anchor='w')

    select_all_button = tk.Button(frame,  font=(fontStyle, fontSize), text="Select All", command=select_all)
    select_all_button.pack(padx=10, pady=5)

    submit_button = tk.Button(frame,  font=(fontStyle, fontSize), text="Upload Data", command=submit_selection, background="#4ac782")
    submit_button.pack(padx=10, pady=5)
    root.mainloop()

    selected_columns = submit_selection()
    global filtered_data
    filtered_data = pd.read_csv(file_path, encoding='ISO-8859-1',header=0, usecols=selected_columns)
    print(filtered_data)

# Function for file upload
def upload_csv():
    global csv_df
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        csv_df = pd.read_csv(file_path , encoding='ISO-8859-1')
        select_columns()

root.title("CSV to Google Sheet")

label = tk.Label(frame,  font=(fontStyle, fontSize), text="Do you want to provide an existing spreadsheet URL or create a new one?", bg= kPc)
label.pack(padx=10, pady=10)

entry = tk.Entry(frame,  font=(fontStyle, fontSize),width=40)
entry.pack(padx=10, pady=10)

button_existing = tk.Button(frame,  font=(fontStyle, fontSize), text="Use Existing", command=create_existing)
button_existing.pack(padx=10, pady=5)

button_new = tk.Button(frame,  font=(fontStyle, fontSize), text="Create New", command=create_new)
button_new.pack(padx=10, pady=10)

root.mainloop()

# Create a button to trigger file upload
upload_button = tk.Button(frame,  font=(fontStyle, fontSize), text="Upload CSV", command=upload_csv, bg=kSc)
upload_button.pack(pady=10)

root.mainloop()

# Create a Close button
def close_window():
    root.destroy()  
close_button = tk.Button(frame,  font=(fontStyle, fontSize), text="Close", command=close_window, bg=kDc)
close_button.pack(pady=10)

# Open the existing spreadsheet by its URL
spreadsheet = client.open_by_url(spreadsheet_url)

# Get the ID and URL of the newly created spreadsheet
spreadsheet_id = spreadsheet.id
spreadsheet_url = spreadsheet.url

# print(f"New spreadsheet created with ID: {spreadsheet_id}")
print(f"Link to the spreadsheet: {spreadsheet_url}")

# Write the CSV data to an Excel file
excel_output_path = './data/SampleFile.xlsx'
filtered_data.to_excel(excel_output_path, index=False)

# Read the Excel sheet into a DataFrame
excel_df = pd.read_excel(excel_output_path)

# Get the first (and only) sheet of the spreadsheet
worksheet = spreadsheet.get_worksheet(0)

try:
    # Convert all non-JSON compliant values to strings
    for col in excel_df.columns:
        excel_df[col] = excel_df[col].astype(str)

    # Convert DataFrame to a list of lists for easy import
    values = excel_df.values.tolist()

    # Update the Google Sheet
    worksheet.clear()
    worksheet.insert_rows(values)

    print(f"Data from Excel file '{excel_output_path}' imported to Google Sheet.")
    show_custom_message("Success", "Data Successfully added!","green")
except Exception as e:
    print(f"An error occurred while processing the Excel file: {e}")
    show_custom_message("Error", "An Error occurred while processing the file!", "red")
time.sleep(2)

