from PIL import Image
import os
import fnmatch

def optimize(width, height, foldername):
    if not os.path.isdir(f'{width}{height}'):
        #print(f'{width}{height} directry has been created')
        os.system(f'mkdir {foldername}')
    cwd = os.path.dirname(os.path.abspath(__file__))
    for root, dirs, files in os.walk(cwd):
        for extension in ['jpg', 'jpeg', 'png']:
            for f in fnmatch.filter(files, '*.' + extension):
                try:
                    i = Image.open(f)
                    fn, fext = os.path.splitext(f)
                    i.thumbnail((width, height))
                    i.save(f'{foldername}/{fn}{fext}')
                except IOError:
                    print(f'{f}: <--- Error')

def main():
    optimize(1920, 1080, 'optim_1920')
    optimize(970, 970, 'optim_970')
    optimize(300, 300, 'optim_300')
    optimize(150, 150, 'optim_150')


if __name__ == '__main__':
    main()
    
