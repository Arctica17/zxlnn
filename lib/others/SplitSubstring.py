from manim import *

class LogicFormula(Scene):
    def construct(self):
        # 创建第一个公式文本
        text_1 = MathTex(r"(\forall x)((\forall y ) P(x,y) {{ \rightarrow }} \neg (\forall y)(Q(x, y) {{ \rightarrow }} R(x, y) )")
        # 展示第一个公式文本
        self.play(Write(text_1))
        self.wait(1)

        # 向上移动第一个公式文本
        text_1.generate_target()
        text_1.target.shift(UP * 1.5)
        self.play(MoveToTarget(text_1))
        self.wait(1)

        # 创建向下箭头
        arrow = MathTex(r"\downarrow").scale(2)
        arrow.next_to(text_1, DOWN, buff=0.5)
        self.play(Write(arrow))

        # 创建中文文本
        cn = Text("转换箭头符号").scale(0.5)
        cn.next_to(arrow, LEFT)
        self.play(Write(cn))
        self.wait(1)

        # 对Tex对象的第一个部分进行颜色转换动画
        text_1.set_color_by_tex(r"\rightarrow", RED)
        self.wait(1)

        # 创建公式注释
        form_1 = MathTex(r"P \rightarrow Q \Leftrightarrow \neg P \vee Q \\ P \leftrightarrow Q \Leftrightarrow \left ( P \wedge Q \right ) \vee \left (\neg P \wedge \neg Q \right )").scale(0.5)
        form_1.next_to(arrow, RIGHT)
        self.play(Write(form_1))
        self.wait(1)     

        # 创建第二个公式文本
        text_2 = MathTex(r"(\forall x) ({{ \neg }}  (\forall y ) P(x,y)\vee  {{ \neg }} (\forall y)({{ \neg }} Q(x, y)\vee R(x, y) )")
        text_2.next_to(arrow, DOWN, buff=0.5)
        # 展示第二个公式文本
        self.play(Write(text_2))
        self.wait(3)

        # 删除第一步
        self.play(Uncreate(text_1), Uncreate(arrow), Uncreate(cn), Uncreate(form_1))
        self.wait(1)

        # 向上移动第二个公式文本
        text_2.generate_target()
        text_2.target.shift(UP * 2.3)
        self.play(MoveToTarget(text_2))
        self.wait(1)

        # 创建向下箭头
        arrow_2 = MathTex(r"\downarrow").scale(2)
        arrow_2.next_to(text_2, DOWN, buff=0.5)
        self.play(Write(arrow_2))

        # 创建中文文本
        cn_2 = Text("减少否定符号阈值").scale(0.5)
        cn_2.next_to(arrow_2, LEFT)
        self.play(Write(cn_2))
        self.wait(1)

        # 对Tex对象的否定符号进行颜色转换动画
        text_2.set_color_by_tex(r"\neg", RED)
        self.wait(1)

        # 创建第三个公式文本
        text_3 = MathTex(r"(\forall x)({{ (\exists y) }} {{\neg}} P(x,y)\vee {{ (\exists y) }} ( {{ Q(x,y) \wedge \neg R(x,y) }} ))")
        text_3.next_to(arrow_2, DOWN, buff=0.5)
        # 展示第三个公式文本
        self.play(Write(text_3))
        self.wait(3)

        # 对Tex对象的否定符号进行颜色转换动画
        text_3.set_color_by_tex(r"\neg", BLUE)
        self.wait(1)

        # 删除第二步
        self.play(Uncreate(text_2), Uncreate(arrow_2), Uncreate(cn_2))
        text_3.set_color_by_tex(r"\neg", WHITE)
        self.wait(1)

        # 向上移动第三个公式文本
        text_3.generate_target()
        text_3.target.shift(UP * 2.3)
        self.play(MoveToTarget(text_3))
        self.wait(1)

        # 创建向下箭头
        arrow_3 = MathTex(r"\downarrow").scale(2)
        arrow_3.next_to(text_3, DOWN, buff=0.5)
        self.play(Write(arrow_3))

        # 创建中文文本
        cn_3 = Text("对变元标准化").scale(0.5)
        cn_3.next_to(arrow_3, LEFT)
        self.play(Write(cn_3))
        self.wait(1)

        # 对Tex对象的特殊进行颜色转换动画
        text_3.set_color_by_tex(r"\exists", RED)
        text_3.set_color_by_tex(r"\wedge", GREEN)
        self.wait(1)

        # 创建第四个公式文本
        text_4 = MathTex(r"(\forall x)({{ (\exists y) }}\neg P(x,y)\vee {{ (\exists z) }} (Q(x,{{ z }}) \wedge \neg R(x,{{ z }})))")
        text_4.next_to(arrow_3, DOWN, buff=0.5)
        # 展示第四个公式文本
        self.play(Write(text_4))
        self.wait(3)

        # 对Tex对象的z进行颜色转换动画
        text_4.set_color_by_tex(r"z", BLUE)
        self.wait(1)

        # 删除第三步
        self.play(Uncreate(text_3), Uncreate(arrow_3), Uncreate(cn_3))
        text_4.set_color_by_tex(r"z", WHITE)
        self.wait(1)

        # 向上移动第四个公式文本
        text_4.generate_target()
        text_4.target.shift(UP * 2.3)
        self.play(MoveToTarget(text_4))
        self.wait(1)

        # 创建向下箭头
        arrow_4 = MathTex(r"\downarrow").scale(2)
        arrow_4.next_to(text_4, DOWN, buff=0.5)
        self.play(Write(arrow_4))

        # 创建中文文本
        cn_4 = Text("化为前束范式").scale(0.5)
        cn_4.next_to(arrow_4, LEFT)
        self.play(Write(cn_4))
        self.wait(1)

        # 对Tex对象的特殊字符进行颜色转换动画
        text_4.set_color_by_tex(r"\exists", RED)
        self.wait(1)

        # 创建第五个公式文本
        text_5 = MathTex(r"(\forall x){{ (\exists y) }} {{ (\exists z) }}(\neg P(x,{{ y }})\vee (Q(x,{{ z }}) \wedge \neg R(x,{{ z }})))")
        text_5.next_to(arrow_4, DOWN, buff=0.5)
        # 展示第五个公式文本
        self.play(Write(text_5))
        self.wait(3)

        # 对Tex对象的\exists进行颜色转换动画
        text_5.set_color_by_tex(r"\exists", BLUE)
        self.wait(1)

        # 删除第四步
        self.play(Uncreate(text_4), Uncreate(arrow_4), Uncreate(cn_4))
        text_5.set_color_by_tex(r"\exists", WHITE)
        self.wait(1)

        # 向上移动第五个公式文本
        text_5.generate_target()
        text_5.target.shift(UP * 2.3)
        self.play(MoveToTarget(text_5))
        self.wait(1)

        # 创建向下箭头
        arrow_5 = MathTex(r"\downarrow").scale(2)
        arrow_5.next_to(text_5, DOWN, buff=0.5)
        self.play(Write(arrow_5))

        # 创建中文文本
        cn_5 = Text("化为前束范式").scale(0.5)
        cn_5.next_to(arrow_5, LEFT)
        self.play(Write(cn_5))
        self.wait(1)

        # 对Tex对象的特殊字符进行颜色转换动画
        text_5.set_color_by_tex(r"y", RED)
        text_5.set_color_by_tex(r"z", GREEN)
        self.wait(1)

        # 创建第六个公式文本
        text_6 = MathTex(r"(\forall x)(\neg P(x,{{ f(x) }}){{ \vee }} (Q(x,{{ g(x) }}) {{ \wedge }} \neg R(x,{{ g(x) }})))")
        text_6.next_to(arrow_5, DOWN, buff=0.5)
        # 展示第六个公式文本
        self.play(Write(text_6))
        self.wait(3)

        # 对Tex对象的f(x)、g(x)进行颜色转换动画
        text_6.set_color_by_tex(r"f(x)", BLUE)
        text_6.set_color_by_tex(r"g(x)", BLUE)
        self.wait(1)

        # 删除第五步
        self.play(Uncreate(text_5), Uncreate(arrow_5), Uncreate(cn_5))
        text_6.set_color_by_tex(r"x", WHITE)
        self.wait(1)

        # 向上移动第六个公式文本
        text_6.generate_target()
        text_6.target.shift(UP * 2.3)
        self.play(MoveToTarget(text_6))
        self.wait(1)

        # 创建向下箭头
        arrow_6 = MathTex(r"\downarrow").scale(2)
        arrow_6.next_to(text_6, DOWN, buff=0.5)
        self.play(Write(arrow_6))

        # 创建中文文本
        cn_6 = Text("化为Skolem标准形").scale(0.5)
        cn_6.next_to(arrow_6, LEFT)
        self.play(Write(cn_6))
        self.wait(1)

        # 对Tex对象的特殊字符进行颜色转换动画
        text_6.set_color_by_tex(r"\vee", RED)
        text_6.set_color_by_tex(r"\wedge", GREEN)
        self.wait(1)

        # 创建第七个公式文本
        text_7 = MathTex(r"{{ (\forall x) }} ({{ (\neg P(x,f(x)) }} {{ \vee }} Q(x,g(x))) {{ \wedge }} {{ (\neg P(x,f(x)) }} {{ \vee }} \neg R(x,g(x))))")
        text_7.next_to(arrow_6, DOWN, buff=0.5)
        # 展示第七个公式文本
        self.play(Write(text_7))
        self.wait(3)

        # 对Tex对象的特殊字符进行颜色转换动画
        text_7.set_color_by_tex(r"\vee", BLUE)
        text_7.set_color_by_tex(r"\wedge", BLUE)
        text_7.set_color_by_tex(r"(\neg P(x,f(x))", ORANGE)
        self.wait(1)

        # 删除第六步
        self.play(Uncreate(text_6), Uncreate(arrow_6), Uncreate(cn_6))
        text_7.set_color_by_tex(r"\vee", WHITE)
        text_7.set_color_by_tex(r"\wedge", WHITE)
        text_7.set_color_by_tex(r"(\neg P(x,f(x))", WHITE)
        self.wait(1)

        # 向上移动第七个公式文本
        text_7.generate_target()
        text_7.target.shift(UP * 2.3)
        self.play(MoveToTarget(text_7))
        self.wait(1)

        # 创建向下箭头
        arrow_7 = MathTex(r"\downarrow").scale(2)
        arrow_7.next_to(text_7, DOWN, buff=0.5)
        self.play(Write(arrow_7))

        # 创建中文文本
        cn_7 = Text("消去全称量词").scale(0.5)
        cn_7.next_to(arrow_7, LEFT)
        self.play(Write(cn_7))
        self.wait(1)

        # 对Tex对象的特殊字符进行颜色转换动画
        text_7.set_color_by_tex(r"\forall", RED)
        self.wait(1)

        # 创建第八个公式文本
        text_8 = MathTex(r"(\neg P(x,f(x))\vee Q(x,g(x))) {{ \wedge }} (\neg P(x,f(x))\vee \neg R(x,g(x)))")
        text_8.next_to(arrow_7, DOWN, buff=0.5)
        # 展示第八个公式文本
        self.play(Write(text_8))
        self.wait(3)

        # 删除第七步
        self.play(Uncreate(text_7), Uncreate(arrow_7), Uncreate(cn_7))
        self.wait(1)

        # 向上移动第八个公式文本
        text_8.generate_target()
        text_8.target.shift(UP * 2.3)
        self.play(MoveToTarget(text_8))
        self.wait(1)

        # 创建向下箭头
        arrow_8 = MathTex(r"\downarrow").scale(2)
        arrow_8.next_to(text_8, DOWN, buff=0.5)
        self.play(Write(arrow_8))

        # 创建中文文本
        cn_8 = Text("去除合取词").scale(0.5)
        cn_8.next_to(arrow_8, LEFT)
        self.play(Write(cn_8))
        self.wait(1)

        # 对Tex对象的特殊字符进行颜色转换动画
        text_8.set_color_by_tex(r"\wedge", RED)
        self.wait(1)

        # 创建第九个公式文本
        text_9 = MathTex(r"\neg P({{ x }},f({{ x }}))\vee Q({{ x }},g({{ x }})) \\ \neg P({{ x }},f({{ x }}))\vee \neg R({{ x }},g({{ x }}))")
        text_9.next_to(arrow_8, DOWN, buff=0.5)
        # 展示第九个公式文本
        self.play(Write(text_9))
        self.wait(3)

        # 删除第八步
        self.play(Uncreate(text_8), Uncreate(arrow_8), Uncreate(cn_8))
        self.wait(1)

        # 向上移动第九个公式文本
        text_9.generate_target()
        text_9.target.shift(UP * 3.0)
        self.play(MoveToTarget(text_9))
        self.wait(1)

        # 创建向下箭头
        arrow_9 = MathTex(r"\downarrow").scale(2)
        arrow_9.next_to(text_9, DOWN, buff=0.5)
        self.play(Write(arrow_9))

        # 创建中文文本
        cn_9 = Text("更换变量名称").scale(0.5)
        cn_9.next_to(arrow_9, LEFT)
        self.play(Write(cn_9))
        self.wait(1)

        # 对Tex对象的特殊字符进行颜色转换动画
        text_9.set_color_by_tex(r"x", RED)
        self.wait(1)

        # 创建第九个公式文本
        text_10 = MathTex(r"\neg P({{ x }},f({{ x }}))\vee Q({{ x }},g({{ x }})) \\ \neg P({{ y }},f({{ y }}))\vee \neg R({{ y }},g({{ x }}))")
        text_10.next_to(arrow_9, DOWN, buff=0.5)
        # 展示第九个公式文本
        self.play(Write(text_10))
        self.wait(3)

        # 对Tex对象的特殊字符进行颜色转换动画
        text_10.set_color_by_tex(r"y", BLUE)
        self.wait(1)

        # 删除第九步
        self.play(Uncreate(text_9), Uncreate(arrow_9), Uncreate(cn_9))
        text_10.set_color_by_tex(r"y", WHITE)
        self.wait(1)

        # 向上移动第十个公式文本
        text_10.generate_target()
        text_10.target.shift(UP * 1.7)
        self.play(MoveToTarget(text_10))
        self.wait(1)
