# import os
# import cv2
# import matplotlib.pyplot as plt
# import numpy as np
# import dlib

# my_image_path = os.path.dirname(__file__) +'/images/Image.png' # os.path.driname(__file__)
# my_image_path_encode= np.fromfile(my_image_path, np.uint8)
# img_bgr = cv2.imdecode(my_image_path_encode,cv2.IMREAD_UNCHANGED)    # OpenCV로 이미지를 불러옵니다
# img_show = img_bgr.copy()      # 출력용 이미지를 따로 보관합니다

# plt.imshow(img_bgr)
# plt.show()


# # Section 3
# # SVG detector를 선언합니다
# detector_hog = dlib.get_frontal_face_detector()

# # Bounding box 추출
# img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
# dlib_rects = detector_hog(img_rgb, 1)   # (image, num of image pyramid)

# for dlib_rect in dlib_rects:
#     l = dlib_rect.left()
#     t = dlib_rect.top()
#     r = dlib_rect.right()
#     b = dlib_rect.bottom()

#     cv2.rectangle(img_show, (l,t), (r,b), (0,255,0), 2, lineType=cv2.LINE_AA)

# img_show_rgb =  cv2.cvtColor(img_show, cv2.COLOR_BGR2RGB)
# plt.imshow(img_show_rgb)
# plt.show()


# # Section 4
# # LandMark 찍기
# model_path = os.path.dirname(__file__) + '/models/shape_predictor_68_face_landmarks.dat'
# landmark_predictor = dlib.shape_predictor(model_path)

# list_landmarks = []

# # 얼굴 영역 박스 마다 face landmark를 찾아냅니다
# for dlib_rect in dlib_rects:
#     points = landmark_predictor(img_rgb, dlib_rect)
#     # face landmark 좌표를 저장해둡니다
#     list_points = list(map(lambda p: (p.x, p.y), points.parts()))
#     list_landmarks.append(list_points)


# # Section 5
# # LandMark 출력
# for landmark in list_landmarks:
#     for point in landmark:
#         cv2.circle(img_show, point, 2, (0, 255, 255), -1)

# img_show_rgb = cv2.cvtColor(img_show, cv2.COLOR_BGR2RGB)
# plt.imshow(img_show_rgb)
# plt.show()


# # Section 6
# # 스티커 위치 구하기
# for dlib_rect, landmark in zip(dlib_rects, list_landmarks):
#     x = landmark[30][0]
#     y = landmark[30][1] - dlib_rect.height()//2
#     w = h = dlib_rect.width()

# # 스티커 사이즈 조절
# sticker_path = os.path.dirname(__file__) + '/images/king.png'
# img_sticker = cv2.imread(sticker_path) # 스티커 이미지를 불러옵니다
# img_sticker = cv2.resize(img_sticker, (w,h))

# # 스티커위치 조정
# refined_x = x - w // 2
# refined_y = y - h

# # 스티커 위치 넘어가면 잘리게
# if refined_x < 0:
#     img_sticker = img_sticker[:, -refined_x:]
#     refined_x = 0
# if refined_y < 0:
#     img_sticker = img_sticker[-refined_y:, :]
#     refined_y = 0

# # 사진에 적용후 출력
# sticker_area = img_bgr[refined_y:refined_y +img_sticker.shape[0], refined_x:refined_x+img_sticker.shape[1]]
# img_bgr[refined_y:refined_y +img_sticker.shape[0], refined_x:refined_x+img_sticker.shape[1]] = \
#     np.where(img_sticker==0,sticker_area,img_sticker).astype(np.uint8)

# plt.imshow(cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB))
# plt.show()


import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
import dlib
import base64

file_dir = os.path.dirname(__file__)

def stickerGen(img):
    img_bgr = cv2.imdecode(np.fromstring(img, np.uint8), cv2.IMREAD_UNCHANGED)
    detector_hog = dlib.get_frontal_face_detector()

    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    dlib_rects = detector_hog(img_rgb, 1)

    model_path = file_dir+'/models/shape_predictor_68_face_landmarks.dat'
    landmark_predictor = dlib.shape_predictor(model_path)

    list_landmarks = []

    for dlib_rect in dlib_rects:
        points = landmark_predictor(img_rgb, dlib_rect)
        list_points = list(map(lambda p: (p.x, p.y), points.parts()))
        list_landmarks.append(list_points)

    for dlib_rect, landmark in zip(dlib_rects, list_landmarks):
        x = landmark[30][0]
        y = landmark[30][1] - dlib_rect.height()//2
        w = h = dlib_rect.width()

    sticker_path = file_dir+'/images/king.png'
    img_sticker = cv2.imread(sticker_path)
    img_sticker = cv2.resize(img_sticker, (w,h))

    refined_x = x - w // 2
    refined_y = y - h

    if refined_x < 0:
        img_sticker = img_sticker[:, -refined_x:]
        refined_x = 0
    if refined_y < 0:
        img_sticker = img_sticker[-refined_y:, :]
        refined_y = 0

    sticker_area = img_bgr[refined_y:refined_y +img_sticker.shape[0], refined_x:refined_x+img_sticker.shape[1]]
    img_bgr[refined_y:refined_y +img_sticker.shape[0], refined_x:refined_x+img_sticker.shape[1]] = \
        np.where(img_sticker==0,sticker_area,img_sticker).astype(np.uint8)

    img_bgr_buffer= cv2.imencode('.jpg', img_bgr)[1]
    result = base64.b64encode(img_bgr_buffer).decode("utf-8")
    return result
