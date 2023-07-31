import os
import subprocess
os.system('clear')

logo = '''

                     ______ ______
                   _/      Y      \_
                  // ~~ ~~ | ~~ ~  \\
                 // ~ ~ ~~ | ~~~ ~~ \\
                //________.|.________\\
               `----------`-'----------'
             _  __                                  _
   _ __   __| |/ _| ___ _ __   ___ _ __ _   _ _ __ | |_
  | '_ \ / _` | |_ / _ \ '_ \ / __| '__| | | | '_ \| __|
  | |_) | (_| |  _|  __/ | | | (__| |  | |_| | |_) | |_
  | .__/ \__,_|_|  \___|_| |_|\___|_|   \__, | .__/ \__|
  |_|Pdf Encryptor coded by Anonycodexia|___/|_|
   '''

print(logo)

def add_password_to_pdf(input_pdf, output_pdf, password):
    # Check if the input PDF file exists
    if not os.path.exists(input_pdf):
        print("Error: Input PDF file not found.")
        return

    # Generate the qpdf command
    qpdf_command = [
        "qpdf",
        "--encrypt",
        password,
        password,
        "256",
        "--",
        input_pdf,
        output_pdf
    ]

    # Execute the qpdf command
    try:
        subprocess.run(qpdf_command, check=True)
        print("Password added successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error adding password: {e}")

if __name__ == "__main__":
    input_pdf_file = input("Enter the name and path to the input PDF file: ")
    output_pdf_file = input("Enter the name and path for the output PDF file: ")
    password = input("Enter the password to be set on the PDF: ")

    add_password_to_pdf(input_pdf_file, output_pdf_file, password)
