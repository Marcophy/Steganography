from PIL import Image
import math
import easygui as eas


def change_color(original_color, bit):
    binary_color = bin(original_color)[2:].zfill(8)
    mod_color = binary_color[:-1] + str(bit)
    return int(mod_color, 2)


def sentence_bit_list(sentence):
    end_mark = [1, 1, 1, 1, 1, 1, 1, 1]
    output_list = []
    for symbol in sentence:
        ascii_format = ord(symbol)
        binary_format = bin(ascii_format)[2:].zfill(8)
        for bit in binary_format:
            output_list.append(bit)
    for bit in end_mark:
        output_list.append(bit)
    return output_list


def hide_sentence(sentence, input_file_path, output_file_path="New.png"):
    print("Hiding text...".format(sentence))
    picture = Image.open(input_file_path)
    pixels = picture.load()

    bit_list = sentence_bit_list(sentence)
    cont = 0
    bit_list_length = len(bit_list)
    for x in range(picture.size[0]):
        for y in range(picture.size[1]):
            if cont < bit_list_length:
                pixel = pixels[x, y]

                red = pixel[0]
                green = pixel[1]
                blue = pixel[2]

                if cont < bit_list_length:
                    new_red = change_color(red, bit_list[cont])
                    cont += 1
                else:
                    new_red = red

                if cont < bit_list_length:
                    new_green = change_color(green, bit_list[cont])
                    cont += 1
                else:
                    new_green = green

                if cont < bit_list_length:
                    new_blue = change_color(blue, bit_list[cont])
                    cont += 1
                else:
                    new_blue = blue

                pixels[x, y] = (new_red, new_green, new_blue)
            else:
                break
        else:
            continue
        break

    if cont >= bit_list_length:
        print("Text hidden successfully.")
    else:
        print("Error: there is no enough space in this picture to save the entire sentence, {} symbols remained".format(
            math.floor((bit_list_length - cont) / 8)))

    picture.save(output_file_path)


# **********************************************************************************************************************

# picture_path = eas.fileopenbox("Select a picture", "Input picture")
picture_path = "granada-principale-1366x691.jpg"

# secret_sentence = input("Write the sentence: ")
secret_sentence = "Hola"

hide_sentence(secret_sentence, picture_path, "new_picture.png")
