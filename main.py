import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file"
]

# Authenticate using JSON key
creds = ServiceAccountCredentials.from_json_keyfile_name('geometric-rock-449809-v8-28e13b6b90a2.json', scope)
client = gspread.authorize(creds)

# Open the Google Sheet
url = 'https://docs.google.com/spreadsheets/d/1B4aRfmAE-reHnAH0Yiluta-VFUCqxQ7j25unA0dyjhM/edit?gid=1086824825#gid=1086824825'
sheet = client.open_by_url(url)  # Open Google Sheet
worksheet = sheet.get_worksheet(1)  # Select the first sheet

# Fetch all rows
data = worksheet.get_all_records()

# Debugging: Print column names to check headers
if data:
    print("Column Names:", data[0].keys())  # Print first row's keys to check if "Question" exists

# Function to get answer
def get_answer(question):
    for row in data:
        if 'Question' in row and 'Answer' in row:  # Ensure keys exist
            if question.lower() in row['Question'].lower():
                return row['Answer']
    return "Sorry, I don't have an answer for that."

# Debugging: Example Query
if __name__ == "__main__":
    user_input = input("Ask a question: ")
    print(get_answer(user_input))
