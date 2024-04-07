from thread import Thread
import logging
import pathlib
import shutil


def create_folder(folder: str):
    if not pathlib.Path(folder).exists():
        folder_name = pathlib.Path(folder)
        folder_name.mkdir(parents=True, exist_ok=True)
    else:
        pass


def sort_files(source_dir, target_dir):
    logging.info('Sorting files...')
    for file in pathlib.Path(source_dir).iterdir():
        if file.is_dir():
            thread = Thread(target=sort_files, args=(file, target_dir))
            thread.start()

        else:
            file_type = file.suffix
            if file_type == ".jpg":
                create_folder(f"{target_dir.name}\\jpg")
                target_file = f"{target_dir}\\jpg\\{file.name}"
                shutil.copy(str(file), target_file)

            elif file_type == ".png":
                create_folder(f"{target_dir.name}\\png")
                target_file = f"{target_dir}\\png\\{file.name}"
                shutil.copy(str(file), target_file)

            elif file_type == ".svg":
                create_folder(f"{target_dir.name}\\svg")
                target_file = f"{target_dir}\\svg\\{file.name}"
                shutil.copy(str(file), target_file)



if __name__ == '__main__':
    if pathlib.Path('dist').exists():
        shutil.rmtree(pathlib.Path('dist'))

    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    sort_files(pathlib.Path("picture"), pathlib.Path("dist"))
    logging.info('Done!')


