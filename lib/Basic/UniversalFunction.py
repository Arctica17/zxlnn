from manim import *
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from NN.nn import NeuralNetworkMobject

class UniversalFunction(Scene):
    def construct(self):
        # 生成一些随机的x和y数据，y = log(x) + 噪声
        x = np.random.uniform(0.1, 10, size=1000)
        y = np.log(x) + np.random.normal(0, 0.2, size=1000)

        # 将数据分为训练集和测试集
        x_train, x_test = x[:800], x[800:]
        y_train, y_test = y[:800], y[800:]

        # 定义一个简单的神经网络模型，有一个隐藏层和一个输出层
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(32, activation='sigmoid', input_shape=(1,)),
            tf.keras.layers.Dense(32, activation='sigmoid'),
            tf.keras.layers.Dense(1)
        ])

        # 编译模型，指定优化器，损失函数和评估指标
        model.compile(optimizer='adam', loss='mse', metrics=['mae'])

        # 训练模型，指定批次大小和迭代次数
        model.fit(x_train, y_train, batch_size=32, epochs=20)

        # 评估模型在测试集上的表现
        model.evaluate(x_test, y_test)

        # 预测一些新的x值，并与真实的y值和模型的预测值进行比较
        x_new = np.linspace(0.1, 10, 10)
        y_pred = model.predict(x_new)

        print(x_new)
        print(y_pred)

        max_shown_neurons = 10
        settings = {"neuron_radius": 0.2, 
                    "neuron_stroke_width": 0.5,
                    "max_shown_neurons": max_shown_neurons}
        nn = NeuralNetworkMobject([1, 32, 32, 1], **settings)
        nn.shift(LEFT * 3)

        # 创建坐标轴
        ax = Axes(x_range=[0, 10, 3], y_range=[-5, 5, 1.5]).scale(0.4)
        ax.shift(RIGHT * 4)
        self.play(Create(ax))
        self.wait(1)

        size = len(nn.layer_sizes)

        # 播放前向传播动画
        for i in range(size):
            animation = AnimationGroup(*[
                Create(neuron) for neuron in nn.layers[i].neurons
            ], lag_ratio=0)

            if(nn.layer_sizes[i] > max_shown_neurons):
                animation = AnimationGroup(*[animation, 
                                            Write(nn.layers[i].dots), 
                                            Create(nn.layers[i].brace),
                                            Write(nn.layers[i].brace_label)])
            
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
        
        # 创建转换点的动画
        predict_dots = VGroup(*[
            Dot(ax.coords_to_point(x, y_pred[i][0]), color=GREEN).scale(0.5) for i, x in enumerate(np.nditer(x_new))
        ])

        output_layer_copy = nn.layers[-1].neurons.copy()
        self.play(Transform(output_layer_copy, predict_dots))
        self.wait(1)

        # 创建log函数
        log_func = ax.plot(lambda x : np.log(x), x_range=[0.1, 10], color=BLUE)
        self.play(Create(log_func))
        self.wait(1)

