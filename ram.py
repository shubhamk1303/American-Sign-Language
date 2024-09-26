# # from tensorflow.keras.models import Sequential
# from keras.models import Sequential
# from keras.layers import LSTM, Dense, Dropout
# import cv2
# import numpy as np
# import os
# from matplotlib import pyplot as plt
# import time
# import mediapipe as mp
#
import requests
url="https://www.1mg.com/otc/tata-1mg-calcium-vitamin-d3-zinc-magnesium-and-alfalfa-tablet-joint-support-bones-health-immunity-energy-support-otc536094"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
}
cookie={
    'eta_pincode':'147001'
}
res=requests.get(url,headers,cookies=cookie)
print(res.content)
# mp_holistic = mp.solutions.holistic # Holistic model
# mp_drawing = mp.solutions.drawing_utils # Drawing utilities
#
#
# actions = np.array(['hello', 'thanks', 'iloveyou','sorry','help','fine','pray','money','yes','no','stand'])
#
# # Thirty videos worth of data
# no_sequences = 30
#
# # Videos are going to be 30 frames in length
# sequence_length = 30
#
# # Folder start
# start_folder = 1
#
# model = Sequential()
# model.add(LSTM(64, return_sequences=True, activation='relu', input_shape=(30,1662)))
# model.add(LSTM(128, return_sequences=True, activation='relu'))
# model.add(LSTM(128, return_sequences=True, activation='sigmoid'))
# model.add(LSTM(64, return_sequences=False, activation='relu'))
# model.add(Dense(64, activation='relu'))
# model.add(Dense(32, activation='relu'))
# model.add(Dense(actions.shape[0], activation='softmax'))
# model.load_weights('./models/action.h5')
#
#
#
#
#
#
#
# #functions
# def extract_keypoints(results):
#     pose = np.array([[res.x, res.y, res.z, res.visibility] for res in results.pose_landmarks.landmark]).flatten() if results.pose_landmarks else np.zeros(33*4)
#     face = np.array([[res.x, res.y, res.z] for res in results.face_landmarks.landmark]).flatten() if results.face_landmarks else np.zeros(468*3)
#     lh = np.array([[res.x, res.y, res.z] for res in results.left_hand_landmarks.landmark]).flatten() if results.left_hand_landmarks else np.zeros(21*3)
#     rh = np.array([[res.x, res.y, res.z] for res in results.right_hand_landmarks.landmark]).flatten() if results.right_hand_landmarks else np.zeros(21*3)
#     return np.concatenate([pose, face, lh, rh])
#
# def draw_landmarks(image, results):
#     mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACEMESH_CONTOURS) # Draw face connections
#     mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS) # Draw pose connections
#     mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS) # Draw left hand connections
#     mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS) # Draw right hand connections
#
# def mediapipe_detection(image, model):
#     if image is None :
#         return image,None
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # COLOR CONVERSION BGR 2 RGB
#     image.flags.writeable = False                  # Image is no longer writeable
#     results = model.process(image)                 # Make prediction
#     image.flags.writeable = True                   # Image is now writeable
#     image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) # COLOR COVERSION RGB 2 BGR
#     return image, results
#
#
#
#
#
#
#
#
# def process_video(video_path):
#     sequence = []
#     sentence = []
#     predictions = []
#     threshold = 0.60
#     cap = cv2.VideoCapture(video_path)
#     # Set mediapipe model
#     with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
#         while cap.isOpened():
#
#             # Read feed
#             ret, frame = cap.read()
#
#             # Make detections
#             image, results = mediapipe_detection(frame, holistic)
#             # print(results)
#             if results is None:
#                 return sentence
#             # 2. Prediction logic
#             keypoints = extract_keypoints(results)
#             sequence.append(keypoints)
#             sequence = sequence[-30:]
#
#             if len(sequence) == 30:
#                 res = model.predict(np.expand_dims(sequence, axis=0))[0]
#                 print(actions[np.argmax(res)])
#                 predictions.append(np.argmax(res))
#
#                 # 3. Viz logic
#                 if np.unique(predictions[-10:])[0] == np.argmax(res):
#                     if res[np.argmax(res)] > threshold:
#
#                         if len(sentence) > 0:
#                             if actions[np.argmax(res)] != sentence[-1]:
#                                 sentence.append(actions[np.argmax(res)])
#                         else:
#                             sentence.append(actions[np.argmax(res)])
#
#                 if len(sentence) > 1:
#                     return sentence
#
#                 # Viz probabilities
#         #         image = prob_viz(res, actions, image, colors)
#         #
#         #     cv2.rectangle(image, (0, 0), (640, 40), (245, 117, 16), -1)
#         #     cv2.putText(image, ' '.join(sentence), (3, 30),
#         #                 cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
#         #
#         #     # Show to screen
#         #     cv2.imshow('OpenCV Feed', image)
#         #
#         #     # Break gracefully
#         #     if cv2.waitKey(10) & 0xFF == ord('q'):
#         #         break
#         # cap.release()
#         cv2.destroyAllWindows()
#
#
# def signtotext():
#     video_path = "./static/recorded-video.webm"
#     output_text = process_video(video_path)
#     print("Final Output Text:", output_text)
#     if(len(output_text)==0):
#         return "try again"
#     return output_text;