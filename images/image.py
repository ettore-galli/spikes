from term_image.image import from_url


def draw_image(image_url):
    image = from_url(image_url)
    image.draw()


if __name__ == "__main__":
    draw_image("https://picsum.photos/536/354")
