from pathlib import Path
import shutil

from core import LessonFactory


def setup(lesson_path):
    for name in Path(__file__).parent.glob('*'):
        if not name.is_dir():
            shutil.copy(name, Path(lesson_path) / name.name)
        else:
            shutil.copytree(name, Path(lesson_path) / name.name)


lesson = LessonFactory('incomplete_insecure_example', description='', setup=setup)
