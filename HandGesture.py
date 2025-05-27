import cv2
import time
import numpy as np
import mediapipe as mp
from datetime import datetime

# Define HandDetector class
class HandDetector:
    def __init__(self, mode=False, max_hands=2, detection_confidence=0.5, tracking_confidence=0.5):
        self.mode = mode
        self.max_hands = max_hands
        self.detection_confidence = detection_confidence
        self.tracking_confidence = tracking_confidence
        
        # Initialize MediaPipe hands module
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.max_hands,
            min_detection_confidence=self.detection_confidence,
            min_tracking_confidence=self.tracking_confidence
        )
        self.mp_draw = mp.solutions.drawing_utils
        self.tip_ids = [4, 8, 12, 16, 20]

    def find_hands(self, img, draw=True):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(img_rgb)
        if self.results.multi_hand_landmarks:
            for hand_lms in self.results.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(img, hand_lms, self.mp_hands.HAND_CONNECTIONS)
        return img

    def find_position(self, img, hand_no=0, draw=True):
        lm_list = []
        if self.results.multi_hand_landmarks:
            my_hand = self.results.multi_hand_landmarks[hand_no]
            for id, lm in enumerate(my_hand.landmark):
                h, w, _ = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
        return lm_list


# Constants for camera width and height
wCam, hCam = 1080, 720

# Capture video from the camera
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
detector = HandDetector(detection_confidence=0.7)
pTime = 0

while True:
    success, img = cap.read()
    if not success:
        print("Failed to read frame from camera. Skipping this frame...")
        continue

    img = detector.find_hands(img)
    lm_list = detector.find_position(img)

    if len(lm_list) != 0:
        # Thumb and index finger coordinates
        x1, y1 = lm_list[4][1], lm_list[4][2]
        x2, y2 = lm_list[8][1], lm_list[8][2]
        length = np.hypot(x2 - x1, y2 - y1)

        # Detect if thumb and index finger are close
        if length < 20:
            # Countdown for photo capture
            for countdown in range(3, 0, -1):
                img_copy = img.copy()
                cv2.putText(img_copy, f'Capturing in {countdown}', (150, 200),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)
                cv2.imshow("Hand Gesture Recognition", img_copy)
                cv2.waitKey(1000)

            # Capture the new image after countdown
            ret, captured_img = cap.read()
            if ret:
                # Save the captured image
                timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                photo_filename = f'Photo_{timestamp}.jpg'
                cv2.imwrite(photo_filename, captured_img)
                print(f"Photo captured and saved as {photo_filename}")
            else:
                print("Failed to capture image after countdown.")

    # Calculate and display FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

    # Display the image
    cv2.imshow("Hand Gesture Recognition", img)
    
    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release camera and destroy all OpenCV windows
cap.release()
cv2.destroyAllWindows()
