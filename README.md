# OpenAI Data Extraction Application

This Python application utilizes the OpenAI API to extract specific information from user input text and generate a formatted output. The extracted data includes a human name, postcode, Japan province, Japan city, Japan street, phone number, ordering count, date, and time. The application then processes this data and displays it in the Japanese language in a JSON format.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.x
- `tkinter` library (for GUI)
- `dotenv` library (for loading environment variables)
- `openai` library (for interacting with the OpenAI API)

You can install the required libraries using the following command:

```bash
pip install tkinter dotenv openai
```

## Setup

1. Clone the repository or download the source code files to your local machine.
2. Create a `.env` file in the project directory and add your OpenAI API key:

   ```plaintext
   API_KEY=your_openai_api_key
   ```

   Replace `your_openai_api_key` with your actual OpenAI API key.

## How to Run

1. Run the `main.py` file using the following command:

   ```bash
   python main.py
   ```

2. The application window will open, providing a text input area where you can enter the relevant information.

3. Click the "保管" (Save) button to extract and process the data using the OpenAI API. The extracted data will be displayed in the output area in Japanese JSON format.

4. The processed data is also saved to a CSV file named `order_<current_date>.csv`, where `<current_date>` represents the current date in the format `YYYYMMDD`.

## Application Workflow

1. The user enters input data in the input text area, which should contain relevant information such as addresses, names, and phone numbers.

2. Upon clicking the "保管" (Save) button, the application sends a prompt to the OpenAI API, requesting the extraction of specific details from the input text.

3. The OpenAI API generates a response based on the prompt, and the application processes the API response to extract the required information.

4. The extracted data is displayed in the output text area in Japanese JSON format.

5. The processed data is saved to a CSV file, which can be useful for record-keeping and further analysis.

## Error Handling

- If the input data is empty, an error message will be displayed, and the processing will not proceed.
- If there is an error in processing the data (e.g., issues with the OpenAI API or invalid API key), an error message dialog will be shown.

## Note

- Ensure that you have a stable internet connection to interact with the OpenAI API.
- Make sure to keep your OpenAI API key confidential and do not share it publicly.

Feel free to customize the application further or integrate additional features as needed!