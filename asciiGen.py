from PIL import Image, ImageDraw, ImageFont

import math

char = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
# char = "#Wo- "[::-1]

char_array = list(char)
interval = len(char_array) / 256
scale_factor = 0.5

char_width = 10
char_height = 18


def get_char(input_int):
    return char_array[math.floor(input_int * interval)]


txt_file = open("output.txt", "w")

img = Image.open("foto.jpg")

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 15)

width, height = img.size
img = img.resize(
    (
        int(scale_factor * width),
        int(scale_factor * height * (char_width / char_height)),
    ),
    Image.NEAREST,
)

width, height = img.size
px = img.load()

output_img = Image.new(
    "RGB", (char_width * width, char_height * height), color=(0, 0, 0)
)
draw_img = ImageDraw.Draw(output_img)

for i in range(height):
    for j in range(width):
        r, g, b = px[j, i]
        gray = int(r / 3 + g / 3 + b / 3)
        px[j, i] = (gray, gray, gray)

        txt_file.write(get_char(gray))

        draw_img.text(
            (j * char_width, i * char_height), get_char(gray), font=font, fill=(r, g, b)
        )

    txt_file.write("\n")

output_img.save("output.png")
