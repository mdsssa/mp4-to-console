#FILE TO START ONE OF THIS FILES IN CONSOLE

import os
print('c for cashed , r for render')
i = '1'
while i.lower() not in ['c' , 'r']:
    i = input().lower()
    if i.lower() == 'c':
        os.startfile('run_cached_animation.py')
    if i.lower() == 'r':
        os.startfile('mp4_to_text.py')
