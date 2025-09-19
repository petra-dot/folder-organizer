# 📂 Folder Organizer

![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.10%2B-brightgreen)

A Python tool to automatically organize files into categories (Images, Videos, Documents, Audio, Code, Archives, Others). Keeps your folders clean and structured with just one command.

---

## 🚀 Features

- Organizes files into categories:
  - **Images**
  - **Videos**
  - **Documents**
  - **Audio**
  - **Archives**
  - **Code**
  - **Others**
- Handles duplicate file names safely (e.g., `file_1.pdf`, `file_2.pdf`, etc.)
- Creates folders automatically if missing
- Skips hidden/system files
- Easy to extend with your own categories in `categories.py`

---

## 🛠️ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/petra-dot/folder-organizer.git
   cd folder-organizer
   ```

2. (Optional) Create a virtual environment:

   ```bash
   python -m venv venv
   ```

   Activate the virtual environment:

   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## ⚡ Usage

Organize any folder by running:

```bash
python -m organizer.main /path/to/your/folder
```

### Examples

#### Windows

```bash
python -m organizer.main "C:\Users\YourName\Downloads"
python -m organizer.main "C:\Users\YourName\Desktop\Stuff"
```

#### Linux / macOS

```bash
python -m organizer.main ~/Downloads
python -m organizer.main ~/Desktop/Stuff
```

---

## 🛠️ Development & Testing

Run tests with `pytest`:

```bash
pytest
```

---

## 📌 Roadmap

- [ ] Add `--dry-run` option to preview changes without moving files
- [ ] Add logging to track moved files
- [ ] Add config file for custom categories
- [ ] Add GUI version (Tkinter or PyQt)
- [ ] Package for PyPI (`pip install folder-organizer`)

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a pull request

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🧠 How It Works

1. Scans the specified folder for files.
2. Matches file extensions with predefined categories in `categories.py`.
3. Moves files into corresponding subfolders.
4. Handles duplicate file names by appending a counter (e.g., `file_1.txt`).

---

Made with ❤️ by Petra.
