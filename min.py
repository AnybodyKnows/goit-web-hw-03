from thread import Thread
import logging
import pathlib
import shutil


def sort_files(source_dir, target_dir):
    logging.info('Sorting files...')
    for file in pathlib.Path(source_dir).iterdir():
        if file.is_dir():
            sort_files(file, target_dir)
        else:
            file_type = file.suffix
            if file_type == ".jpg":
                target_file = f"{target_dir}\\jpg\\{file.name}"
                shutil.copy(str(file), target_file)
            elif file_type == ".png":
                target_file = f"{target_dir}\\png\\{file.name}"
                shutil.copy(str(file), target_file)
            elif file_type == ".svg":

                target_file = f"{target_dir}\\svg\\{file.name}"
                shutil.copy(str(file), target_file)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    sort_files(pathlib.Path("picture"), pathlib.Path("dist"))
    logging.info('Done!')
