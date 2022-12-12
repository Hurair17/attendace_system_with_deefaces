import cv2
import time
import os

def createdirectory(name):
    directory = name 
    # parent_dir = 'D:/JMM/00 IMAGES/'
    parent_dir = '/JMM/05 django/attendance/media/'
    path = parent_dir + directory
    # path = os.path.join(parent_dir, directory)
    print(path)
    try:
        os.mkdir(path)
        print(path)
        return path
    except:
        print('Failed')
        return 0
def takepicture(name):
    list_of_path = []
    path = createdirectory(name)
    # path = '/JMM/05 django/attendance/media/'
    if path != 0:
        cam = cv2.VideoCapture(0)
        cv2.namedWindow(name)
        img_counter = 0
        font = cv2.FONT_HERSHEY_SIMPLEX
        while True:
            ret, frame = cam.read()
            cv2.putText(frame, 
                        'Image {}'.format(img_counter), 
                        (50, 50), 
                        font, 1, 
                        (0, 255, 255), 
                        2, 
                        cv2.LINE_4)
            if not ret:
                print("failed to grab frame")
                break
            cv2.imshow(name, frame)

            k = cv2.waitKey(1)
            if k%256 == 113:
                # ESC pressed
                print("Escape hit, closing...")
                break
            elif k%256 == 32:
                # SPACE pressed
                img_name = "{}/{}_{}.jpg".format(path,name,img_counter)
                cv2.imwrite(img_name, frame)
                list_of_path.append(img_name)
                print("{} written!".format(img_name))
                img_counter += 1
        cam.release()
        cv2.destroyAllWindows()
        return list_of_path,name
    else:
        print('This person already excit')
        return '',''
        


