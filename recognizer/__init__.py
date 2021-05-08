import functools

import click
import cv2

from .utils import get_color_name

APP = "Image Color Recognition App"

# -- Other functions --
def handle_events(img, event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        b, g, r = img[y, x]
        b, g, r = int(b), int(g), int(r)

        cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)

        name, closest_name = get_color_name((r, g, b))
        if not name:
            name = closest_name

        text = f"{closest_name} | RGB: ({r}, {g}, {b})"

        cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

        if r + g + b >= 600:
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)


# -- Commands --
@click.command()
@click.option("-i", "--image", "image", required=True, type=click.Path(exists=True))
def recognize(image):
    img = cv2.imread(image)

    cv2.namedWindow(APP)
    cv2.setMouseCallback(APP, functools.partial(handle_events, img))

    while True:
        cv2.imshow(APP, img)

        if cv2.waitKey(20) & 0xFF == 27:
            break

    cv2.destroyAllWindows()
