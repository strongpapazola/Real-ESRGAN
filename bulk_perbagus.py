from subprocess import Popen, PIPE
import os

def shell(cmd):
    return Popen(cmd, shell=True, stdout=PIPE).stdout.read().decode('utf-8')

# mv all file from input folder to folder inputdone
shell("move input/* inputdone")
shell("move output/* outputdone")


# get all file name inside input folder
files = os.listdir('input')
for i in files:
    print(f"realesrgan-ncnn-vulkan.exe -i input\{i} -o output\{i}")
    shell(f"realesrgan-ncnn-vulkan.exe -i \"input\{i}\" -o \"output\{i}\"")
