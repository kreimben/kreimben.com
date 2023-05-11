import PIL.Image as PILI

char_set = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`\'.'


def get_image(image_name: str):
    return PILI.open(image_name)


def get_gray_image(image):
    return image.convert("L")


def convert_to_ascii(image, compress_ratio: int = 3) -> str:
    width, height = image.size
    ratio = height / width
    height = int(width * ratio * 0.5)
    image = image.resize((width, height), PILI.LANCZOS)
    res = ''
    N = len(char_set)
    for i in range(0, height, compress_ratio):
        for j in range(0, width, compress_ratio):
            pixel = image.getpixel((j, i))
            res += char_set[int(pixel / (256 / N))]
        res += '\n'
    return res

# def main():
#     if len(sys.argv) < 2:
#         print("Usage: python3 main.py <image_name> [<compress_level>]")
#         print(f'The higher the compress_level, the more compressed the image will be. Default is 3.')
#         sys.exit(1)
#     image_name = sys.argv[1]
#
#     if len(sys.argv) == 3:
#         compress_ratio = int(sys.argv[2])
#     else:
#         compress_ratio = 3
#
#     image = get_image(image_name)
#
#     if not hasattr(image, 'is_animated') or not image.is_animated:
#         gray_image = get_gray_image(image)
#         with open(image_name.split('.')[0] + '.txt', "w") as f:
#             f.write(convert_to_ascii(gray_image, compress_ratio))
#     else:
#         frames = []
#         for frame in range(image.n_frames):
#             image.seek(frame)
#             print(f'Frame {image.tell()}')
#             gray_image = get_gray_image(image)
#             text = convert_to_ascii(gray_image, compress_ratio)
#             frames.append(text)
#         for i, frame in enumerate(frames):
#             with open(image_name.split('.')[0] + '-' + f'{i}.txt', "w") as f:
#                 f.write(frame)
