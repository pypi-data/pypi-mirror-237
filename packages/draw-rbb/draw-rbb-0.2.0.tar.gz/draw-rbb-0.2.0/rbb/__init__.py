import cv2
import numpy as np
from typing import Tuple, Union


def rounded_rectangle(
    src: np.ndarray,
    top_left: Tuple[int, int],
    bottom_right: Tuple[int, int],
    radius: float = 1,
    color: Union[Tuple[int, int, int], int] = 255,
    thickness: int = 1,
    line_type: int = cv2.LINE_AA
) -> np.ndarray:

    """
    Draws a rounded rectangle

    :param src: image source in numpy array
    :param top_left: top-left of the rectangle
    :param bottom_right: bottom-right of the rectangle
    :param radius: radius of the rounded corner
    :param color: color of the rectangle
    :param thickness: thickness of the rectangle
    :param line_type: line type of rectangle
    :return: src: output image with rounded rectangle
    """

    p1 = top_left
    p2 = (bottom_right[0], top_left[1])
    p3 = (bottom_right[0], bottom_right[1])
    p4 = (top_left[0], bottom_right[1])

    height = abs(bottom_right[1] - top_left[1])

    if radius > 1:
        radius = 1

    corner_radius = int(radius * (height / 2))

    if thickness < 0:
        # big rect
        top_left_main_rect = (int(p1[0] + corner_radius), int(p1[1]))
        bottom_right_main_rect = (int(p3[0] - corner_radius), int(p3[1]))

        top_left_rect_left = (p1[0], p1[1] + corner_radius)
        bottom_right_rect_left = (p4[0] + corner_radius, p4[1] - corner_radius)

        top_left_rect_right = (p2[0] - corner_radius, p2[1] + corner_radius)
        bottom_right_rect_right = (p3[0], p3[1] - corner_radius)

        all_rects = [
            [top_left_main_rect, bottom_right_main_rect],
            [top_left_rect_left, bottom_right_rect_left],
            [top_left_rect_right, bottom_right_rect_right]
        ]

        [cv2.rectangle(src, rect[0], rect[1], color, thickness) for rect in all_rects]

    # draw straight lines
    cv2.line(
        src,
        (p1[0] + corner_radius, p1[1]),
        (p2[0] - corner_radius, p2[1]),
        color,
        abs(thickness),
        line_type
    )
    cv2.line(
        src,
        (p2[0], p2[1] + corner_radius),
        (p3[0], p3[1] - corner_radius),
        color,
        abs(thickness),
        line_type
    )
    cv2.line(
        src,
        (p3[0] - corner_radius, p4[1]),
        (p4[0] + corner_radius, p3[1]),
        color,
        abs(thickness),
        line_type
    )
    cv2.line(
        src,
        (p4[0], p4[1] - corner_radius),
        (p1[0], p1[1] + corner_radius),
        color,
        abs(thickness),
        line_type
    )

    # draw arcs
    cv2.ellipse(
        src,
        (p1[0] + corner_radius, p1[1] + corner_radius),
        (corner_radius, corner_radius),
        180.0,
        0,
        90,
        color,
        thickness,
        line_type
    )
    cv2.ellipse(
        src,
        (p2[0] - corner_radius, p2[1] + corner_radius),
        (corner_radius, corner_radius),
        270.0,
        0,
        90,
        color,
        thickness,
        line_type
    )
    cv2.ellipse(
        src,
        (p3[0] - corner_radius, p3[1] - corner_radius),
        (corner_radius, corner_radius),
        0.0,
        0,
        90,
        color,
        thickness,
        line_type
    )
    cv2.ellipse(
        src,
        (p4[0] + corner_radius, p4[1] - corner_radius),
        (corner_radius, corner_radius),
        90.0,
        0,
        90,
        color,
        thickness,
        line_type
    )

    return src


def draw_bounding_box(
    src,
    top_left,
    bottom_right,
    text: str = '',
    font: int = cv2.FONT_HERSHEY_SIMPLEX,
    text_scale: int = 2,
    text_color: Tuple[int, int, int] = (0, 255, 255),
    text_thickness: int = 3,
    bb_color: Tuple[int, int, int] = (0, 0, 255),
    bb_radius: int = -1,
    bb_thickness: int = 10,
    tb_color: Tuple[int, int, int] = (0, 0, 255),
    tb_radius: float = 0.1,
    tb_thickness: int = -1,
    tb_ratio_w: float = 0.7,
    tb_ratio_h: float = 0.15,
    outline_color: Union[Tuple[int, int, int], bool] = False
) -> np.ndarray:

    """
    Draws a rounded bounding with text

    :param src: image source in numpy array
    :param top_left: top-left of the bounding box
    :param bottom_right: bottom-right of the bounding box
    :param text: text to be displayed
    :param font: font of the text
    :param text_scale: text sale
    :param text_color: color of the text, (B, G, R)
    :param text_thickness: thickness of the text
    :param bb_color: color of the bounding box, (B, G, R)
    :param bb_radius: radius of the bounding box
    :param bb_thickness: thickness of the bounding box
    :param tb_color: color of the text box
    :param tb_radius: radius of the text box
    :param tb_thickness: thickness of the text box
    :param tb_ratio_w: width ratio of the text box to bounding box width
    :param tb_ratio_h: height ratio of the text box to bounding box height
    :param outline_color:
    :return: src: output image with rounded bounding box and text
    """

    # --- Draw outline
    x1, y1 = top_left
    x2, y2 = bottom_right

    if outline_color:
        outline_x1 = x1 - bb_thickness
        outline_y1 = y1 - bb_thickness

        outline_x2 = x2 + bb_thickness
        outline_y2 = y2 + bb_thickness

        outline_thickness = bb_thickness

        src = rounded_rectangle(
            src=src,
            top_left=(outline_x1, outline_y1),
            bottom_right=(outline_x2, outline_y2),
            color=outline_color,
            radius=bb_radius,
            thickness=outline_thickness
        )

    # --- Draw rounded bounding box
    src = rounded_rectangle(
        src=src,
        top_left=top_left,
        bottom_right=bottom_right,
        color=bb_color,
        radius=bb_radius,
        thickness=bb_thickness
    )

    # --- Draw rounded text box
    w = int(tb_ratio_w * (x2 - x1))
    h = int(tb_ratio_h * (y2 - y1))

    t_x1 = x1
    t_y1 = y1 - h

    t_x2 = t_x1 + w
    t_y2 = y1

    src = rounded_rectangle(
        src=src,
        top_left=(t_x1, t_y1),
        bottom_right=(t_x2, t_y2),
        color=tb_color,
        radius=tb_radius,
        thickness=tb_thickness
    )

    # --- Draw text
    text_org = (x1 + int(0.1 * w), y1 - int(0.3 * h))
    src = cv2.putText(
        img=src,
        text=text,
        org=text_org,
        fontFace=font,
        fontScale=text_scale,
        color=text_color,
        thickness=text_thickness
    )

    return src
