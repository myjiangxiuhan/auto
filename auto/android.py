from xml.etree.ElementTree import *
import re
import os
import shutil


class Android:

    def __init__(self, android_path: str):
        print('ε = = (づ′▽`)づ Android主模块')
        self.android_path = android_path
        self.manifest = Manifest(self)
        self.smalis: list < Smali > () = []
        self.scripts: list < Script > () = []
        print("ε = = (づ′▽`)づ 加载smali文件中...")
        wolk = os.walk(self.android_path + '\\smali')
        for root, dirs, files in wolk:
            for file in files:
                self.smalis.append(Smali(os.path.join(root, file)))
        print("ε = = (づ′▽`)づ 共加载" + str(len(self.smalis)) + "个smali文件...")

    def add_script(self, script):
        self.scripts.append(script)

    def run_script(self):
        for script in self.scripts:
            script.init(self)
            script.run()
        self.__init__(self.android_path)

class Manifest:

    def __init__(self, android: Android):
        print('ε = = (づ′▽`)づ Manifest分模块')
        register_namespace('android', 'http://schemas.android.com/apk/res/android')
        self._android: Android = android
        self._manifest_path: str = self._android.android_path + "\\" + "AndroidManifest.xml"
        self._tree: ElementTree = parse(self._manifest_path)
        self.root: Element = self._tree.getroot()
        print('ε = = (づ′▽`)づ 加载' + self._manifest_path + '成功...')
        self.package: str = self.root.attrib['package']
        self.application: Application = Application(self)
        self.permissions: set < str > () = []
        for permission in self.root.findall('uses-permission'):
            self.permissions.append(permission.get('{http://schemas.android.com/apk/res/android}name'))

    def update(self):
        for permission in self.root.findall('uses-permission'):
            self.root.remove(permission)
        for permission in self.permissions:
            ele: Element = Element('uses-permission')
            ele.set('{http://schemas.android.com/apk/res/android}name', permission)
            self.root.append(ele)
        self._tree.write(self._manifest_path)
        self.__init__(self._android)


class Application:

    def __init__(self, manifest: Manifest):
        print('ε = = (づ′▽`)づ Application子模块')
        self._manifest: Manifest = manifest
        self.application_dom: Element = self._manifest.root.find('application')
        self.name = self.application_dom.get('{http://schemas.android.com/apk/res/android}name')

    def set_name(self, name: str):
        self.application_dom.set('{http://schemas.android.com/apk/res/android}name', name)

    def update(self):
        self._manifest.update()


class Smali:
    def __init__(self, smali_path_file: str):
        self.smali_path_file = smali_path_file
        self.body = ''
        self.class_name = ''
        with open(self.smali_path_file) as file:
            for str in file.readlines():
                self.body += str
            self.class_name = re.compile(r'(?<=.class ).*?(?=\n)').findall(self.body)[0]

    """
    某个字符串是否存在
    """

    def is_exist(self, str: str):
        return self.body.find(str) > -1

    def replace(self, old: str, new: str):
        self.body = self.body.replace(old, new)

    def update(self):
        with open(self.smali_path_file, mode='w') as file:
            file.write(self.body)
        self.__init__(self.smali_path_file)


class Script:

    def __init__(self):
        self.android: Android = None

    def init(self, android: Android):
        self.android = android

    def __find(self, str):
        res = []
        for smali in self.android.smalis:
            if smali.is_exist(str):
                res.append(smali)
        return res

    def find(self, str: str):
        res = []
        for smali in self.__find(str):
            res.append(smali.smali_path_file)
        return res

    def replace(self, old, new):
        for sm in self.__find(old):
            sm.replace(old, new)
            sm.update()

    def cp(self, old_path, new_path):
        if (os.path.isfile(old_path)):
            shutil.copyfile(old_path, new_path)
        elif (os.path.isdir(old_path)):
            shutil.copytree(old_path, new_path)

    def rm(self, path):
        if (os.path.isfile(self.android.android_path + "\\"+ path)):
            os.remove(path)
        elif (os.path.isdir(path)):
            shutil.rmtree(path)

    def run(self):
        pass
