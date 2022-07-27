import zipfile
from typing import List, Dict


class FileZipHelper(object):
    def __init__(self, src_path, dir_name, dir_path):
        self.src_path: List[str] = src_path
        self.dir_name: List[str] = dir_name
        self.dir_path = self._path(dir_path)

    @staticmethod
    def _path(path):
        if isinstance(path, list) and len(path) == 1:
            return path[0]
        return path

    def zipInit(self):
        # init zip
        res = zipfile.ZipFile(self.dir_path)

    def collect(self):
        for i, path in enumerate(self.src_path):
            ...


if __name__ == '__main__':
    args1 = ['1.txt', '2.txt', '3.jpg', '4.txt', '5.txt']
    args2 = ['1_.txt', '2_2.txt', '3_3.jpg', '4_.txt', '5_.txt']
    args3 = 'output'
