from manim import *
import random

class Parallelogram(Polygon):
    def __init__(self, **kwargs):
        Polygon.__init__(self, UL, UR, DR + RIGHT, DL + RIGHT, **kwargs)

class YOLOVisualization(Scene):
    def construct(self):
        title = Text("YOLO's CNN is like..", font_size=24)
        self.play(FadeIn(title))
        self.wait(2)
        self.play(FadeOut(title))

        grid_classification = VGroup(*[Square() for _ in range(49)])
        grid_classification.arrange_in_grid(rows=7, cols=7, buff=0.1)
        grid_classification.scale_to_fit_height(4) 
        grid_classification.to_edge(LEFT, buff=0.5)

        grid_bbox = VGroup(*[Square() for _ in range(49)])
        grid_bbox.arrange_in_grid(rows=7, cols=7, buff=0.1)
        grid_bbox.scale_to_fit_height(3) 
        grid_bbox.to_edge(RIGHT, buff=0.5)

        colors = [BLUE, GREEN, YELLOW]  
        bboxes = [] 

        for square, bbox_square in zip(grid_classification, grid_bbox):
            square.set_fill(random.choice(colors), opacity=1.0)

            bbox_size_factor = random.uniform(0.25, 4.0)
            bbox_height = min(bbox_size_factor * bbox_square.height, grid_bbox.height)
            bbox_width = min(bbox_size_factor * bbox_square.width, grid_bbox.width)
            bbox = Rectangle(height=bbox_height, width=bbox_width)
            bbox.move_to(bbox_square)
            bbox_square.add(bbox)  
            bboxes.append(bbox)

        self.play(*[Create(square) for square in grid_classification], *[Create(bbox) for bbox in bboxes], run_time=3)
        self.wait(2)

        self.play(
            grid_classification.animate.move_to(ORIGIN),
            grid_bbox.animate.move_to(ORIGIN),
            run_time=2
        )
        self.wait(2)

        highlighted_bboxes = random.sample(grid_bbox.submobjects, 2)  
        for bbox in highlighted_bboxes:
            self.play(bbox.submobjects[0].animate.set_color(RED).set_opacity(0.8))


        explanation_text = Text("Highlighted bounding boxes detect objects\nand their color classifications",
                                font_size=24).to_edge(UP)
        self.play(Write(explanation_text))
        self.wait(3)

        yolo_process_text = Text("Place image in grid for processing.\n"
                                 "\t Each cell predicts 2 bounding boxes and classifies objects.\n"
                                 "\t\t Multiply class prediction with confidence to get PrIOU.\n"
                                 "\t\t\t Perform non-max suppression on PrIOU. (Workflow)\n",
                                 font_size=20).to_edge(DOWN)
        self.play(FadeIn(yolo_process_text))
        self.wait(6)
        self.play(FadeOut(yolo_process_text),FadeOut(grid_classification), FadeOut(grid_bbox), FadeOut(explanation_text))

        layers_group = VGroup(
            Parallelogram(), Parallelogram(), Text("...", font_size=36), Parallelogram(), Parallelogram()
        ).arrange(RIGHT, buff=0.5)
        layers_group.scale_to_fit_width(10) 
        layers_text = Text("YOLO has 24 convolutional layers to enhance accuracy", font_size=24).to_edge(UP)
        self.play(FadeIn(layers_group), Write(layers_text))
        self.wait(2)
        self.play(FadeOut(layers_group), FadeOut(layers_text))

if __name__ == "__main__":
    from manim import *
    config.pixel_height = 1080
    config.pixel_width = 1920
    config.frame_rate = 60

    scene = YOLOVisualization()
    scene.render()
