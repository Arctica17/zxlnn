from manim import *
from manim_ml.neural_network import Convolutional2DLayer, FeedForwardLayer, NeuralNetwork

config.pixel_height = 700
config.pixel_width = 1900
config.frame_height = 7.0
config.frame_width = 19.0

class BasicScene(ThreeDScene):
    def construct(self):
        nn = NeuralNetwork([
            Convolutional2DLayer(1, 6, 3, filter_spacing=0.32),
            Convolutional2DLayer(2, 4, 3, filter_spacing=0.32),
            Convolutional2DLayer(4, 2, 3, filter_spacing=0.18),
            FeedForwardLayer(3),
            FeedForwardLayer(3),
        ], layer_spacing=0.25)
        
        nn.scale(4.0)
        nn.move_to(ORIGIN)
        self.add(nn)

        forward_pass = nn.make_forward_pass_animation()

        self.play(
            forward_pass,
            run_time=forward_pass.run_time / 2
        )

if __name__ == "__main__":
    forward_pass_scene = BasicScene()
    forward_pass_scene.render()
