# 🧠 Face Recognition & Room Access System

This is my first face recognition project using Python, OpenCV, and the face_recognition library. It allows users to register their face with a name and room access permissions, and later recognizes them via webcam and grants or denies access based on the room.

---

## 📂 Project Structure
.
├── face_recognition.py     # Script to register new faces  
├── main.py                 # Script to recognize faces and check room access  
├── registered_faces/       # Folder to store registered face encodings  
└── README.md               # Project documentation  

---

## 🚀 Features

- Register a person's face and define the rooms they have access to  
- Recognize faces using webcam input  
- Grant or deny access visually using colored rectangles (green for access, red for denial)  
- Save face encodings securely using pickle  

---

## 🔧 Requirements

Make sure you have Python installed, then run:
pip install opencv-python face_recognition

---

## ✅ How to Use

### 1. Register a Face

Run the following to register a new person:
python face_recognition.py

- Enter the person's name.  
- Enter the rooms they can access (comma-separated).  
- Press S to capture the face when ready.  
- Press Q to exit.  

Face data will be saved in the registered_faces/ folder.

---

### 2. Recognize and Grant/Deny Access

Run the main recognition system:
python main.py

- The webcam will open and recognize registered faces.  
- Displays:  
  - Name  
  - Access status  
  - Room name (currently generic "room")  

Press Q to quit.

---

## 📌 Notes

- Both scripts must be used together — registering faces before running the recognition script.  
- You can improve results by registering each person with multiple photos.  
- Make sure the webcam has good lighting during registration and recognition.
