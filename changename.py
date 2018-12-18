import os

os.chdir(r'C:\Users\student\heesu\SSAFY지원자')

# for name in os.listdir("."):
#     if name.startswith('SAMSUNG_'):
#         newname = name.replace('SAMSUNG_','SSAFY_')
#         os.rename(name,newname)

for filename in os.listdir("."):
        after_name = filename.replace("SAMSUNG","SSAFY")
        os.rename(filename, after_name)
