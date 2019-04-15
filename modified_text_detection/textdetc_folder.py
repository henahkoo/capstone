from text_detection import td_single
import os

def get_image_paths():
    folder = './train_model/text'
    files = os.listdir(folder)
    files.sort()
    files = ['{}/{}'.format(folder, file) for file in files]
    files.remove('./train_model/text/.DS_Store')
    return files


X_img_paths = get_image_paths()
print(X_img_paths)

for filename in X_img_paths:
    print(filename)
    td_single(filename)

print("detection finished")


