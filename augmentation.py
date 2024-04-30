import Augmentor
p = Augmentor.Pipeline("data\Triangulo")
p.rotate(probability=0.7, max_left_rotation=10, max_right_rotation=10)
p.zoom(probability=0.3, min_factor=0.8, max_factor=1.5)
p.flip_top_bottom(probability=0.4)
p.flip_left_right(probability=0.4)
p.random_brightness(probability=0.3, min_factor=0.3, max_factor=1.3)
p.random_distortion(probability=0.2, grid_width=4, grid_height=4, magnitude=3)
p.random_distortion(probability=1, grid_width=4, grid_height=4, magnitude=8)
p.random_contrast(probability=0.3, min_factor=0.5, max_factor=1.5)
p.random_color(probability=0.3, min_factor=0.5, max_factor=1.5)

p.sample(10000)