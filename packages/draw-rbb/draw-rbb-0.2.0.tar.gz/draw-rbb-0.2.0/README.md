# Drawing Rounded Bounding Box

![](figures/example.jpg)

## Example run

```shell
pip install draw-rbb
python demo.py
```

* `src`: image source in `numpy` array
* `top_left`: top-left of the bounding box
* `bottom_right`: bottom-right of the bounding box
* `text`: text to be displayed
* `font`: font of the text
* `text_scale`: text sale
* `text_color`: color of the text, (B, G, R)
* `text_thickness`: thickness of the text
* `bb_color`: color of the bounding box, (B, G, R)
* `bb_radius`: radius of the bounding box
* `bb_thickness`: thickness of the bounding box
* `tb_color`: color of the text box
* `tb_radius`: radius of the text box
* `tb_thickness`: thickness of the text box
* `tb_ratio_w`: width ratio of the text box to bounding box width
* `tb_ratio_h`: height ratio of the text box to bounding box height
* returns: `src`: output image with rounded bounding box and text
