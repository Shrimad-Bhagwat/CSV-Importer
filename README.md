
# StackIt Hiring Assignment

## ✨ **Problem Statement: Crafting a CSV Importer for Google Sheets** ✨


**Problem Statement**:
Make a CSV Importer for Google Sheets that lets users drag and drop CSV files onto the Google Sheet. The moment they drop the CSV file, allow them to select which columns to import 🗂️.

## Tech Stack 🛠️

- Python 🐍
- Tkinter 🖥️
- gspread 📊
- pandas 🐼
- OAuth2 🔐

## Workflow 🔄

1. **Create or Use Existing Sheet** 🗂️
Users have the option to either create a new Google Sheet or use an existing one for the data import. If they choose to create a new sheet, they will be prompted to provide a file name and an access email for sharing the sheet.

2. **Import Data** 📤
Once the user confirms their selections, then the user is asked to upload the csv file.If a new sheet was created, it will be shared with the specified email for collaborative access.

3. **Upload CSV** 📁
Users then have to click the "Upload CSV" button. This action prompts them to select a CSV file from their local system. The selected file will be used for further processing.

4. **Select Columns** ✅
After the CSV file is uploaded, users are presented with a list of columns from the file. They can then choose which columns they want to import into the Google Sheet. This step allows for customization and flexibility in data selection.

5. **Close Application** 🚀
After the import process is complete, users have the option to close the application using the "Close" button. This concludes the workflow.

This workflow ensures a user-friendly experience, guiding users through the necessary steps to import CSV data into Google Sheets. It offers flexibility in data selection, allows for both new and existing sheets, and provides clear instructions for a smooth process.

## Usage 🧾

 **Create a Service Account Key (***Important Step***)** 🔑:

 For this project to work on your device you must have the service account key.
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Select your project or create a new one.
   - In the sidebar, navigate to the "APIs & Services" > "Credentials" section.
   - Click "Create credentials" and select "Service Account Key".
   - Fill out the form and select the role "Editor" or "Owner".
   - Click "Create" to generate the key. This will download a JSON file containing your credentials.
   - Place this JSON file in the project directory with the name `csv_key.json` inside data.


1. Launch the application. 🚀
2. Choose to either create a new Google Sheet or use an existing one. 🗂️
3. Click the "Upload CSV" button to select a CSV file. 📁
4. Select the columns you want to import. ✅
5. Confirm the import. ✅


## Developer's Section 👨‍💻👩‍💻

Watch this demo video walkthrough. Feel free to leave comments and ask any questions.

### [Demo Video](https://youtu.be/tQpk7mAm6qk)

[![Watch the video](https://storage.googleapis.com/website-production/uploads/2023/04/how-to-build-demo-landing-pages.webp)](https://youtu.be/tQpk7mAm6qk)



## Contributing 🤝

Contributions are welcome! Feel free to open an issue or submit a pull request. 🛠️

To contribute to this project, follow these steps:

1. **Fork this repository** 🍴: Click the "Fork" button at the top-right corner of this page to create your own copy of the repository.

2. **Clone your fork** 📥: Use `git clone` to clone your forked repository to your local machine. Replace `[your_username]` with your GitHub username.

    ```bash
    git clone https://github.com/[your_username]/StackIt-Hiring-Assignment.git
    ```

3. **Create a new branch** 🌿: Create a new branch for your contributions. This keeps your changes isolated from the `main` branch.

    ```bash
    cd StackIt-Hiring-Assignment
    git checkout -b feature/new-feature
    ```

4. **Set up a virtual environment** ⚗️: It's recommended to create a virtual environment to manage dependencies.

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

5. **Install dependencies** 📦: Install the required packages listed in `requirements.txt`.

    ```bash
    pip install -r requirements.txt
    ```

6. **Create a Service Account Key (***Important Step***)** 🔑:
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Select your project or create a new one.
   - In the sidebar, navigate to the "APIs & Services" > "Credentials" section.
   - Click "Create credentials" and select "Service Account Key".
   - Fill out the form and select the role "Editor" or "Owner".
   - Click "Create" to generate the key. This will download a JSON file containing your credentials.
   - Place this JSON file in the project directory with the name `csv_key.json` inside data.


7. **Make your changes** 🛠️: Make the necessary changes and improvements in the code.

8. **Commit your changes** 📝: Once you're satisfied with your changes, commit them with a descriptive message.

    ```bash
    git add .
    git commit -m "Add your commit message here"
    ```

9. **Push your changes** 🚀: Push your changes to your forked repository.

    ```bash
    git push origin feature/new-feature
    ```

10. **Create a pull request** 🔄: Go to the original repository and click on the "New Pull Request" button. Provide a clear description of your changes.

11. **Review and merge** ✔️: Collaborators will review your pull request. Once approved, your changes will be merged into the main branch.


Now you're all set to start contributing to this project! Happy coding! 🚀


## License 📝

This project is licensed under the [MIT License](link_to_license). 📜
