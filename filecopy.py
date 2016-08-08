from os import listdir
from os.path import isfile, join
import glob
import shutil


def copy_method_0(source_path, target_path):
    list = [f for f in listdir(source_path) if isfile(join(source_path, f))]
    for path in list:
        if path.find("RELEASE.jar") != -1:
            print path
            shutil.copy2(source_path + "/" + path, target_path)
 

def copy_method_1(source_path, target_path):
    list2 = glob.glob(source_path + "\*.RELEASE.jar")
    for path in list2:
        print path
        shutil.copy2(path, target_path)


source_path = "D:\download\spring-framework-4.2.5.RELEASE\libs"
target_path = "D:\workspace\JAVA\HelloWorld\lib"
copy_method_1(source_path, target_path)
