from manim import *
import itertools as it
from types import SimpleNamespace

# A customizable Sequential Neural Network
class NeuralNetworkMobject(VGroup):
    CONFIG = {
        "neuron_radius": 0.4,
        "neuron_to_neuron_buff": MED_SMALL_BUFF,
        "layer_to_layer_buff": LARGE_BUFF,
        "output_neuron_color": GREEN,
        "input_neuron_color": BLUE,
        "hidden_layer_neuron_color": WHITE,
        "neuron_stroke_width": 2,
        "neuron_fill_color": GREEN,
        "edge_color": LIGHT_GREY,
        "edge_stroke_width": 2,
        "edge_propogation_color": YELLOW,
        "edge_propogation_time": 1,
        "max_shown_neurons": 16,
        "max_layers": 5,
        "brace_for_large_layers": True,
        "average_shown_activation_of_large_layer": True,
        "include_output_labels": False,
        "arrow": False,
        "arrow_tip_size": 0.1,
        "left_size": 1,
        "neuron_fill_opacity": 1
    }
    # Constructor with parameters of the neurons in a list
    def __init__(self, neural_network, **kwargs):
        self.settings = self.CONFIG.copy()
        self.settings.update(kwargs)
        VGroup.__init__(self)
        self.layer_sizes = neural_network
        self.add_neurons()
        self.add_edges()
        self.add_to_back(self.layers)
    # Helper method for constructor
    def add_neurons(self):
        args = SimpleNamespace(**self.settings)

        layers_list = []
        for index, size in enumerate(self.layer_sizes):
            layers_list.append(self.get_layer(size, index))
        
        layers = VGroup(*layers_list)

        layers.arrange_submobjects(RIGHT, buff=args.layer_to_layer_buff)
        self.layers = layers
        if args.include_output_labels:
            self.label_outputs_text()
    # Helper method for constructor
    def get_nn_fill_color(self, index):
        args = SimpleNamespace(**self.settings)

        if index == -1 or index == len(self.layer_sizes) - 1:
            return args.output_neuron_color
        if index == 0:
            return args.input_neuron_color
        else:
            return args.hidden_layer_neuron_color
    # Helper method for constructor
    def get_layer(self, size, index=-1):
        args = SimpleNamespace(**self.settings)

        layer = VGroup()
        n_neurons = size
        if n_neurons > args.max_shown_neurons:
            n_neurons = args.max_shown_neurons
        neurons = VGroup(*[
            Circle(
                radius=args.neuron_radius,
                stroke_color=self.get_nn_fill_color(index),
                fill_color=BLACK
            )
            for x in range(n_neurons)
        ])
        neurons.arrange_submobjects(
            DOWN, buff=args.neuron_to_neuron_buff
        )
        for neuron in neurons:
            neuron.edges_in = VGroup()
            neuron.edges_out = VGroup()
        layer.neurons = neurons
        layer.add(neurons)

        if size > n_neurons:
            dots = MathTex("\\vdots")
            dots.move_to(neurons)
            VGroup(*neurons[:len(neurons) // 2]).next_to(
                dots, UP, MED_SMALL_BUFF
            )
            VGroup(*neurons[len(neurons) // 2:]).next_to(
                dots, DOWN, MED_SMALL_BUFF
            )
            layer.dots = dots
            layer.add(dots)
            if args.brace_for_large_layers:
                brace = Brace(layer, LEFT)
                brace_label = brace.get_tex(str(size))
                layer.brace = brace
                layer.brace_label = brace_label
                layer.add(brace, brace_label)

        return layer
    
    # Helper method for constructor
    def add_edges(self):
        self.edge_groups = VGroup()
        for l1, l2 in zip(self.layers[:-1], self.layers[1:]):
            edge_group = VGroup()
            for n1, n2 in it.product(l1.neurons, l2.neurons):
                edge = self.get_edge(n1, n2)
                edge_group.add(edge)
                n1.edges_out.add(edge)
                n2.edges_in.add(edge)
            self.edge_groups.add(edge_group)
        self.add_to_back(self.edge_groups)
    
    # Helper method for constructor
    def get_edge(self, neuron1, neuron2):
        args = SimpleNamespace(**self.settings)
        if args.arrow:
            return Arrow(
                neuron1.get_center(),
                neuron2.get_center(),
                buff=args.neuron_radius,
                stroke_color=args.edge_color,
                stroke_width=args.edge_stroke_width,
                tip_length=args.arrow_tip_size
            )
        return Line(
            neuron1.get_center(),
            neuron2.get_center(),
            buff=args.neuron_radius,
            stroke_color=args.edge_color,
            stroke_width=args.edge_stroke_width,
        )
    
    # Labels each input neuron with a char l or a LaTeX character
    def label_inputs(self, l):
        self.output_labels = VGroup()
        for n, neuron in enumerate(self.layers[0].neurons):
            label = MathTex(f"{l}_"+"{"+f"{n + 1}"+"}")
            label.set_height(0.3 * neuron.get_height())
            label.move_to(neuron)
            self.output_labels.add(label)
        self.add(self.output_labels)

    # Labels each output neuron with a char l or a LaTeX character
    def label_outputs(self, l):
        self.output_labels = VGroup()
        for n, neuron in enumerate(self.layers[-1].neurons):
            # label = MathTex(f"{l}_"+"{"+f"{n + 1}"+"}")
            label = MathTex("{"+f"{n}"+"}")
            label.set_height(0.4 * neuron.get_height())
            label.move_to(neuron)
            self.output_labels.add(label)
        self.add(self.output_labels)

    # Labels each neuron in the output layer with text according to an output list
    def label_outputs_text(self, outputs):
        self.output_labels = VGroup()
        for n, neuron in enumerate(self.layers[-1].neurons):
            label = MathTex(outputs[n])
            label.set_height(0.75*neuron.get_height())
            label.move_to(neuron)
            label.shift((neuron.get_width() + label.get_width()/2)*RIGHT)
            self.output_labels.add(label)
        self.add(self.output_labels)

    # Labels the hidden layers with a char l or a LaTeX character
    def label_hidden_layers(self, l):
        self.output_labels = VGroup()
        for layer in self.layers[1:-1]:
            for n, neuron in enumerate(layer.neurons):
                label = MathTex(f"{l}_{n + 1}")
                label.set_height(0.4 * neuron.get_height())
                label.move_to(neuron)
                self.output_labels.add(label)
        self.add(self.output_labels)
    
    def get_forward_animation(self):
        args = SimpleNamespace(**self.settings)
        animation = AnimationGroup()

        size = len(self.layer_sizes)
        for i in range(size):
            circle_animation = AnimationGroup(*[
                Create(neuron) for neuron in self.layers[i].neurons
            ], lag_ratio=0)

            animation = AnimationGroup(*[animation, circle_animation], lag_ratio=1)

            if(self.layer_sizes[i] > args.max_shown_neurons):
                animation = AnimationGroup(*[animation, 
                                            Write(self.layers[i].dots), 
                                            Create(self.layers[i].brace),
                                            Write(self.layers[i].brace_label)], lag_ratio=1)
            
            if(i == size - 1 and args.include_output_labels):
                animation = AnimationGroup(*[animation,
                                             Write(self.output_labels)], lag_ratio=1)
            
            animation = AnimationGroup(*[animation, Wait(1)], lag_ratio=1)

            if(i < size - 1):
                points = VGroup(*[
                    Dot(color=ORANGE, radius=0.01) for x in self.edge_groups[i]
                ])

                tails = VGroup(*[
                    TracedPath(point.get_center, dissipating_time=0.5, stroke_color=ORANGE) for point in points
                ])

                self.add(tails)
                
                dl_animation = AnimationGroup(*[
                    MoveAlongPath(d, l) for d, l in zip(points, self.edge_groups[i])
                ])
                
                animation = AnimationGroup(*[
                    animation, dl_animation, Uncreate(points)
                ], lag_ratio=1)
        return animation