from manim import *
from NN.nn import NeuralNetworkMobject

class Component(ThreeDScene):
    def construct(self):
        nn = NeuralNetworkMobject([3, 5, 5, 5, 3])

        nn.shift(DOWN)

        print(nn.layer_sizes)

        size = len(nn.layer_sizes)

        for i in range(size):
            if(i == 0):
                input_layer_label = Text("输入层").scale(0.7)
                input_layer_label.next_to(nn.layers[i], UP)
                input_layer_label.shift(UP)
                self.play(Write(input_layer_label))
                self.wait(1)
            elif(i == 1):
                hidden_layer_label = Text("隐藏层").scale(0.7)
                hidden_layer_label.next_to(nn.layers[i], UP)
                hidden_layer_label.shift(RIGHT * 1.8)
                self.play(Write(hidden_layer_label))
                self.wait(1)
            elif(i == size - 1):
                output_layer_label = Text("输出层").scale(0.7)
                output_layer_label.next_to(nn.layers[i], UP)
                output_layer_label.shift(UP)
                self.play(Write(output_layer_label))
                self.wait(1)

            animation = AnimationGroup(*[
                Create(neuron) for neuron in nn.layers[i].neurons
            ], lag_ratio=0)
            self.play(animation)
            self.wait(1)

            if(i < size - 1):
                animation = AnimationGroup(*[
                    Create(line) for line in nn.edge_groups[i]
                ], lag_ratio=0)

                self.play(animation)
                self.wait(1)
