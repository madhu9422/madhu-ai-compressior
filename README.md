# AI Document Comparison Assistant

A Streamlit web application that compares two PDF documents using the Gemini API. It extracts text from each PDF, identifies similarities and differences, summarizes key details, and lets users download a comparison report as a Word document.

## Features

- Upload two PDF documents for comparison.
- Extract and preview PDF text.
- Show document page counts and character counts.
- Compare document summaries, similarities, differences, and key details.
- Display an overall conclusion and limitations.
- Download the comparison results as a `.docx` report.
- Configure the Gemini API key securely for local use or Streamlit Community Cloud.

## Project structure

```text
ai-document-comparison-assistant/
├── app.py                 # Streamlit user interface
├── comparison.py          # Gemini API comparison logic
├── document_reader.py     # PDF validation and text extraction
├── report_generator.py    # Word report generation
├── test_key.py            # Optional Gemini API connection test
├── requirements.txt       # Python dependencies
├── .env.example           # Example local environment configuration
├── .gitignore             # Files excluded from Git
└── README.md              # Project documentation
```

Your exact files may differ slightly. Keep the file names consistent with the imports in your code.

## Requirements

- Python 3.10 or a compatible version supported by your installed dependencies.
- A Gemini API key that is valid for the Gemini API used by your code.
- Internet access when calling Gemini.
- Two readable PDF files to compare.

## Run locally on Windows

### 1. Open PowerShell and go to the project folder

```powershell
cd "C:\Users\admin\Videos\AI_Document_Comparison_Assistant_Project\ai-document-comparison-assistant"
```

### 2. Create a virtual environment (if you do not already have one)

```powershell
python -m venv .venv
```

### 3. Activate the virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run this in the current PowerShell window and then activate again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

If you need to install the main packages separately:

```powershell
python -m pip install streamlit pypdf python-dotenv google-genai python-docx
```

### 5. Configure your local API key

Create or open the `.env` file in the project folder:

```powershell
notepad .env
```

Add your own valid API key and the model configured for your project:

```text
GEMINI_API_KEY=YOUR_VALID_GEMINI_API_KEY
GEMINI_MODEL=gemini-3.8-flash
```

Replace `YOUR_VALID_GEMINI_API_KEY` with your key. Do not include the placeholder literally. Do not commit `.env` to GitHub.

The model name above reflects the current project configuration; use a model name that is available to your Gemini API key and supported by the API call in `comparison.py`.

### 6. Test the Gemini API connection (optional)

If your project includes `test_key.py`, it should load the key from `.env` rather than hard-coding the key in the Python file.

Run:

```powershell
python test_key.py
```

A successful test should report that the Gemini API is working. Never print, paste, or share the actual API key.

### 7. Start the app

```powershell
python -m streamlit run app.py
```

Streamlit will display a local URL in the terminal, commonly `http://localhost:8501`. Open that URL in your browser.

To stop the app, press `Ctrl+C` in PowerShell.

### 8. Check Python syntax

```powershell
python -m py_compile app.py comparison.py document_reader.py report_generator.py
```

## Deploy to Streamlit Community Cloud

### 1. Prepare GitHub

Push the project code to a GitHub repository. Include the application source files, `requirements.txt`, `.gitignore`, and this README.

Do **not** commit or upload:
- `.env`
- `.venv/`
- API keys, passwords, or other credentials
- Private PDF documents or reports containing confidential information

Check `.gitignore` includes at least:

```gitignore
.env
.venv/
__pycache__/
*.py[cod]
.streamlit/secrets.toml
```

A public GitHub repository makes committed source files visible to everyone. Do not place secrets in source code or commit history.

### 2. Create the Streamlit app

1. Open [Streamlit Community Cloud](https://share.streamlit.io/).
2. Choose the option to create or deploy an app from GitHub.
3. Select your repository and the branch that contains your code.
4. Set **Main file path** to `app.py` if it is in the repository root.
5. Open **Advanced settings** and locate **Secrets**.

### 3. Configure Streamlit Secrets

Enter your key in TOML format:

```toml
GEMINI_API_KEY = "YOUR_VALID_GEMINI_API_KEY"
GEMINI_MODEL = "gemini-3.8-flash"
```

Replace the placeholder with your actual key in Streamlit Secrets only. Do not add the real key to this README, GitHub, or chat.

Your Python code must read `GEMINI_API_KEY` from Streamlit Secrets when deployed and may read it from `.env` for local development. For example:

```python
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY", "").strip()

if not api_key:
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
    except (KeyError, FileNotFoundError):
        api_key = ""
```

Use `api_key` when creating the Gemini client. Avoid creating a second variable later that overwrites it.

### 4. Deploy and test

Save the settings and deploy the app. When it starts, upload two non-confidential sample PDFs and run a comparison. Check the Streamlit logs if startup or comparison fails.

After changing code, commit and push the changes to GitHub. Streamlit Community Cloud usually rebuilds the app from the updated repository. Restart the app if needed.

## Troubleshooting

### `401 UNAUTHENTICATED` or `API_KEY_INVALID`

- Confirm the key is valid and active in [Google AI Studio](https://aistudio.google.com/apikey).
- Confirm the key belongs to a project configured for the Gemini API.
- Confirm Streamlit Secrets uses the exact name `GEMINI_API_KEY`.
- Check that the deployed app is using the updated secret.
- Verify that the authentication method in your Python SDK/code is compatible with the type of key you created.
- If a key has been shared or committed publicly, revoke it and create a replacement.

### `503 UNAVAILABLE`

This can indicate temporary service demand. Wait briefly and retry. If it persists, check the provider's status and model availability. Retry handling may help with temporary errors, but it cannot fix an invalid key.

### `This file does not exist`

- Confirm `app.py` is present in the selected repository and branch.
- Set the main file path to `app.py` if it is in the repository root.
- If the file is inside a folder, enter its correct relative path, such as `folder_name/app.py`.
- Match file names and capitalization exactly.

### Local app works but cloud app fails

- Confirm the new API key is saved under Streamlit **Settings → Secrets**.
- Confirm `comparison.py` reads Streamlit Secrets as well as `.env`.
- Check that `requirements.txt` includes all required dependencies.
- Review the Streamlit app logs for the full error.

## Security

- Never hard-code API keys in Python files.
- Keep `.env` and `.streamlit/secrets.toml` out of Git.
- Revoke any API key that has been exposed and create a new one.
- Do not use confidential documents for testing unless your organization's rules permit it.
- Only upload PDFs you are authorized to process.

## Technology stack

- Python
- Streamlit
- Google Gemini API (`google-genai`)
- `pypdf` for PDF text extraction
- `python-docx` for Word report generation
- `python-dotenv` for local environment variables

## License

Add a license appropriate for your project before distributing or reusing the source code publicly.
