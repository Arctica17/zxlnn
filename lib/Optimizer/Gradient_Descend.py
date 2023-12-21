from manimlib import *
import numpy as np
from scipy.interpolate import interp1d
def numberical_grandient(f, x):
    h = 1e-4                     #定义一个微小量，不能太小，太小计算机没法正确表示     #生成和x形状相同的数组   #计算所有偏导
    x_h = x + h            #要计算的那个自变量加h，其余不变
    fxh1 = f(x_h)                     #计算f(x+h)

    x_l = x - h           #计算f(x-h)
    fxh2 = f(x_l)

    grad = (fxh1 - fxh2) / (2*h)    #计算偏导
    return grad

class PlotFunctionGraph(Scene):
    
    def construct(self):
        # 梯队下降有关参数
        # 学习率
        lr=0.1
        # 梯度阈值 小于该阈值时退出
        threshold=1e-5
        # 训练轮次
        epochs=100
        
        # 创建坐标系
        axes = Axes(
            # x-axis ranges from -1 to 10, with a default step size of 1
            x_range=(-8, 8),
            # y-axis ranges from -2 to 2 with a step size of 0.5
            y_range=(-8, 8),
            # The axes will be stretched so as to match the specified
            # height and width
            height=10,
            width=10,
            # Axes is made of two NumberLine mobjects.  You can specify
            # their configuration with axis_config
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2,
            },
            # Alternatively, you can specify configuration for just one
            # of them, like this.
            y_axis_config={
                "include_tip": False,
            }
        )
        axes.add_coordinate_labels()
        self.play(Write(axes, lag_ratio=0.01, run_time=0.5))
        self.wait(0.5)
        self.play(
            axes.animate.scale(0.75),
            run_time=0.5,
        )

        data = np.array([(-3, 7), (-1, -1), (1,5),(2,-3), (3, 3),(4,-5),(5,5)])
        # 分离 x 和 y 坐标
        x, y = data.T
        # 使用 interp1d 进行插值
        z1=np.polyfit(x,y,4)
        f1=np.poly1d(z1)
        interp_func = interp1d(x, y, kind='cubic')

        # 绘制差值后的图像
        fitting_graph = axes.get_graph(
            lambda x: f1(x),
            #x_range=[-3, 3],
            use_smoothing=True,
            color=YELLOW,
        )
        fitting_label = axes.get_graph_label(fitting_graph, "fitting label")
        self.play(
            ShowCreation(fitting_graph),
            #ShowCreation(fitting_label),
            run_time=0.5,
            #FadeIn(fitting_label, RIGHT),
        )
        
        target=2
        x=target
        y=f1(x)
        for i in range(epochs):
            start_dot = Dot(fill_color=RED)
            start_dot.move_to(axes.c2p(x, y))

            #self.play(ShowCreation(start_dot))
            self.play(ShowCreation(start_dot),run_time=0.25)
            self.wait(0.1)
            
            grad=numberical_grandient(f1,x)
            grad_text=Tex(f"gradient~is~{grad:.5f}")
            self.play(ShowCreation(grad_text.to_corner(UR)))
            self.wait(0.25)
            self.play(FadeOut(grad_text),run_time=0.25)
            
            if math.fabs(grad) <= threshold :
                break
            factor=(grad**2+1)**(1/2)
            if grad > 0:
                factor=-factor
            x_hat=x+1/factor
            y_hat=y+grad/factor
            
           
            
            end_dot = Dot(fill_color=RED)
            end_dot.move_to(axes.c2p(x_hat, y_hat))
            #self.play(ShowCreation(end_dot))
            # self.play(FadeIn(end_dot, scale=0.5))
            # self.wait(0.5)
            
            x=x-lr*grad
            y=f1(x)
            
            arrow = Arrow(start=start_dot.get_center(), end=end_dot.get_center()\
                , buff=0.1,stroke_width=3)
            self.play(ShowCreation(arrow),run_time=0.1)
            self.wait(0.1)
            self.play(FadeOut(start_dot),run_time=0.01)
            self.play(FadeOut(arrow),run_time=0.01)
        
