from manim import *

class TextScene(ThreeDScene):
    def construct(self):
        text1 = Text("Conv-1 Size:6x6 Depth:1", font_size=24).to_edge(DOWN)
        text2 = Text("Conv-2 Size:4x4 Depth:2", font_size=24).to_edge(DOWN)
        text3 = Text("Conv-3 Size:2x2 Depth:4", font_size=24).to_edge(DOWN)

        self.play(Create(text1))
        self.wait(3)
        self.play(FadeOut(text1))

        self.play(Create(text2))
        self.wait(21)
        self.play(FadeOut(text2))

        self.play(Create(text3))
        self.wait(15)
        self.play(FadeOut(text3))

if __name__ == "__main__":
    text_scene = TextScene()
    text_scene.render()
