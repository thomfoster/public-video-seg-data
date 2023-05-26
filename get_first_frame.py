import sys
import cv2
import os

def mp4_to_images(mp4_path):

    # Open the video file
    video = cv2.VideoCapture(mp4_path)

    success, frame = video.read()

    image_path = mp4_path.split('.')[0] + '.jpg'
    cv2.imwrite(image_path, frame)

    # Release the video file
    video.release()


# Example usage
mp4_path = sys.argv[1]

mp4_to_images(mp4_path)


