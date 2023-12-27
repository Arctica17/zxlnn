from manim import *
import numpy as np
def sigmoid(x):
    return 1/(1+np.exp(-x))

# 要拟合的目标函数
def func(x_1,x_2):
    return x_1+x_2+x_1*x_2+1

def p_sig(x):
    return (1-sigmoid(x))*sigmoid(x)

def ReLU(x):
    # 写一个激活函数
    return max(x, 0)
def p_ReLU(x):
    return 0 if x<=0 else 1

act=ReLU
p_act=p_ReLU
lr=0.05
act_name="ReLU"


x_range=0.2
x_step=0.05

y_down=0
y_up=0.2
y_step=0.05



class FBScene(Scene):
    def construct(self):
        node1=Circle(radius=0.5).move_to(3*LEFT+1.5*UP)
        node2=Circle(radius=0.5).move_to(3*LEFT+1.5*DOWN)
        node3=Circle(radius=0.5).move_to(1*LEFT+1.5*UP)
        node4=Circle(radius=0.5).move_to(1*LEFT+1.5*DOWN)
        node5=Circle(radius=0.5).move_to(1*RIGHT+1.5*UP)
        node6=Circle(radius=0.5).move_to(1*RIGHT+1.5*DOWN)
        node7=Circle(radius=0.5).move_to(3*RIGHT+0*UP)
        node5.set_color(ORANGE)
        node6.set_color(ORANGE)
        #self.wait(5)
        self.play(Create(node1))
        self.play(Create(node2))
        self.play(Create(node3))
        self.play(Create(node4))
        self.play(Create(node5))
        self.play(Create(node6))
        self.play(Create(node7))
        #nodes1_group=VGroup(node1,node2,node3,node4,node5,node6,node7)
        #self.play(Create(nodes1_group))
        
        line1=Line(2.5*LEFT+1.5*UP,1.5*LEFT+1.5*UP)
        line2=Line(2.5*LEFT+1.5*UP,1.5*LEFT+1.5*DOWN)
        line3=Line(2.5*LEFT+1.5*DOWN,1.5*LEFT+1.5*UP)
        line4=Line(2.5*LEFT+1.5*DOWN,1.5*LEFT+1.5*DOWN)
        
        line5=Line(.5*LEFT+1.5*UP,.5*RIGHT+1.5*UP)
        line6=Line(.5*LEFT+1.5*UP,.5*RIGHT+1.5*DOWN)
        line7=Line(.5*LEFT+1.5*DOWN,.5*RIGHT+1.5*UP)
        line8=Line(.5*LEFT+1.5*DOWN,.5*RIGHT+1.5*DOWN)
        
        line9=Line(1.5*RIGHT+1.5*UP,2.5*RIGHT)
        line10=Line(1.5*RIGHT+1.5*DOWN,2.5*RIGHT)
        
        linegroup=VGroup(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10)
        self.play(Create(linegroup))
        
        
        
       
        x_1=.1
        x_2=.2
        input_arrow1=Arrow(4.5*LEFT+1.5*UP,3.5*LEFT+1.5*UP,buff=0)
        input_arrow2=Arrow(4.5*LEFT+1.5*DOWN,3.5*LEFT+1.5*DOWN,buff=0)
        input_text1=MathTex(f"x_1={x_1}",font_size=40)
        input_text2=MathTex(f"x_2={x_2}",font_size=40)
        input_text1.next_to(input_arrow1,UP,buff=0).scale(0.8)
        input_text2.next_to(input_arrow2,UP,buff=0).scale(0.8)
        group_x1=VGroup(input_arrow1,input_text1)
        group_x2=VGroup(input_arrow2,input_text2)
        
        self.play(Create(input_arrow1))
        self.play(Create(input_arrow2))
        self.play(Create(input_text1))
        self.play(Create(input_text2))
        #self.wait()

        group=VGroup(node1,node2,node3,node4,node5,node6,node7,group_x1,group_x2,linegroup)
        group.save_state()
        self.play(group.animate.scale(0.75).shift(2*DOWN))
        self.wait()
        
        
        #--------------------
        # 矩阵推导
        
        matrix = MathTex(r"Out=f(\
            \begin{bmatrix} x_1 & x_2 \end{bmatrix}\
            \begin{bmatrix} W_1 & W_2 \\ W_3 & W_4 \end{bmatrix}\
            \begin{bmatrix} W_5 & W_6 \\ W_7 & W_8 \end{bmatrix})\
            \begin{bmatrix} W_9 \\ W_{10} \end{bmatrix}")
        up_matrix=MathTex(r"Out=f(\
            \begin{bmatrix} x_1 & x_2 \end{bmatrix}\
            \begin{bmatrix} W_{11} & W_{12} \\ W_{21} & W_{22} \end{bmatrix})\
            \begin{bmatrix} W_9 \\ W_{10} \end{bmatrix}")
        matrix.move_to(UP*3).scale(0.75)
        up_matrix.move_to(UP*3).scale(0.75)
        self.play(Create(matrix))
        self.wait(2)
        self.play(Transform(matrix,up_matrix))
        self.wait(2)
        self.play(FadeOut(matrix))
        #--------------------
        
        self.play(group.animate.restore())
        self.wait()
        
        self.play(FadeOut(linegroup))
        self.play(FadeOut(node3,node4))
        
        self.wait()
        l_shift_group=VGroup(node5,node6,node7)
        self.play(l_shift_group.animate.shift(2*LEFT))
        group.remove(node3)
        group.remove(node4)
        group.remove(linegroup)
        linegroup.remove(line7,line8,line5,line6)
        line9.shift(2*LEFT)
        line10.shift(2*LEFT)
        group.add(linegroup)
        self.play(group.animate.scale(1.25).shift(DOWN))
       
        
        y=func(x_1,x_2)
        text_y=MathTex(f"y=x_1+x_2+x_1*x_2")
        text_y.move_to(UP*3.5+RIGHT*4.8).scale(0.75)
        self.play(Create(text_y))
        self.wait()
        
        text_lr=Tex(f"learning~rate={lr}")
        text_lr.move_to(UP*3.5+4.8*LEFT).scale(0.75)
        self.play(Create(text_lr))
        self.wait()
        #----------正向传播开始--------------
        value_w=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7]
        #----------文字标注-----------------
        w11=value_w[1]
        w12=value_w[3]
        w21=value_w[2]
        w22=value_w[4]
        w31=value_w[5]
        w32=value_w[6]
        for i in range(200):
            h1=w11*x_1+w12*x_2
            h2=w21*x_1+w22+x_2
            o1=act(h1)
            o2=act(h2)
            out=w31*o1+w32*o2
            e_hat=out-y
            if abs(e_hat)<1e-6:
                print(i) 
                break
            p_w31=e_hat*o1
            p_w32=e_hat*o2
            p_w11=e_hat*w31*p_act(h1)*x_1
            p_w12=e_hat*w31*p_act(h1)*x_2
            p_w21=e_hat*w32*p_act(h2)*x_1
            p_w22=e_hat*w32*p_act(h2)*x_2
            
            w11=w11-0.1*p_w11
            w12=w12-0.1*p_w12
            w21=w21-0.1*p_w21
            w22=w22-0.1*p_w22
            w31=w31-0.1*p_w31
            w32=w32-0.1*p_w32
    

       
        
       

        value_w=[round(value_w[i],4) for i in range(7)]
        
        text11=MathTex(f"W_{{11}}={value_w[1]}")
        text21=MathTex(f"W_{{21}}={value_w[2]}")
        text12=MathTex(f"W_{{12}}={value_w[3]}")
        text22=MathTex(f"W_{{22}}={value_w[4]}")
        text31=MathTex(f"W_{{31}}={value_w[5]}")
        text32=MathTex(f"W_{{32}}={value_w[6]}")
        text11.move_to(line1.get_center()).set_color(BLUE).scale(0.75).shift(0.25*UP)
        text21.move_to(line2.get_center()).set_color(BLUE).scale(0.75).shift(0.5*UP+0.5*LEFT)
        text12.move_to(line3.get_center()).set_color(BLUE).scale(0.75).shift(0.5*DOWN+0.5*RIGHT)
        text22.move_to(line4.get_center()).set_color(BLUE).scale(0.75).shift(0.25*DOWN)
        text31.move_to(line9.get_center()).set_color(BLUE).scale(0.75).shift(0.25*RIGHT)
        text32.move_to(line10.get_center()).set_color(BLUE).scale(0.75).shift(0.25*RIGHT)
            
        arrow11=Arrow(line1.get_start(),line1.get_end(),color=BLUE)
        arrow12=Arrow(line3.get_start(),line3.get_end(),color=BLUE)
        arrow21=Arrow(line2.get_start(),line2.get_end(),color=BLUE)
        arrow22=Arrow(line4.get_start(),line4.get_end(),color=BLUE)
        arrow31=Arrow(line9.get_start(),line9.get_end(),color=BLUE)
        arrow32=Arrow(line10.get_start(),line10.get_end(),color=BLUE)
        
            
        self.play(Write(text11))        
        self.play(Write(text21))        
        self.play(Write(text12))        
        self.play(Write(text22))       
        self.play(Write(text31))       
        self.play(Write(text32)) 
        
        text_ford=Text("正向传播过程").scale(0.8)
        text_ford.move_to(UP*3)
        self.play(FadeIn(text_ford))
        self.wait()
        self.play(FadeOut(text_ford))
        
            
        #----------------计算h1-------------------
        
        
        show_text_h1=MathTex("x_1*W_{11}+x_2*W_{12}=h_1")
        show_text_h1.move_to(UP*3)
        self.play(Transform(line1,arrow11, path_arc=0))
        self.play(Transform(line3,arrow12, path_arc=0))
        self.play(Write(show_text_h1))
        self.wait()
    
        h1=round(value_w[1]*x_1+value_w[3]*x_2,3)
        text=Tex(f"{x_1}*{value_w[1]}+{x_2}*{value_w[3]}={h1}")
        text.move_to(UP*3)
        
        self.play(Transform(show_text_h1,text))
        
        text_h1=MathTex(f"h_{{1}}={h1}")
        text_h1.move_to(UP*3)

        self.play(Transform(show_text_h1,text_h1))
        self.play(show_text_h1.animate.scale(0.5).move_to(node5))
        self.wait(1)
        
        #----------------计算h2-------------------
        self.play(Transform(line2,arrow21))
        self.play(Transform(line4,arrow22))
        
        show_text_h2=MathTex("x_1*W_{12}+x_2*W_{22}=h2")
        show_text_h2.move_to(UP*3)
        self.play(Create(show_text_h2))
        self.wait()
        
        h2=round(value_w[2]*x_1+value_w[4]*x_2,3)
        text=Tex(f"{x_1}*{value_w[2]}+{x_2}*{value_w[4]}={h2}")
        text.move_to(UP*3)
        self.play(Transform(show_text_h2,text))
        
        text_h2=MathTex(f"h_{{2}}={h2}")
        text_h2.move_to(UP*3)
        self.play(Transform(show_text_h2,text_h2))
        
        self.play(show_text_h2.animate.scale(0.5).move_to(node6))
        self.wait()
    



        #----------------
        # 创建激活函数文本
        self.play(FadeOut(text_y))
        activ = Text(f"{act_name}").scale(0.5)

        activ.move_to(UP+RIGHT*2.35)
        activ.shift(UP * 0.3)
        self.play(Write(activ))
        self.wait(1)

        # 创建坐标轴
        #ax = Axes(x_range=[-2, 2, 1], y_range=[0, 2, 1]).scale(0.3)
        ax = Axes(x_range=[-x_range, x_range, x_step], y_range=[y_down, y_up, y_step]).scale(0.3)

        ax.next_to(activ, UP)
        self.play(Create(ax))
        self.wait(1)

        # 创建ReLU激活函数
        actfunc = ax.plot(lambda x : act(x), x_range=[-x_range,x_range], color=BLUE)
        self.play(Create(actfunc))
        self.wait(1)


        axegroup=VGroup(activ,ax,actfunc)
        

        
        #----------------计算o1-------------------
        
        show_text_o1=MathTex(f"{act_name}(h_1)=o_1")

        show_text_o1.move_to(UP*3)
        self.play(Create(show_text_o1))
        self.wait()
        
        o1=round(act(h1),3)
        text=Tex(f"{act_name}({h1})={o1}")
        text.move_to(UP*3)
        self.play(Transform(show_text_o1,text))
        self.wait()
        
        at_point = Dot(ax.coords_to_point(o1, act(o1)), color=RED)
        self.play(Transform(show_text_o1, at_point))
        self.wait(1)
        
        
        text_o1=MathTex(f"o_1={o1}")
        text_o1.move_to(UP*3)
        self.play(Transform(show_text_o1,text_o1))
        
        
        self.play(FadeOut(show_text_h1))
        self.play(show_text_o1.animate.scale(0.5).move_to(node5))
        self.wait()
        
        #----------------计算o2-------------------
        
        show_text_o2=MathTex(f"{act_name}(h_2)=o_2")        
        show_text_o2.move_to(UP*3)
        self.play(Create(show_text_o2))
        self.wait()
        
        o2=round(act(h2),3)
        text=MathTex(f"{act_name}({h2})={o2}")
        text.move_to(UP*3)
        self.play(Transform(show_text_o2,text))
        self.wait()
        
        at_point = Dot(ax.coords_to_point(o2, act(o2)), color=RED)
        self.play(Transform(show_text_o2, at_point))
        self.wait(1)
        
        
        text_o2=MathTex(f"o_2={o2}")
        text_o2.move_to(UP*3)
        self.play(Transform(show_text_o2,text_o2))
        self.play(FadeOut(show_text_h2))
        self.play(show_text_o2.animate.scale(0.5).move_to(node6))
        self.wait()

        #-----------------
        self.play(FadeOut(axegroup))
        self.play(FadeIn(text_y))
        
        #----------------计算y_hat-------------------
        
        
            
        self.play(Transform(line9,arrow31))
        self.play(Transform(line10,arrow32))
        
        show_text_y_hat=MathTex("o_1*W_{31}+o_2*W_{32}=Out")
        show_text_y_hat.move_to(UP*3)
        self.play(Create(show_text_y_hat))
        self.wait()
        
        y_hat=round(o1*value_w[5]+o2*value_w[6],3)
        text=Tex(f"{o1}*{value_w[5]}+{o2}*{value_w[6]}={y_hat}")
        text.move_to(UP*3)
        self.play(Transform(show_text_y_hat,text))
        self.wait()
        
        text_y_hat=Tex(f"out={y_hat}")
        text_y_hat.move_to(UP*3)
        self.play(Transform(show_text_y_hat,text_y_hat))
        self.play(show_text_y_hat.animate.scale(0.5).move_to(node7))
        self.wait()
        
        text_out=Tex(f"out={y_hat}")
        text_out.next_to(text_y,DOWN).scale(0.8)
        self.play(Create(text_out))
        self.wait()
        
        #---------正向传播完毕---------------
        
        group.add(text12,text11,text21,text22,text31,text32,show_text_o1,show_text_o2,show_text_y_hat)
        group.save_state()
        self.play(group.animate.scale(0.75).shift(DOWN))
        self.wait()
        
        #--误差反向传播的计算--
        equation = MathTex(
            r"Err=\frac{1}{2}(out-y)^2"
        )
        equation.next_to(text_out,DOWN).scale(0.5)
        self.play(Create(equation))
        
        text_pw11=MathTex(
            r"\frac{\partial Err}{\partial W_{11} }=\frac{\partial Err}{\partial o_1}\
            \frac{\partial o_1}{\partial h_1}\frac{\partial h_1}{\partial W_{11}}",           
        )
        up_text_pw11=MathTex(r"\frac{\partial Err}{\partial W_{11} }=(out-y)W_{31}*\frac{\partial o_1}{\partial h_1}x_1")
        text_pw12=MathTex(
            r"\frac{\partial Err}{\partial W_{12} }=\frac{\partial Err}{\partial o_1}\
            \frac{\partial o_1}{\partial h_1}\frac{\partial h_1}{\partial W_{12}}",  
        )
        up_text_pw12=MathTex(r"\frac{\partial Err}{\partial W_{12} }=(out-y)W_{31}*\frac{\partial o_1}{\partial h_1}x_2")
        
        text_pw21=MathTex(
            r"\frac{\partial Err}{\partial W_{21} }= \frac{\partial Err}{\partial o_2}\
            \frac{\partial o_2}{\partial h_2}\frac{\partial h_2}{\partial W_{21}}",
            
        )
        up_text_pw21=MathTex(r"\frac{\partial Err}{\partial W_{21} }=(out-y)W_{32}*\frac{\partial o_2}{\partial h_2}x_1")
        
        text_pw22=MathTex(
            r"\frac{\partial Err}{\partial W_{22} }= \frac{\partial Err}{\partial o_2}\
            \frac{\partial o_2}{\partial h_2}\frac{\partial h_2}{\partial W_{22}} \\\\",
           
        )
        up_text_pw22=MathTex( r"\frac{\partial Err}{\partial W_{22} }=(out-y)W_{32}*\frac{\partial o_2}{\partial h_2}x_2")
        
        text_pw31=MathTex(
            r"\frac{\partial Err}{\partial W_{31} }=(out-y)o_1"
        )
        text_pw32=MathTex(
            r"\frac{\partial Err}{\partial W_{32} }=(out-y)o_2"
        )
        
        text_pw31.next_to(equation,DOWN,buff=0).scale(0.5)
        self.play(Create(text_pw31))
        self.wait()
        text_pw32.next_to(text_pw31,DOWN,buff=0).scale(0.5)
        self.play(Create(text_pw32))
        self.wait()
        
        text_pw11.next_to(text_pw32,DOWN,buff=0).scale(0.5)
        up_text_pw11.next_to(text_pw32,DOWN,buff=0).scale(0.5)
        self.play(Create(text_pw11))
        self.wait()
        self.play(Transform(text_pw11,up_text_pw11))
        
        text_pw12.next_to(text_pw11,DOWN,buff=0).scale(0.5)
        up_text_pw12.next_to(text_pw11,DOWN,buff=0).scale(0.5)
        self.play(Create(text_pw12))
        self.wait()
        self.play(Transform(text_pw12,up_text_pw12))
        
        text_pw21.next_to(text_pw12,DOWN,buff=0).scale(0.5)
        up_text_pw21.next_to(text_pw12,DOWN,buff=0).scale(0.5)
        self.play(Create(text_pw21))
        self.wait()
        self.play(Transform(text_pw21,up_text_pw21))
        
        text_pw22.next_to(text_pw21,DOWN,buff=0).scale(0.5)
        up_text_pw22.next_to(text_pw21,DOWN,buff=0).scale(0.5)
        self.play(Create(text_pw22))
        self.wait()
        self.play(Transform(text_pw22,up_text_pw22))
        self.wait()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        self.play(group.animate.restore())
        #---------开始反向传播---------------
        
        

        
        text_back=Text("反向传播过程").scale(0.8)
        text_back.move_to(UP*3)
        self.play(FadeIn(text_back))
        self.wait()
        self.play(FadeOut(text_back))
        
        #------计算梯度---------
        dw31=round((y_hat-y)*o1,4)
        dw32=round((y_hat-y)*o2,3)
        
        dw11=round((y_hat-y)*value_w[5]*p_act(h1)*x_1,3)
        dw12=round((y_hat-y)*value_w[5]*p_act(h1)*x_2,3)
        dw21=round((y_hat-y)*value_w[6]*p_act(h2)*x_1,3)
        dw22=round((y_hat-y)*value_w[6]*p_act(h2)*x_2,3)
        
        text_dw11=MathTex(f"\\frac{{\partial Err}}{{\partial W_{{11}}}}={dw11}",font_size=30)
        text_dw11.next_to(text11,DOWN,buff=0.1).scale(0.75).set_color(RED)
        
        text_dw12=MathTex(f"\\frac{{\partial Err}}{{\partial W_{{12}}}}={dw12}",font_size=30)
        text_dw12.next_to(text12,DOWN,buff=0.1).scale(0.75).set_color(RED)
        
        text_dw21=MathTex(f"\\frac{{\partial Err}}{{\partial W_{{21}}}}={dw21}",font_size=30)
        text_dw21.next_to(text21,DOWN,buff=0.1).scale(0.75).set_color(RED)
        
        text_dw22=MathTex(f"\\frac{{\partial Err}}{{\partial W_{{22}}}}={dw22}",font_size=30)
        text_dw22.next_to(text22,DOWN,buff=0.1).scale(0.75).set_color(RED)
        
        text_dw31=MathTex(f"\\frac{{\partial Err}}{{\partial W_{{31}}}}={dw31}",font_size=30)
        text_dw31.next_to(text31,DOWN,buff=0.2).scale(0.75).set_color(RED)
        
        text_dw32=MathTex(f"\\frac{{\partial Err}}{{\partial W_{{32}}}}={dw32}",font_size=30)
        text_dw32.next_to(text32,DOWN,buff=0.2).scale(0.75).set_color(RED)
        
        #----显示D w31 w32-----------
        arrowd31=Arrow(line9.get_end(),line9.get_start(),color=RED,buff=0)
        arrowd32=Arrow(line10.get_end(),line10.get_start(),color=RED,buff=0)
        self.play(Transform(line9,arrowd31))
        self.play(Create(text_dw31))
        self.wait()
        
        self.play(Transform(line10,arrowd32))
        self.play(Create(text_dw32))
        self.wait()
        
        #----显示D w11 w12 w21 w22-----------
        
        arrodw21=Arrow(line2.get_end(),line2.get_start(),color=RED,buff=0)
        arrodw22=Arrow(line4.get_end(),line4.get_start(),color=RED,buff=0)
        arrodw11=Arrow(line1.get_end(),line1.get_start(),color=RED,buff=0)
        arrodw12=Arrow(line3.get_end(),line3.get_start(),color=RED,buff=0)
        
        
        self.play(Transform(line1,arrodw11))
        self.play(Create(text_dw11))
        self.wait()
        
        self.play(Transform(line3,arrodw12))
        self.play(Create(text_dw12))
        self.wait()
        
        self.play(Transform(line2,arrodw21))
        self.play(Create(text_dw21))
        self.wait()
        
        self.play(Transform(line4,arrodw22))
        self.play(Create(text_dw22))
        self.wait()
        
        #-----------参数更新------------
        value_w[5]=round(value_w[5]-lr*dw31,3)
        value_w[6]=round(value_w[6]-lr*dw32,3)
        
        up_text_31=Tex(f"w31={value_w[5]}")
        up_text_31.scale(0.75).set_color(ORANGE).shift(0.25*RIGHT).move_to(line9.get_center())
        self.play(FadeOut(text31))
        self.play(Transform(text_dw31,up_text_31))
        self.wait()
        
        up_text_32=Tex(f"w32={value_w[6]}")
        up_text_32.scale(0.75).set_color(ORANGE).shift(0.25*RIGHT).move_to(line10.get_center())
        self.play(FadeOut(text32))
        self.play(Transform(text_dw32,up_text_32))
        self.wait()
        
        value_w[4]=round(value_w[4]-lr*dw22,3)
        value_w[2]=round(value_w[2]-lr*dw21,3)
        value_w[3]=round(value_w[3]-lr*dw12,3)
        value_w[1]=round(value_w[1]-lr*dw11,3)
        
        up_text_11=Tex(f"w11={value_w[1]}")
        up_text_11.move_to(line1.get_center()).scale(0.75).set_color(ORANGE).shift(0.25*UP)
        self.play(FadeOut(text11))
        self.play(Transform(text_dw11,up_text_11))
        self.wait()
        
        up_text_21=Tex(f"w21={value_w[2]}")
        up_text_21.move_to(line2.get_center()).scale(0.75).set_color(ORANGE).shift(0.5*UP+0.5*LEFT)
        self.play(FadeOut(text21))
        self.play(Transform(text_dw21,up_text_21))
        self.wait()
        
        up_text_12=Tex(f"w12={value_w[3]}")
        up_text_12.move_to(line3.get_center()).scale(0.75).set_color(ORANGE).shift(0.25*UP)
        self.play(FadeOut(text12))
        self.play(Transform(text_dw12,up_text_12))
        self.wait()
        
        up_text_22=Tex(f"w22={value_w[4]}")
        up_text_22.move_to(line4.get_center()).scale(0.75).set_color(ORANGE).shift(0.25*UP)
        self.play(FadeOut(text22))
        self.play(Transform(text_dw22,up_text_22))
        self.wait(3)
        print(f"y_hat={out}")
        print(f"y={y}")