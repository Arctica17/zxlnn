from manim import *
import numpy as np

class LinearRegressionScene(Scene):
    def predict(self,test_data, coef):
        '''
        input:test_data(ndarray):测试样本
        '''
        #********* Begin *********#
        print(test_data.shape)
        p = np.ones((test_data.shape[0], 1))
        test_X = np.hstack((test_data, p))
        return np.dot(test_X, coef)

    def fit_normal(self, x, y):
        '''
        input:train_data(ndarray):训练样本
              train_label(ndarray):训练标签
        '''
        #********* Begin *********#
        X = np.vstack([x, np.ones(len(x))]).T
        m, c = np.linalg.lstsq(X, y, rcond=None)[0]
        # print(self.theta.shape)
        #********* End *********#
        return m, c

    def construct(self):
        # 创建坐标系
        axes = Axes(
            x_range=[0, 7, 1],
            y_range=[0, 6, 1],
            axis_config={"color": BLUE},
            x_axis_config={"numbers_to_include": np.arange(0, 7, 1)},
            y_axis_config={"numbers_to_include": np.arange(0, 6, 1)},
        )

        # 生成数据点
        data = [(1, 2), (2, 3), (3, 3.5), (4, 4), (5, 5), (6, 5.5)]
        points = [Dot(axes.coords_to_point(x, y)) for x, y in data]

        self.play(Create(axes))
        self.wait(0.5)

        if(len(data) < 2):
            raise("Data length should > 2.")
        else:
            # 生成拟合线
            X = []
            Y = []
            for i, (x, y) in enumerate(data):
                X.append(x)
                Y.append(y)
                self.play(Create(points[i]))
                self.wait(0.5)
                if(len(X) >= 2):
                    m, c = self.fit_normal(X, Y)
                    line_graph = axes.plot(
                        lambda x: m * x + c,
                        color=GREEN
                    )

                    # 显示直线
                    self.play(Create(line_graph))
                    self.wait(1)

                    # 淡出直线
                    self.play(FadeOut(line_graph))
                    self.wait(1)
