import os

from flask_bombril.r import R
from flask_bombril.utils import raise_with_stop


class UniqueFilename(object):
    def __init__(self, folder_full_path, message=R.string.unique_filename, stop=True):
        self.message = message
        self.folder_full_path = folder_full_path
        self.stop = stop

    def __call__(self, form, field):
        if callable(self.message):
            self.message = self.message()

        is_file = os.path.isfile(os.path.join(self.folder_full_path, field.data.filename))
        if is_file:
            raise_with_stop(self)
