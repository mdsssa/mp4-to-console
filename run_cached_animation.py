import time
import os

class Animation:
    def __init__(self):
        self.delay = None
        self.start_time = None
        self.file = None
    def run_it(self):
        frames = 0
        for text_frame in self.file:
            print(text_frame)
            frames += 1
            fps = round(frames / (time.time() - self.start_time), 6) if time.time() - self.start_time else round(
                frames * (time.time() - self.start_time), 6)
            timee = round(time.time() - self.start_time, 6)
            maxi = max([len(str(fps)) + len('FPS : '), len(str(timee)) + len('Time : ')])
            print('-*' * round(maxi / 2) + '-')
            print(f'''Time : {timee}\nFPS : {fps}\nFrames : {frames}''')
            time.sleep(self.delay)
            os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    anima = Animation()
    #path to txt with frames
    anima.file = open('cached_animation4.txt' , 'r').read().split('Split')
    #float delay between frames
    anima.delay = 0.04
    anima.start_time = time.time()
    anima.run_it()