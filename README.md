# 📂 Folder Organizer

A Python tool to automatically organize files into categories (Images, Videos, Documents, Audio, Code, Archives, Others).  
Keeps your folders clean and structured with just one command.

---

## 🚀 Installation

Clone the repo:

```bash
git clone https://github.com/petra-dot/folder-organizer.git
cd folder-organizer
```

(Optional) create a virtual environment:

python -m venv venv
source venv/bin/activate # On macOS/Linux
venv\Scripts\activate # On Windows

Install dependencies (standard library only, so requirements.txt may be empty for now):

pip install -r requirements.txt

⚡ Usage

Organize any folder by running:

python -m organizer.main /path/to/your/folder

Examples

Windows

python -m organizer.main "C:\Users\YourName\Downloads"
python -m organizer.main "C:\Users\YourName\Desktop\Stuff"

Linux / macOS

python -m organizer.main ~/Downloads
python -m organizer.main ~/Desktop/Stuff

✅ Features

Organizes files into categories:

Images

Videos

Documents

Audio

Archives

Code

Others

Handles duplicate file names safely (file_1.pdf, file_2.pdf, etc.)

Creates folders automatically if missing

Error-proof (skips hidden/system files)

Easy to extend with your own categories in categories.py

🛠️ Development & Testing

Run tests with pytest:
pytest

📌 Roadmap

Add --dry-run option to preview changes without moving files

Add logging to track moved files

Add config file for custom categories

Add GUI version (Tkinter or PyQt)

Package for PyPI (pip install folder-organizer)

📜 License

This project is licensed under the MIT License

--- Made with ❤️ by Petra
