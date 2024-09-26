import os
from pygifsicle import optimize
import cv2
# import matplotlib.pyplot as plt
def extract_word_from_filename(filename, separator="_"):
    base_name = os.path.splitext(filename)[0]
    word = base_name.split(separator)[0]
    return word

def match_words_in_directory(directory_path, separator="_"):
    word_image_map = {}

    for filename in os.listdir(directory_path):
        if filename.lower().endswith(".gif") or filename.lower().endswith(".jpg"):
            word = extract_word_from_filename(filename, separator)
            image_path = os.path.join(directory_path, filename)
            word_image_map[word] = image_path

    return word_image_map
def combine_gifs(input_gifs, output_path):
    # input_gifs is a list of paths to the input GIFs that you want to combine
    # output_path is the path to the output GIF where the combined GIF will be saved
    optimize(input_gifs, output_path)

def size(path):
    vidcap=cv2.VideoCapture(path);
    success,image=vidcap.read()
    while success:
        success,image=vidcap.read()
        resize=cv2.resize(image,(480,848))


def textToSign(text):
    directory_path = "ISL_Gifs"
    word_image_map = match_words_in_directory(directory_path)
    ll = [];
    search_word = text
    words = search_word.split()  # split the sentence in to words
    for search_word in words:  # get each word from the list then search in the GIF directory
        if search_word in word_image_map:
            image_path = word_image_map[search_word]
            print(f"Image path for '{search_word}': {image_path}")
            ll.append(image_path);
        else:
            # if not there in dataset split the word in to alphabets and then print
            alphabets = list(search_word);
            alphabets = [a.upper() for a in alphabets]
            for s in alphabets:
                if s in word_image_map:
                    image_path = word_image_map[s]
                    print(f"Image path for '{s}': {image_path}")
                    ll.append(image_path)
            # print(f"No image found for '{search_word}'.")

    print(ll)
    output_path = "static/results/path_to_output_combined.gif"
    combine_gifs(ll, output_path)

# def main():

    # directory_path = "../ISL_Gifs"
    # word_image_map = match_words_in_directory(directory_path)
    # ll=[];
    # search_word = "Hi Sir"
    # words = search_word.split()     #split the sentence in to words
    # for search_word in words:      # get each word from the list then search in the GIF directory
    #     if search_word in word_image_map:
    #         image_path = word_image_map[search_word]
    #         print(f"Image path for '{search_word}': {image_path}")
    #         ll.append(image_path);
    #     else:
    #         # if not there in dataset split the word in to alphabets and then print
    #         alphabets = list(search_word);
    #         alphabets = [a.upper() for a in alphabets]
    #         for s in alphabets:
    #             if s in word_image_map:
    #                 image_path = word_image_map[s]
    #                 print(f"Image path for '{s}': {image_path}")
    #                 ll.append(image_path)
    #         # print(f"No image found for '{search_word}'.")
    #
    #
    # print(ll)
    # # output_path = "path_to_output_combined.gif"
    # output_path = "../static/results/path_to_output_combined.gif"
    # combine_gifs(ll, output_path)

# if __name__ == "__main__":
#     main()
