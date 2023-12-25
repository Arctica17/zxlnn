import cv2
import numpy as np

cap_basic = cv2.VideoCapture('BasicScene.mp4')
cap_text = cv2.VideoCapture('TextScene.mp4')

length_basic = int(cap_basic.get(cv2.CAP_PROP_FRAME_COUNT))
length_text = int(cap_text.get(cv2.CAP_PROP_FRAME_COUNT))
max_length = max(length_basic, length_text)

frame_width = int(cap_basic.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap_basic.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = max(cap_basic.get(cv2.CAP_PROP_FPS), cap_text.get(cv2.CAP_PROP_FPS))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('CNN_visualization.mp4', fourcc, fps, (frame_width, frame_height), True)

frame_count = 0
while frame_count < max_length:
    ret_basic, frame_basic = cap_basic.read()
    ret_text, frame_text = cap_text.read()

    if not ret_basic and frame_count < length_basic:
        frame_basic = np.zeros((frame_height, frame_width, 3), dtype=np.uint8)
    if not ret_text and frame_count < length_text:
        frame_text = np.zeros((frame_height, frame_width, 3), dtype=np.uint8)

    if ret_text:
        gray_text = cv2.cvtColor(frame_text, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(gray_text, 180, 255, cv2.THRESH_BINARY) 

        mask_inv = cv2.bitwise_not(mask)
        white_text = cv2.bitwise_and(frame_text, frame_text, mask=mask)

        frame_basic_masked = cv2.bitwise_and(frame_basic, frame_basic, mask=mask_inv)
        frame_combined = cv2.add(frame_basic_masked, white_text)

        out.write(frame_combined)
    else:
        out.write(frame_basic)

    frame_count += 1

cap_basic.release()
cap_text.release()
out.release()
