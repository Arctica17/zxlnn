# 导入所需的库
from manim import *
from manim_ml.neural_network import NeuralNetwork, FeedForwardLayer

# 定义一个场景类
class Neuron(Scene):
    def ReLU(self, x):
        # 写一个激活函数
        return max(x, 0)

    def construct(self):
        neuron = Circle(radius=1.5, color=WHITE).scale(0.8)
        neuron.shift(DOWN * 0.8)

        p_up = neuron.point_at_angle(PI / 2) # 获得圆的顶点
        p_down = neuron.point_at_angle(270 * DEGREES) # 获得圆的底点

        l = Line(p_up, p_down)

        p_left_up = neuron.point_at_angle(140 * DEGREES) # 从上而下的第一个神经连线的起点
        p_left = neuron.point_at_angle(PI) # 从上而下的第二个神经连线的起点
        p_left_down = neuron.point_at_angle(220 * DEGREES) # 从上而下的第三个神经连线的起点
        p_first = Dot(p_left + 2.8 * LEFT + 1.7 * UP) # 从上而下的第一个神经连线的终点
        p_second = Dot(p_left + 3 * LEFT) # 从上而下的第二个神经连线的终点
        p_third = Dot(p_left + 2.8 * LEFT + 1.7 * DOWN) # 从上而下的第三个神经连线的终点

        l_first = Line(p_first, p_left_up) # 创建从上而下第一个连线
        l_second = Line(p_second, p_left) # 创建从上而下第二个连线
        l_third = Line(p_third, p_left_down) # 创建从上而下第二个连线

        # 先播放左边的线
        self.play(Create(l_first), Create(l_second), Create(l_third))
        self.wait(1)

        # 再播放中间的神经元
        self.play(Create(neuron), Create(l))
        self.wait(1)

        p_right = neuron.point_at_angle(0) # 右侧线的起点
        dot_right = Dot(p_right + 2.5 * RIGHT)
        l_right = Line(p_right, dot_right) # 创建右侧连线
        self.play(Create(l_right)) # 播放右侧的线
        self.wait(1)

        # 创建输入参数
        label_first = MathTex("x_1 = -1").scale(0.7)
        label_second = MathTex("x_2 = 3").scale(0.7)
        label_third = MathTex("x_3 = 1").scale(0.7)

        # 修改颜色和位置
        label_first.set_color(BLUE)
        label_first.next_to(l_first, LEFT * 1.2, buff=0.1)
        label_second.set_color(BLUE)
        label_second.next_to(l_second, LEFT * 1.2, buff=0.1)
        label_third.set_color(BLUE)
        label_third.next_to(l_third, LEFT * 1.2, buff=0.1)
        
        self.play(Write(label_first), Write(label_second), Write(label_third))
        self.wait(1)

        # 创建输入权重
        w_first = MathTex("w_1 = 2").scale(0.7)
        w_second = MathTex("w_2 = 1").scale(0.7)
        w_third = MathTex("w_3 = -2").scale(0.7)

        # 权重的颜色和位置修改
        w_first.set_color(GREEN)
        w_second.set_color(GREEN)
        w_third.set_color(GREEN)
        w_first.next_to(l_first, UP, buff=0.1)
        w_second.next_to(l_second, UP, buff=0.1)
        w_third.next_to(l_third, UP, buff=0.1)
        w_first.shift(DOWN * 0.2)
        w_third.shift(DOWN * 0.2)

        self.play(Write(w_first), Write(w_second), Write(w_third))
        self.wait(1)

        # 创建偏置
        b = MathTex("b = 2").scale(0.7)
        b.set_color(YELLOW)
        b.next_to(neuron, DOWN, buff=0.1)
        b.shift(DOWN * 0.4)
        self.play(Write(b))
        self.wait(1)

        # 创建公式
        ans = 1
        form = MathTex("z = w_1 \\cdot x_1 + w_2 \\cdot x_2 + w_3 \\cdot x_3 + b = " + str(ans))
        form.set_color(ORANGE)
        form.next_to(b, DOWN)
        self.play(Write(form))
        self.wait(1)

        # 创建激活函数文本
        activ = Text("ReLU激活函数").scale(0.5)
        activ.next_to(neuron, UP)
        activ.shift(UP * 0.3)
        self.play(Write(activ))
        self.wait(1)

        # 创建坐标轴
        ax = Axes(x_range=[-2, 2, 1], y_range=[0, 2, 1]).scale(0.3)
        ax.next_to(activ, UP)
        self.play(Create(ax))
        self.wait(1)

        # 创建ReLU激活函数
        relu = ax.plot(lambda x : self.ReLU(x), x_range=[-2, 1.8], color=BLUE)
        self.play(Create(relu))
        self.wait(1)

        # 创建坐标点
        at_point = Dot(ax.coords_to_point(ans, self.ReLU(ans)), color=RED)
        self.play(Transform(form, at_point))
        self.wait(1)

        # 创建最后的输出结果
        y = MathTex("y = " + str(self.ReLU(ans))).scale(0.7)
        y.next_to(l_right, UP, buff=0.1)
        y.set_color(RED)
        y.shift(UP * 0.2)
        self.play(Transform(at_point, y))
        self.wait(1)
