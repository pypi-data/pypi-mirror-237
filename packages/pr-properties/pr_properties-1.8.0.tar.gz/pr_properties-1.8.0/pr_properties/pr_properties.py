import os
import shutil
import uuid

import filelock


class PropertiesHandler:
    def __init__(self, file_path=None):
        """
        初始化PropertiesHandler对象。

        参数：
        - file_path：文件路径，默认为None。
        """
        self.file_path = file_path
        self.properties = {}

    def backup(self):
        """
        备份文件。
        """
        backup_file_path = self.file_path + '.pr_bak'
        if not os.path.exists(backup_file_path):
            try:
                shutil.copy2(self.file_path, backup_file_path)
            except IOError as e:
                raise Exception(f"备份文件时出现错误：{e}")

    def read(self, file_path=None):
        """
        从文件中读取属性。

        参数：
        - file_path：文件路径，默认为None。

        返回：
        - properties：读取到的属性字典。
        """
        if file_path is not None:
            self.file_path = file_path

        if not os.path.exists(self.file_path):
            raise FileNotFoundError("文件路径不存在")

        try:
            lock = filelock.FileLock(self.file_path + '.lock')

            with lock.acquire(timeout=10):
                with open(self.file_path, 'r', encoding='utf-8') as file:
                    lines = file.readlines()

            for line in lines:
                line = line.strip()

                if len(line) == 0:
                    key = str(uuid.uuid4())  # 使用UUID作为键
                    self.properties[key] = None
                    continue
                elif line.startswith('#') or line.startswith(';'):
                    self.properties[line] = ""
                    continue

                key_value = line.split('=')
                if len(key_value) == 1:
                    self.properties[key_value[0].strip()] = ""

                if len(key_value) < 2:
                    continue

                key = key_value[0].strip()
                value = '='.join(key_value[1:]).strip()

                self.properties[key] = value

        except IOError as e:
            raise Exception(f"读取文件时出现错误：{e}")

        return self

    def write(self):
        """
        将属性写入文件。
        """
        self.backup()

        try:
            lock = filelock.FileLock(self.file_path + '.lock')

            with lock.acquire(timeout=10):
                with open(self.file_path, 'w', encoding='utf-8') as file:
                    file.write(str(self))
        except IOError as e:
            raise Exception(f"写入文件时出现错误：{e}")

    def __getitem__(self, key):
        """
        获取属性值。

        参数：
        - key：属性键。

        返回：
        - value：属性值。
        """
        return self.properties[str(key)]

    def __setitem__(self, key, value):
        """
        设置属性值。

        参数：
        - key：属性键。
        - value：属性值。
        """
        self.properties[str(key)] = value

    def __delitem__(self, key):
        """
        删除属性。

        参数：
        - key：属性键。
        """
        del self.properties[str(key)]

    def get(self, key, default=None):
        """
        获取属性值，如果属性不存在则返回默认值。

        参数：
        - key：属性键。
        - default：默认值，默认为None。

        返回：
        - value：属性值或默认值。
        """
        return self.properties.get(str(key), default)

    def __str__(self):
        output = ""
        for key, value in self.properties.items():
            if value is None:
                output += "\n"  # 将None值转换为空行
            elif value == "":
                output += str(key) + "\n"  # 写入注释
            else:
                output += str(key) + ' = ' + str(value) + '\n'  # 写入属性和对应的值
        return output


pr_properties = PropertiesHandler()
