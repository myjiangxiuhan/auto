import sys
import os
from scripts.one_script import *

from auto.apk import *
from auto.android import *

if __name__ == "__main__":
    pass
    apk = Apk("apk\\xiyouzhuanzhuan__02_1_2_333.apk")
    apk.decode()
    android: Android = Android(apk.out_path)
    xxx = OneScript()
    android.add_script(xxx)
    android.run_script()
    print(android.manifest.package)
    # application: Application = android.manifest.application
    # application.set_name('org.mf.lb.PayApplication')
    # application.update()
    # for smali in android.smalis:
    #     if smali.is_exist(';->pay('):
    #         print(smali.smali_path_file)


