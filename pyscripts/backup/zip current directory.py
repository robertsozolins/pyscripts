import shutil
import os

from datetime import date
def backupnow():
    backup(os.getcwd(), f'Backup {date.today()}.zip')

def backup(source, destination):
    base = os.path.basename(destination)
    name = base.split('.')[0]
    format = base.split('.')[1]
    archive_from = os.path.dirname(source)
    archive_to = os.path.basename(source.strip(os.sep))
    shutil.make_archive(name, format, archive_from, archive_to)
    shutil.move('%s.%s' % (name, format), destination)

def main():
    backupnow()

if __name__ == '__main__':
    main()
