#Spot's Vision System... utilizes OpenCV to take in the world around them...
import cv2  

CAMERA_PORT = 701 #set the desired camera by their ID number... 

def read_cameras():
    '''Reads the current cameras in the Local Machine, and prints/returns a String dictinary of cameras and their associated IDs).
    This is helpful for indicating the camera that the Quadruped will see out of when conducting Computer Vision processing.
    
    #CAMERA PORT NUMBERS ON GRETA'S VIRTUAL MACHINE...
        #1400: Integrated Camera
        #700: Integrated Camera
        #701: Twitch Virtual Cam (USB CAMERA!!!!)'''
    
    from cv2_enumerate_cameras import enumerate_cameras
    for camera_info in enumerate_cameras():
        print(f'{camera_info.index}: {camera_info.name}')
        return camera_info

def blink():
    '''Captures and returns an Image taken on the camera_port indicated at the top of the file.'''
    cap = cv2.VideoCapture(CAMERA_PORT) 
    result, image = cap.read() 
    if result: 
        return image
    else:
        #if captured image is corrupted, throws a helpful error 
        raise FileNotFoundError("No image detected. Maybe the camera did not read the image properly...Please try again!") 
    
def stare():
    '''Starts streaming LIVE from the camera_port indicated at the top of the file.'''
    #needs some work, but its not necessary for the MVP for now...

def memorize(image):
    '''If given an image, commits the image to memory... by saving it locally, of course.'''
    cv2.imwrite("short_term_memory.png", image)
    return 0

if __name__ == "__main__":
    print("I got eyes! I got eyes!")
    print("Say cheeeeeese!!")
    current_view = blink()
    cv2.imshow('Look, its you!!',current_view)
    print("Press any key to close the demo.")
    cv2.waitKey(0)
    
    
