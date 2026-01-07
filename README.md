# ASCII Art (TT PROJECT 2) 🎨🐍

A lightweight Python project that reconstructs and prints a large ASCII art image using **Run-Length Encoding (RLE)**. The project demonstrates basic data compression concepts, string processing, and clean terminal output.

---

📌 Project Overview

**Project Title:** ASCII Art using Run-Length Encoding
**Project Code:** TT PROJECT 2
**Language Used:** Python
**Output:** ASCII Art printed on terminal (stdout)

This project stores ASCII art in a compressed **RLE format** and reconstructs it at runtime. Instead of storing every character, it stores *(count, character)* pairs to reduce size and improve readability of large artworks.

---

 🎯 Objectives

* Understand **Run-Length Encoding (RLE)** as a basic compression technique
* Learn how to process structured text data in Python
* Practice string manipulation and iteration
* Generate large ASCII art efficiently

---

🧠 How It Works

1. **RLE_TEXT**

   * A triple-quoted string containing encoded data
   * Each entry represents how many times a character repeats

2. **Parsing Phase**

   * The RLE text is parsed into a list of tuples: `(count, character)`

3. **Reconstruction Phase**

   * The script expands each tuple
   * Characters are printed row-by-row to form the final ASCII art

---

🛠️ Technologies Used

* Python 3.x
* Standard Python libraries only
* Runs on any OS (Windows / Linux / macOS)

---

📂 Project Structure

```
ASCII-Art-TT-Project-2/
│
├── asciiart.py        # Main Python script
├── README.md          # Project documentation
└── RLE_TEXT (inside script)
```

---

 ▶️ How to Run the Project

🔧 Prerequisites

* Python 3 installed

 ▶️ Execution Command

```bash
python -u asciiart.py
```

The ASCII art will be printed directly in the terminal.

---

 ✏️ Editing the Artwork

You can customize the ASCII art easily:

* Open `asciiart.py`
* Modify the `RLE_TEXT` block
* Ensure the `(count, character)` format is preserved

Example:

```
5 *
3 #
10 .
```

 💡 Key Concepts Demonstrated

* Run-Length Encoding (RLE)
* Efficient storage of repetitive data
* String reconstruction
* Looping and parsing in Python

 ✅ Advantages

* Memory-efficient
* Easy to modify artwork
* Simple logic, beginner-friendly
* No external dependencies

🚀 Future Enhancements (Optional)

* Add file input/output support
* Add color using ANSI escape codes
* Support multiple ASCII artworks
* Convert image → ASCII → RLE automatically

👨‍🎓 Academic Use

This project is suitable for:

* Python mini project
* Data compression basics
* Terminal-based applications
* College practical / TT Project submission



📌 Author

**Avinash Thakur**
B.Tech (AI/ML)

