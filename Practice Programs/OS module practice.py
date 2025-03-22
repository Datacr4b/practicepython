import os

folder = input("Type in the Folder path: ")
filter_size = int(input("Type in the size filter: "))
for file in os.listdir(folder):
    size = os.stat(os.path.join(folder,file)).st_size
    if size > filter_size:
        print(f"{file}: {size} bytes")
