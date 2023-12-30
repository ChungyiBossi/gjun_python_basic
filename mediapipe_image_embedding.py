import cv2
import math
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import time

DESIRED_HEIGHT = 480
DESIRED_WIDTH = 480

def resize_and_show(image):
  h, w = image.shape[:2]
  if h < w:
    img = cv2.resize(image, (DESIRED_WIDTH, math.floor(h/(w/DESIRED_WIDTH))))
  else:
    img = cv2.resize(image, (math.floor(w/(h/DESIRED_HEIGHT)), DESIRED_HEIGHT))
  cv2.imshow(img)

def load_image_embedding_model(model_name):
    # Create options for Image Embedder
    base_options = python.BaseOptions(model_asset_path=model_name)
    l2_normalize = True #@param {type:"boolean"}
    quantize = True #@param {type:"boolean"}
    options = vision.ImageEmbedderOptions(
        base_options=base_options,
        l2_normalize=l2_normalize,
        quantize=quantize
    )  
   
    image_embedder = vision.ImageEmbedder.create_from_options(options)
    return image_embedder
      
def opencv_detect_faces(np_image, face_cascade_model, output_folder='.'):
    face_filenames = list()
    faces_bbox_from_image = face_cascade_model.detectMultiScale(cv2.cvtColor(np_image, cv2.COLOR_RGB2GRAY))    # 偵測人臉一
    if len(faces_bbox_from_image):
        for bbox in faces_bbox_from_image:
          x, y, w, h = bbox
          cv2.rectangle(np_image, (x, y), (x+w, y+h), color=(0, 255, 255))
          filename = f'{output_folder}/face_{time.time()}.jpg'
          face_filenames.append(filename)
          cv2.imwrite(filename, np_image[y:y+h, x:x+w, ::]) # 座標是相反的, 先給y再給x, 拿原來的圖去取臉部
          cv2.imshow('first', np_image)
          cv2.waitKey(1000)

    return faces_bbox_from_image, face_filenames

if __name__ == '__main__':
    # model url : https://storage.googleapis.com/mediapipe-models/image_embedder/mobilenet_v3_small/float32/1/mobilenet_v3_small.tflite

    # Format images for MediaPipe
    IMAGE_FILENAMES = ['jay_1.jpg', 'fake_jay.jpg']
    first_image = cv2.imread(IMAGE_FILENAMES[0])
    second_image = cv2.imread(IMAGE_FILENAMES[1])

    # 偵測臉部, 回傳bounding box & 臉部擷取的存檔 filename
    face_cascade = cv2.CascadeClassifier(".\python_scripts\haarcascade_frontalface_default.xml")   # 載入人臉模型
    bboxes_1, facefilename_1 = opencv_detect_faces(first_image, face_cascade, './face_image')
    bboxes_2, facefilename_2 = opencv_detect_faces(second_image, face_cascade, './face_image')
    
    # Create Image Embedder
    with load_image_embedding_model('mobilenet_v3_small.tflite') as embedder:
        # read files as mediapipe Image object
        first_image = mp.Image.create_from_file(facefilename_1[0])
        second_image = mp.Image.create_from_file(facefilename_2[0])
        first_embedding_result = embedder.embed(first_image)
        second_embedding_result = embedder.embed(second_image)

        # Calculate and print similarity
        similarity = vision.ImageEmbedder.cosine_similarity(
            first_embedding_result.embeddings[0],
            second_embedding_result.embeddings[0]
        )
        print(similarity)