from PIL import Image
import os, sys, shutil
from datetime import datetime


def status(iteration, total, prefix='', suffix='', decimals=1, bar_length=100):
    percents = f'{100 * (iteration / float(total)):.2f}'
    filled_length = int(round(bar_length * iteration / float(total)))
    bar = f'{"#" * filled_length}{"-" * (bar_length - filled_length)}'
    sys.stdout.write(f'\r{prefix} |{bar}| {percents}% {suffix}'),
    sys.stdout.flush()


def make_archive(source, destination):
    base = os.path.basename(destination)
    name = base.split('.')[0]
    format = base.split('.')[1]
    archive_from = os.path.dirname(source)
    archive_to = os.path.basename(source.strip(os.sep))
    shutil.make_archive(name, format, archive_from, archive_to)
    shutil.move('%s.%s' % (name, format), destination)


def getFolderSize(p):
    from functools import partial
    prepend = partial(os.path.join, p)
    return sum([(os.path.getsize(f) if os.path.isfile(f) else getFolderSize(f)) for f in map(prepend, os.listdir(p))])


def human(size):
    B = "B"
    KB = "KB"
    MB = "MB"
    GB = "GB"
    TB = "TB"
    UNITS = [B, KB, MB, GB, TB]
    HUMANFMT = "%f %s"
    HUMANRADIX = 1024.
    for u in UNITS[:-1]:
        if size < HUMANRADIX: return HUMANFMT % (size, u)
        size /= HUMANRADIX
    return HUMANFMT % (size, UNITS[-1])


def init():
    global cwd, size, tstart, size_initial, size_backup
    tstart = datetime.now()
    cwd = os.path.dirname(os.path.abspath(__file__))
    size = (1920, 1080)
    size_initial = getFolderSize(os.getcwd())
    size_backup = 0


def backup():
    global today, size_backup
    sys.stdout.write('Starting backup..')
    today = date.today()
    make_archive(cwd, f'Backup {today}.zip')
    size_backup = getFolderSize(os.getcwd()) - size_initial


def optimize():
    global size_final, tend
    for root, dirs, files in os.walk(cwd):
        statuslenght = len(files)
        current_dir = root.split("\\")
        for num, file in enumerate(files, 1):
            try:
                current_file = os.path.join(root, file)
                if os.path.isfile(current_file):
                    filename, extension = os.path.splitext(current_file)
                    if extension.lower() in ('.jpg', '.jpeg', '.png'):
                        im = Image.open(current_file)
                        im.thumbnail(size)
                        im.save(f'{filename}{extension}', optimize=True, quality=75, compress_level=9)
                        status(num, statuslenght, f'\r{current_dir[-1]}--> {file[:15]}: {num} / {statuslenght}', 'Complete', 1, 50)
            except IOError:
                print(f'{file}: <--- Error')
    size_final = getFolderSize(os.getcwd())
    tend = datetime.now()

def stats():
    print('-----------------------------------')
    print(f'Uncompressed: {human(size_initial)}')
    print(f'Optimized: {human(size_final - size_backup)}')
    print(f'Saved: {human((size_final - size_initial - size_backup))}')
    print(f'Backup: {human(size_backup)}')
    print('-----------------------------------')
    print(f'Executed: {tend - tstart}')

def main():
    init()
    backup()
    optimize()
    stats()

if __name__ == '__main__':
    main()
