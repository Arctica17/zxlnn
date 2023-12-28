from manim import *
from NN.nn import NeuralNetworkMobject
import pathlib
import numpy as np

class Component(ThreeDScene):
    def get_mnist(self):
        with np.load(f"{pathlib.Path(__file__).parent.absolute()}/MNIST_Data/mnist.npz") as f:
            images, labels = f["x_train"], f["y_train"]
        images = images.astype("float32") / 255
        images = np.reshape(images, (images.shape[0], images.shape[1] * images.shape[2]))
        labels = np.eye(10)[labels]
        return images, labels

    def construct(self):
        ## 训练过程 ##
        images, labels = self.get_mnist()
        w_i_h = np.random.uniform(-0.5, 0.5, (20, 784))
        w_h_o = np.random.uniform(-0.5, 0.5, (10, 20))
        b_i_h = np.zeros((20, 1))
        b_h_o = np.zeros((10, 1))

        learn_rate = 0.01
        nr_correct = 0
        epochs = 3

        # ### 训练epoch ###
        # for epoch in range(epochs):
        #     for img, l in zip(images, labels):
        #         img.shape += (1,)
        #         l.shape += (1,)
        #         # Forward propagation input -> hidden
        #         h_pre = b_i_h + w_i_h @ img
        #         h = 1 / (1 + np.exp(-h_pre))
        #         # Forward propagation hidden -> output
        #         o_pre = b_h_o + w_h_o @ h
        #         o = 1 / (1 + np.exp(-o_pre))

        #         # Cost / Error calculation
        #         e = 1 / len(o) * np.sum((o - l) ** 2, axis=0)
        #         nr_correct += int(np.argmax(o) == np.argmax(l))

        #         # Backpropagation output -> hidden (cost function derivative)
        #         delta_o = o - l
        #         w_h_o += -learn_rate * delta_o @ np.transpose(h)
        #         b_h_o += -learn_rate * delta_o
        #         # Backpropagation hidden -> input (activation function derivative)
        #         delta_h = np.transpose(w_h_o) @ delta_o * (h * (1 - h))
        #         w_i_h += -learn_rate * delta_h @ np.transpose(img)
        #         b_i_h += -learn_rate * delta_h

        #     # Show accuracy for this epoch
        #     print(f"Acc: {round((nr_correct / images.shape[0]) * 100, 2)}%")
        #     nr_correct = 0
        
        index = int(input("Enter a number (0 - 59999): "))

        # 展示图片
        input_layer = images[index]
        img = input_layer.reshape(28, 28)
        # print(img)
        img = np.uint8(img * 255)
        # print(img)
        img = ImageMobject(img)
        img.shift(LEFT * 3)
        img.height = 5
        img.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
        
        self.play(FadeIn(img))
        self.wait(1)

        # 创建一个28*28的圆圈矩阵
        pixels = VGroup(*[
            Circle(radius=0.05, stroke_color=BLUE, fill_color=WHITE, fill_opacity=x)
            for x in np.nditer(input_layer)
        ])
        pixels.arrange_in_grid(28, 28, buff=SMALL_BUFF)
        pixels.shift(LEFT * 3)
        self.play(FadeOut(img), Create(pixels))
        self.wait(1)

        max_shown_neurons = 20
        settings = {"neuron_radius": 0.10, 
                    "max_shown_neurons": max_shown_neurons,
                    "neuron_stroke_width": 0.5,
                    "neuron_to_neuron_buff": SMALL_BUFF}

        nn = NeuralNetworkMobject([784, 20, 10], **settings)
        nn.label_outputs(None)
        nn.shift(RIGHT * 3)
        
        size = len(nn.layer_sizes)

        # 进行神经网络创建
        for i in range(size):
            animation = AnimationGroup(*[
                Create(neuron) for neuron in nn.layers[i].neurons
            ], lag_ratio=0)

            if(nn.layer_sizes[i] > max_shown_neurons):
                animation = AnimationGroup(*[animation, 
                                            Write(nn.layers[i].dots), 
                                            Create(nn.layers[i].brace),
                                            Write(nn.layers[i].brace_label)])
            
            if(i == size - 1):
                animation = AnimationGroup(*[animation,
                                             Write(nn.output_labels)])
            
            self.play(animation)
            self.wait(1)

            if(i < size - 1):
                points = VGroup(*[
                    Dot(color=ORANGE, radius=0.01) for x in nn.edge_groups[i]
                ])

                tails = VGroup(*[
                    TracedPath(point.get_center, dissipating_time=0.5, stroke_color=ORANGE) for point in points
                ])

                self.add(tails)
                
                animation = AnimationGroup(*[
                    MoveAlongPath(d, l) for d, l in zip(points, nn.edge_groups[i])
                ])
                self.play(animation)
                self.play(Uncreate(points))

        # 开始进行前馈传递
        pixels_copy = pixels.copy()
        
        # 将输入层元素的透明度进行设置
        for idx, neuron in enumerate(nn.layers[0].neurons[:max_shown_neurons // 2]):
            neuron.set_fill(color=WHITE, opacity=input_layer[idx])
        for idx, neuron in enumerate(nn.layers[0].neurons[max_shown_neurons // 2:]):
            neuron.set_fill(color=WHITE, opacity=input_layer[nn.layer_sizes[0] - max_shown_neurons // 2 + idx])
        self.play(Transform(pixels_copy, nn.layers[0].neurons))
        self.wait(1)

        # 将输入层传递到隐藏层
        h_pre = b_i_h + w_i_h @ input_layer.reshape(784, 1)
        h = 1 / (1 + np.exp(-h_pre))

        # 播放输入层到隐藏层的前向传播动画
        points = VGroup(*[
            Dot(color=ORANGE, radius=0.01) for x in nn.edge_groups[0]
        ])
        tails = VGroup(*[
            TracedPath(point.get_center, dissipating_time=0.5, stroke_color=ORANGE) for point in points
        ])
        self.add(tails)
        animation = AnimationGroup(*[
            MoveAlongPath(d, l) for d, l in zip(points, nn.edge_groups[0])
        ])
        self.play(animation)
        self.play(Uncreate(points))

        # 对隐藏层设置透明度
        for idx, neuron in enumerate(nn.layers[1].neurons):
            neuron.set_fill(color=WHITE, opacity=h[idx][0])
        animation = AnimationGroup(*[
            Create(neuron) for neuron in nn.layers[1].neurons
        ], lag_ratio=0)
        self.play(animation)
        self.wait(1)

        # 将隐藏层传递到输出层
        o_pre = b_h_o + w_h_o @ h
        o = 1 / (1 + np.exp(-o_pre))

        # 隐藏层到输出层的前向传播动画
        points = VGroup(*[
            Dot(color=ORANGE, radius=0.01) for x in nn.edge_groups[1]
        ])
        tails = VGroup(*[
            TracedPath(point.get_center, dissipating_time=0.5, stroke_color=ORANGE) for point in points
        ])
        self.add(tails)
        animation = AnimationGroup(*[
            MoveAlongPath(d, l) for d, l in zip(points, nn.edge_groups[1])
        ])
        self.play(animation)
        self.play(Uncreate(points))

        # 对输出层设置透明度
        for idx, neuron in enumerate(nn.layers[2].neurons):
            neuron.set_fill(color=WHITE, opacity=o[idx][0])
        animation = AnimationGroup(*[
            Create(neuron) for neuron in nn.layers[2].neurons
        ], lag_ratio=0)
        self.play(animation)
        self.wait(1)

        # 强调最后的结果
        self.play(Indicate(nn.layers[2].neurons[o.argmax()]))
        self.wait(1)