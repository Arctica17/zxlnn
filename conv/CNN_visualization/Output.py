import cv2

cap_basic = cv2.VideoCapture('BasicScene.mp4')
cap_text = cv2.VideoCapture('TextScene.mp4')


frame_width = int(cap_basic.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap_basic.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap_basic.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('CNN_visualization.mp4', fourcc, fps, (frame_width, frame_height), True)

while True:
    ret_basic, frame_basic = cap_basic.read()
    ret_text, frame_text = cap_text.read()

    if not ret_basic or not ret_text:
        break

    gray_text = cv2.cvtColor(frame_text, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray_text, 200, 255, cv2.THRESH_BINARY)

    mask_inv = cv2.bitwise_not(mask)
    white_text = cv2.bitwise_and(frame_text, frame_text, mask=mask)

    frame_basic_masked = cv2.bitwise_and(frame_basic, frame_basic, mask=mask_inv)
    frame_combined = cv2.add(frame_basic_masked, white_text)

    out.write(frame_combined)

cap_basic.release()
cap_text.release()
out.release()
