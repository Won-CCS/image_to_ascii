import cv2
import numpy as np
import txt_to_image

def remove_suffix_after_last_dot(s):
    last_dot_index = s.rfind('.')

    if last_dot_index == -1:
        return s
    
    return s[:last_dot_index]

def int_from_img(file_name):
    img = cv2.imread(file_name)
    
    with open(file_name, 'rb') as f:
        binary = f.read()

    arr = np.asarray(bytearray(binary), dtype=np.uint8)
    img = cv2.imdecode(arr, -1)
    
    luminance_mat = 0.299*img[:,:,2] + 0.587*img[:,:,1] + 0.114*img[:,:,0]
    
    return luminance_mat

def main():
    image_file_name = input()
    luminance_mat  = int_from_img("from_image/" + image_file_name)
    ascii_art_txt = ""
    max_luminance = np.amax(luminance_mat)
    min_luminance = np.amin(luminance_mat)
    gap_between_luminance_level = (max_luminance - min_luminance) / 11
    luminance_order_ascii = ['.',',','-','~',':',';','=','!','*','#','$','@']
    for i in range(luminance_mat.shape[0]):
        for j in range(luminance_mat.shape[1]):
            luminance_level = int((luminance_mat[i][j] - min_luminance) / gap_between_luminance_level)
            ascii_art_txt += luminance_order_ascii[luminance_level]
        ascii_art_txt += "\n"
    file_base_name = remove_suffix_after_last_dot(image_file_name)
    txt_file_name = file_base_name + ".txt"
    with open("to_txt/" + txt_file_name, 'w') as f:
        f.write(ascii_art_txt)

    txt_to_image.txt_to_image(txt_file_name, image_file_name)

if __name__ == '__main__':
    main()
