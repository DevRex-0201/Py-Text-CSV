import tkinter as tk
import os
import json
import csv
from tkinter import messagebox
from dotenv import load_dotenv
import openai
import datetime



current_date = datetime.date.today()
formatted_datetime = current_date.strftime("%Y%m%d")

# Load environment variables from .env file
load_dotenv()

# Function to process data when the Save button is clicked
def process_data():
    """
    Extracts input data from the user, sends a prompt to OpenAI API, processes the generated response,
    displays the extracted information, and saves the data to a CSV file.
    """
    input_data = input_text.get("1.0", "end-1c")
    if not input_data.strip():
        messagebox.showerror("Error", "Input data cannot be empty.")
        return
    
    # Prompt text for OpenAI API
    prompt = input_data + """
\nplease extract a human name, postcode, Japan province, Japan city, Japan street, phone number, ordering count, date, and time from the above text. \n\n Then keep in mind to give me a JSON data in Japanese with the below template. Keep in mind that should be Japanese. \n{"name": "value", "postcode": "value", "province": "value", "city": "value", "street": "value", "phonenumber": "value", "count": "value", "date": "value", "time": "value"}). \n\nIn case can not find similar content for each item, keep in mind to insert the empty letter
"""
    try:
        # Call OpenAI API to generate text based on the prompt
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=300,  # Adjust max tokens based on response length
            api_key=os.getenv('API_KEY')  # Read API_KEY from environment variables
        )

        # Get the generated response text
        generated_text = response.choices[0].text.strip()
        json_data = json.loads(generated_text)
        output_data = "氏名: " + json_data['name'] + "\n郵便番号: " + json_data['postcode'] + "\n都道府県: " + json_data['province'] + "\n住所1: " + json_data['city'] + "\n住所2: " + json_data['street'] + "\n電話番号: " + json_data['phonenumber'] + "\n数: " + json_data['count'] + "\n発送日: " + json_data['date'] + "\n発送時間: " + json_data['time']

        # Display generated text in the output textarea
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, output_data)

        csv_file_path = f'order_{formatted_datetime}.csv'

        file_exists = os.path.exists(csv_file_path)
    
        # Read existing data from the CSV file if it exists
        existing_data = []
        if file_exists:
            with open(csv_file_path, mode='r', encoding='utf-8-sig', newline='') as csv_file:
                csv_reader = csv.reader(csv_file)
                existing_data = list(filter(None, list(csv_reader)))
        else:
            header = ["氏名", "氏名フリガナ", "郵便番号", "都道府県", "住所1", "住所2", "電話番号1分類1", "数", "発送日", "発送時間"]
            existing_data.append(header)

        with open(csv_file_path, mode='w', encoding='utf-8-sig', newline='') as csvfile: # OR MAYBE encoding='utf-8-sig's
            csv_writer = csv.writer(csvfile)
            # Extract keys and values from the JSON data
            values = list(json_data.values())
            values.insert(1, "")
            existing_data.append(values)
            csv_writer.writerows(existing_data)

    except Exception as e:
        messagebox.showerror("Error", f"Failed to process data: {e}")

# GUI setup
root = tk.Tk()
root.title("")

# Input Text Area
input_label = tk.Label(root, text="入力:")
input_label.pack()
input_text = tk.Text(root, height=10, width=50)
input_text.pack()

# Output Text Area
output_label = tk.Label(root, text="出力:")
output_label.pack()
output_text = tk.Text(root, height=10, width=50)
output_text.pack()

# Save Button
save_button = tk.Button(root, text="保管", command=process_data)
save_button.pack()

root.mainloop()
