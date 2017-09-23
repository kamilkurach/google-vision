from PIL import Image, ImageDraw
from google.cloud import vision
from google.cloud.vision import types, client
from oauth2client.client import GoogleCredentials
import json
from processjson import Processor
import os

class Vision:

    def detect_face(self, face_file, max_results=4):
        """Uses the Vision API to detect faces in the given file.
        Args:
            face_file: A file-like object containing an image with faces.
        Returns:
            An array of Face objects with information about the picture.
        """
        # [START get_vision_service]
        client = vision.ImageAnnotatorClient()
        # [END get_vision_service]

        content = face_file.read()
        image = types.Image(content=content)

        #request = {'image': {'source': {'image_uri': '{}'.format(url)},},}

        return client.face_detection(image=image).face_annotations



def main():
    max_results=1
    input_filename = '/home/slippy/Dokumenty/face.jpg'
    v = Vision()
    with open(input_filename, 'rb') as image:
        face = v.detect_face(image, max_results)
        s_face = str(face)
        f = open('test.txt', 'w')
        f.write(s_face)
        f.close()

        if os.path.isfile('test.txt'):
            file = open('test.txt')
            p = Processor(file)
            print(p.get_joy_value())
            print(p.get_sorrow_value())
            print(p.get_anger_value())
            print(p.get_surprise_value())
            print(p.get_underexposed_value())
            print(p.get_blurred_value())
            print(p.get_headwear_value())

if __name__ == '__main__':
    main()