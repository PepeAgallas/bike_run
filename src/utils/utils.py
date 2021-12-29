import os


def load_file(path, filename):
    directory = os.path.dirname(path)
    file = os.path.join(directory, filename)

    return file
