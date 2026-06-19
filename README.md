# 📂 Smart File Organizer

A Python-based File Management System that automatically organizes files into categorized folders based on their extensions and maintains detailed logs of all operations.

This project helps users keep their directories clean and structured by automatically sorting files into folders such as Images, Documents, Videos, Music, Archives, Scripts, Programs, and more.

---

## 🚀 Features

* 📁 Automatic file organization
* 🖼️ Organizes Images, Videos, Documents, Music, Archives, and more
* 📝 Detailed logging of all file movements
* 🔄 Automatically creates category folders if they do not exist
* 🛡️ Handles duplicate file names safely
* ⚠️ Error handling for inaccessible or locked files
* 📊 Displays organization statistics
* 🔍 Supports 50+ file extensions
* 💻 Simple and lightweight implementation using Python

---

## 📂 Supported Categories

| Category  | Supported Extensions                           |
| --------- | ---------------------------------------------- |
| Images    | jpg, jpeg, png, gif, bmp, tiff, webp, svg      |
| Videos    | mp4, mkv, mov, avi, wmv, flv                   |
| Documents | pdf, doc, docx, txt, ppt, pptx, xls, xlsx, csv |
| Music     | mp3, wav, flac, aac                            |
| Archives  | zip, rar, 7z, tar, gz, iso                     |
| Scripts   | py, js, html, css, php, bat, ps1               |
| Programs  | exe, apk, jar                                  |
| Databases | db, sqlite, sql                                |
| Config    | json, xml, yaml, ini                           |
| Others    | Unrecognized file types                        |

---

## 🏗️ Project Structure

```text
SmartFileOrganizer/
│
├── main.py
├── file_organization_log.txt
│
├── Images/
├── Videos/
├── Documents/
├── Music/
├── Archives/
├── Scripts/
├── Programs/
├── Databases/
├── Config/
└── Others/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/SmartFileOrganizer.git
```

### Navigate to Project Directory

```bash
cd SmartFileOrganizer
```

### Run the Program

```bash
python main.py
```

---

## 🖥️ Example

### Before Organization

```text
RandomFiles/
│
├── image.jpg
├── report.pdf
├── video.mp4
├── song.mp3
├── script.py
├── data.json
└── archive.zip
```

### After Organization

```text
RandomFiles/
│
├── Images/
│   └── image.jpg
│
├── Documents/
│   └── report.pdf
│
├── Videos/
│   └── video.mp4
│
├── Music/
│   └── song.mp3
│
├── Scripts/
│   └── script.py
│
├── Config/
│   └── data.json
│
└── Archives/
    └── archive.zip
```

---

## 📋 Logging

Every file movement is recorded in:

```text
file_organization_log.txt
```

Example:

```text
2026-06-19 10:15:02 - Moved: image.jpg -> Images
2026-06-19 10:15:03 - Moved: report.pdf -> Documents
2026-06-19 10:15:04 - Moved: video.mp4 -> Videos
```

---

## 🛠️ Technologies Used

* Python 3.x
* os
* shutil
* logging
* datetime

---

## 🎯 Learning Objectives

This project demonstrates:

* File Handling
* Directory Management
* Python Automation
* Logging Systems
* Exception Handling
* Clean Code Practices
* Project Structuring

---

## 📈 Future Enhancements

* GUI Version using Tkinter / CustomTkinter
* Drag-and-Drop Folder Support
* Duplicate File Detection
* CSV & Excel Reports
* Real-Time Folder Monitoring
* Undo Last Operation
* File Statistics Dashboard
* Dark Mode Interface

---

## 👨‍💻 Author

**Harshid Panchal**

B.Sc. IT Graduate
M.Sc. IT (Data Science & AI + Full Stack Development) Student

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates future improvements.
