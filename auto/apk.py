import os
import sys


class Apk:

    def __init__(self, path):
        self.path = path
        self.apk_path = os.path.split(self.path)[-1]
        self.apk_name = os.path.splitext(self.apk_path)[-2]
        self.out_path = "project\\" + self.apk_name
        self.new_path = os.getcwd() + "\\" + self.out_path
        self.new_apk_path = self.new_path + "\\dist\\" + self.apk_path
        print("====================")
        print("apk模块已启动...")
        print("====================")

    # 解析apk
    def decode(self):
        print("★=> 解析APK")
        print("-------------------")
        print("ε = = (づ′▽`)づ 准备检测" + self.path + "是否存在...")
        if os.path.exists(self.path):
            print("ε = = (づ′▽`)づ " + self.path + "存在, 准备检测项目" + self.apk_name + "是否已经存在...")
            if os.path.exists(self.out_path):
                print("ε = = (づ′▽`)づ 检测目录" + self.apk_name + "存在, 跳过解析...")
            else:
                print("ε = = (づ′▽`)づ 检测目录" + self.apk_name + "不存在, 正在准备解析...")
                print("ε = = (づ′▽`)づ 解析" + self.apk_path + "开始...")
                code = os.system(r"java -jar bin\apktool\apktool.jar d " + self.path + " -o " + self.out_path)
                if code == 0:
                    print("ε = = (づ′▽`)づ 解析" + self.apk_path + "成功...")
                else:
                    print("ε = = (づ′▽`)づ 解析" + self.apk_path + "失败, 准备退出...")
                    print("ε = = (づ′▽`)づ 正在退出...")
                    sys.exit()
            print("ε = = (づ′▽`)づ 项目文件在 " + self.new_path)
        else:
            print("ε = = (づ′▽`)づ " + self.path + "不存在")
        print("-------------------")

    # 编译apk
    def build(self):
        print("★<= 编译APK")
        print("-------------------")
        print("ε = = (づ′▽`)づ 准备检测目录" + self.apk_name + "是否存在...")
        if os.path.exists(self.out_path):
            print("ε = = (づ′▽`)づ 检测目录" + self.apk_name + "存在, 准备编译...")
            code = os.system(r"java -jar bin\apktool\apktool.jar b " + self.out_path)
            if code == 0:
                print("ε = = (づ′▽`)づ 编译" + self.apk_path + "成功...")
                print("ε = = (づ′▽`)づ 新apk在 " + self.new_apk_path)
            else:
                print("ε = = (づ′▽`)づ 编译" + self.apk_path + "失败, 准备退出...")
                print("ε = = (づ′▽`)づ 正在退出...")
                sys.exit()
        else:
            print("ε = = (づ′▽`)づ 检测项目不存在, 准备退出...")
            print("ε = = (づ′▽`)づ 正在退出...")
            sys.exit()
        print("-------------------")
