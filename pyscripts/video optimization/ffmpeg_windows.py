import subprocess
import os
import fnmatch
from pathlib import Path


def checkfolder(destination=os.walk(os.path.dirname(os.path.abspath(__file__)))):
    for root, dirs, files in destination:
        for num, file in enumerate(files, 1):
            try:
                current_file = os.path.join(root, file)
                if os.path.isfile(current_file):
                    filename, extension = os.path.splitext(current_file)
                    if extension.lower() in ('.avi', '.mp4', '.mkv', '.flv', '.wmv', '.mpg', '.mkv', '.webm'):
                        if fnmatch.fnmatch(filename, '*_optimized'):
                            print(f'\r Already optimized --- {file[:50]} '),
                        else:
                            compress(filename, extension)
            except IOError:
                print(f'{file}: <--- Error')
    print(' Optimization complete')


def main():
    checkfolder()
    return


def compress(file, extension):
    # uses https://ffmpeg.zeranoe.com/builds/win64/static/ffmpeg-20190217-9326117-win64-static.zip
    command = Path('A:/ffmeg/bin/ffmpeg.exe -i')
    filename = Path(file)
    subprocess.run(f'{command} "{filename}{extension}" "{filename}_optimized.mp4"', shell=False)
    os.remove(f'{filename}{extension}')


if __name__ == '__main__':
    main()
