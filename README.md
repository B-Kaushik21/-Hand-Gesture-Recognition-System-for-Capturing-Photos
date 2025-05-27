# ✋ Hand-Gesture-Recognition-System-for-Capturing-Photos

This project uses a webcam and **MediaPipe** to detect hand gestures in real time. It specifically detects when the **thumb and index finger touch** and automatically captures a photo with a countdown timer.

---

## 🧠 Features

- Real-time hand tracking using **MediaPipe**
- Detects **thumb-index finger pinch gesture**
- Captures and saves a photo when gesture is detected
- Displays **FPS** for performance tracking
- Adds a 3-second countdown overlay before capturing the photo

---

## 📷 Demo

> ✨ Live detection of hand gesture  
> ⏱ Countdown displayed  
> 🖼 Photo saved as `Photo_YYYY-MM-DD_HH-MM-SS.jpg`

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/B-Kaushik21/Hand-Gesture-Recognition-System-for-Capturing-Photos.git
cd <REPO-NAME>
```

### 2. Install Dependencies

Make sure you have Python installed (preferably 3.7+). Then install:

```bash
pip install opencv-python mediapipe numpy
```

### 3. Run the Script

```bash
python HandGesture.py
```

Press `q` to quit the program anytime.

---

## 📂 Project Structure

```
HandGesture.py      # Main script for hand detection and image capture
README.md           # Project overview and instructions
```

---

## 📌 How It Works

1. Webcam captures real-time video
2. MediaPipe detects hand landmarks
3. Detects pinch (distance between thumb tip and index tip < 20 px)
4. Starts 3-second countdown overlay
5. Captures and saves photo with timestamp

---

## 🛠 Technologies Used

- Python
- OpenCV
- MediaPipe (Google)
- NumPy

---

## 💡 Future Enhancements

- Add gesture-based controls for video recording or other actions
- Save photos to a dedicated folder
- Add GUI using Tkinter or PyQt
- Integrate with a web application using Flask or Streamlit

---

## 🙋‍♂️ Author

**B. Kaushik**  
[GitHub Profile](https://github.com/B-Kaushik21)

---

## 📜 License

This project is licensed under the MIT License – feel free to use and modify!
