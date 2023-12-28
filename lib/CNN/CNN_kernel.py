from manim import *

class CNNkernel(Scene):
    def construct(self):
        self.introduction_to_cnn()
        self.show_convolution_operation()
        self.show_convolution_layer()
        self.show_pooling_layer()

    def introduction_to_cnn(self):
        intro_title = Text("Convolutional Neural Network (CNN)", font_size=24).to_edge(UP)
        intro_desc = Text("CNNs use layers for feature detection and pooling to reduce dimensions. Designed for image-like data.", font_size=20, line_spacing=1.5).next_to(intro_title, DOWN, buff=0.5)

        self.animate_section(intro_title, None, intro_desc)

    def show_convolution_operation(self):
        conv_title = Text("Convolution Operation", font_size=24).to_edge(UP)
        conv_formula = MathTex(r"(f*g)(t) = \int_{-\infty}^{+\infty} f(\tau)g(t-\tau) d\tau", font_size=28).next_to(conv_title, DOWN, buff=0.5)
        conv_desc = Text("Sliding one function over another, a weighted sum.", font_size=20, line_spacing=1.5).next_to(conv_formula, DOWN, buff=0.5)

        self.animate_section(conv_title, conv_formula, conv_desc)

    def show_convolution_layer(self):
        layer_title = Text("Convolution Layer", font_size=24).to_edge(UP)
        layer_desc = Text("Neurons connect to a local region for feature detection. Convolution kernels reduce parameters.", font_size=20, line_spacing=1.5).next_to(layer_title, DOWN, buff=0.5)
        kernel_image = ImageMobject("convolution.gif").scale_to_fit_width(12).move_to(ORIGIN)

        self.animate_section(layer_title, kernel_image, layer_desc)

    def show_pooling_layer(self):
        pooling_title = Text("Pooling Layer", font_size=24).to_edge(UP)
        pooling_desc = Text("Pooling reduces feature map dimensions. Max pooling is common.", font_size=20, line_spacing=1.5).next_to(pooling_title, DOWN, buff=0.5)
        pooling_image = ImageMobject("pooling.gif").scale_to_fit_width(12).move_to(ORIGIN)

        self.animate_section(pooling_title, pooling_image, pooling_desc)

    def animate_section(self, title, visual_element, desc):
        self.play(Write(title))
        self.wait(2)
        if visual_element:
            self.play(FadeIn(visual_element))
            self.wait(1)  
        self.play(Write(desc))
        self.wait(4)

        animations = [FadeOut(title), FadeOut(desc)]
        if visual_element:
            animations.append(FadeOut(visual_element))
        
        self.play(*animations)

if __name__ == "__main__":
    config.pixel_height = 1080
    config.pixel_width = 1920
    config.frame_rate = 60
    config.output_file = "CNN_kernel"
    config.write_to_movie = True

    scene = CNNkernel()
    scene.render()
