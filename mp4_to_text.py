
import cv2
import os
import time
#width and height to resize
width = 155
height = 60
dir_lengh = len(os.listdir())
cache = False
print('Hi there! to start the program - write "t" here , for toggle cache option write "cache"')
console_com = input()
while console_com != 't':
    if console_com == 'cache':
        cache = not cache
        print(f'cache status : {cache}')
    console_com = input()
start_time = time.time()
frames = 0

def pixel_to_char(pixel_value):
    chars = ['@','%', '#', '*', '+', '=', '-', ':', '.', ' ']
    index_ = int(pixel_value / 255 * (len(chars) - 1))
    return chars[index_]

def frame_to_text(frame, width=width, height=height):
    frame_resized = cv2.resize(frame, (width, height))
    text_frame = ""
    for row in frame_resized:
        for pixel in row:
            text_frame += pixel_to_char(pixel)
        text_frame += "\n"
    return text_frame

def video_to_console(video_path, width=width, height=height):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("can't load a video")
        return
    print(cap.isOpened())
    os.system('cls' if os.name == 'nt' else 'clear')
    while cap.isOpened():
        r , frame = cap.read()
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        text_frame = frame_to_text(gray_frame, width, height)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(text_frame)
        global cache , frames , dir_lengh
        if cache:
            with open(f'./cached_animation{dir_lengh}.txt' , 'a') as file:
                file.write(f'{text_frame}\nSplit\n')
        frames += 1
        fps = round(frames / (time.time() - start_time) , 6) if time.time() - start_time else round(frames * (time.time() - start_time) , 6)
        timee = round(time.time() - start_time , 6)
        maxi = max([len(str(fps))+ len('FPS : '), len(str(timee)) + len('Time : ')])
        print('-*' * round(maxi/2) + '-')
        print(f'''Time : {timee}\nFPS : {fps}\nFrames : {frames}\nCashing rn : {cache}''')
        print('-*' * round(maxi / 2) + '-')
        time.sleep(0.05)
    cap.release()
if __name__ == "__main__":
    #path
    video_path = 'Path to video?'
    video_to_console(video_path)


