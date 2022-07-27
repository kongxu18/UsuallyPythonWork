import zipfile, os
from typing import List, Dict
from zipfile import ZIP_STORED, ZIP_DEFLATED


class FileZipHelper(object):
    def __init__(self, src_path, dir_name, dir_path):
        self.src_path: List[str] = src_path
        self.dir_name: List[str] = dir_name
        self.dir_path = self._path(dir_path)
        self.err = []

    @staticmethod
    def _path(path):
        if isinstance(path, list) and len(path) == 1:
            return path[0]
        return path

    def init_zip(self):
        # init zip
        Zip.File = self.dir_path
        return Zip.ziper()

    def start(self):
        zip_ = self.init_zip()
        for i, path in enumerate(self.src_path):
            try:
                new_name = self.dir_name[i]
                if not new_name or len(new_name) == 0:
                    self.err.append('%s:目标文件没有对应的重命名' % path)
            except Exception as err:
                new_name = os.path.basename(path)
                self.err.append('%s:目标文件没有对应的重命名' % path)

            if self.check_file(path):
                try:
                    zip_.write(filename=path, arcname=new_name, compress_type=ZIP_DEFLATED)
                except Exception as err:
                    self.err.append(str(err))
        zip_.close()

    def check_file(self, path):
        try:
            if os.path.isfile(path):
                return True
            elif os.path.isdir(path) or not os.path.exists(path):
                raise ValueError('%s:目标文件不存在' % path)
        except Exception as err:
            self.err.append(str(err))


class Zip(object):
    File = None
    Mode = 'w'
    Compression = ZIP_DEFLATED

    @classmethod
    def ziper(cls):
        if not cls.File:
            current_directory = os.path.dirname(os.path.abspath(__file__))
            cls.File = os.path.join(current_directory, 'myZip.zip')
        return zipfile.ZipFile(file=Zip.File, mode=Zip.Mode, compression=Zip.Compression)


if __name__ == '__main__':
    args1 = ['output/1.txt', 'output/2.txt', 'output/3.jpg', 'output/4.txt', 'output/5.txt']
    args2 = ['1_.txt', '2_2.txt', '3_3.jpg', '4_.txt']
    args3 = 'output/t.zip'

    deal = FileZipHelper(args1, args2, args3)
    deal.start()
    print(deal.err)
