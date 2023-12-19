from manim import *

class NumberPuzzle(Scene):
    def computeCost(self, list0):
        ideal_list = [1, 2, 3, 8, None, 4, 7, 6, 5]
        cnt = 0
        for i, item in enumerate(list0):
            # print(item, ideal_list[i])
            if(item == None):
                continue
            rown = i // 3
            coln = i % 3
            if(item == 1):
                cnt = cnt + abs(0 - rown) + abs(0 - coln)
            if(item == 2):
                cnt = cnt + abs(0 - rown) + abs(1 - coln)
            if(item == 3):
                cnt = cnt + abs(0 - rown) + abs(2 - coln)
            if(item == 4):
                cnt = cnt + abs(1 - rown) + abs(2 - coln)
            if(item == 5):
                cnt = cnt + abs(2 - rown) + abs(2 - coln)
            if(item == 6):
                cnt = cnt + abs(2 - rown) + abs(1 - coln)
            if(item == 7):
                cnt = cnt + abs(2 - rown) + abs(0 - coln)
            if(item == 8):
                cnt = cnt + abs(1 - rown) + abs(0 - coln)
        return cnt

    def getCost(self, dist0):
        return dist0["cost"]
    
    def getId(self, dist0):
        return dist0["id"]

    def A(self):
        print("请输入3*3的初始格局(如果为空，就输入E）：")
        init_a = input()
        init_b = input()
        init_c = input()

        init_list = init_a.split() + init_b.split() + init_c.split()
        for i, item in enumerate(init_list):
            try:
                init_list[i] = int(item)
            except:
                pass
        em_index = init_list.index('E')
        init_list[em_index] = None

        node = {"g":init_list, "cost":self.computeCost(init_list), "d": 0}
        OPEN_list = [node]
        all_list = [node]
        # print(node["cost"])

        ideal_list = [1, 2, 3, 8, None, 4, 7, 6, 5]
        last_node = {
            0: None
        }

        cols = 3
        rows = 3

        current_id = 1

        while(True):

            OPEN_list = sorted(OPEN_list, key=self.getCost)

            current_list = OPEN_list[0]["g"]

            print(all_list.index(OPEN_list[0]), OPEN_list[0]["cost"], "id: ", current_id)
            print(current_list)

            depth = OPEN_list[0]["d"] + 1

            if(current_list == ideal_list):
                t_id = all_list.index(OPEN_list[0])
                res_path = [{"g": OPEN_list[0]["g"], "id": t_id}]

                while(last_node[t_id] != None):
                    t_id = last_node[t_id]
                    res_path.append({"g": all_list[t_id]["g"], "id":t_id})
                
                res_path = sorted(res_path, key=self.getId)
                return res_path
            else:
                index = current_list.index(None)
                row_idx = index // rows
                col_idx = index % cols
                # print(row_idx, col_idx)
                if(row_idx - 1 >= 0):
                    new_index = index - cols
                    # print(new_index)
                    new_list = list(current_list)
                    new_list[index], new_list[new_index] = new_list[new_index], new_list[index]
                    node = {"g":new_list, "cost":depth + self.computeCost(new_list), "d":depth}
                    f_idx = last_node[all_list.index(OPEN_list[0])]
                    if(f_idx == None or all_list[f_idx]["g"] != node["g"]):
                        last_node[current_id] = all_list.index(OPEN_list[0])
                        current_id = current_id + 1
                        OPEN_list.append(node)
                        all_list.append(node)
                    # print(new_list)
                    # print(index, new_index)
                    # print(i + self.computeCost(new_list))
                if(col_idx - 1 >= 0):
                    new_index = index - 1
                    new_list = list(current_list)
                    new_list[index], new_list[new_index] = new_list[new_index], new_list[index]
                    node = {"g":new_list, "cost":depth + self.computeCost(new_list), "d":depth}
                    f_idx = last_node[all_list.index(OPEN_list[0])]
                    if(f_idx == None or all_list[f_idx]["g"] != node["g"]):
                        last_node[current_id] = all_list.index(OPEN_list[0])
                        # if(current_id == 9 or current_id == 10):
                        #     print("id", current_id, node["cost"])
                        #     return None
                        current_id = current_id + 1
                        OPEN_list.append(node)
                        all_list.append(node)
                    # print(new_list)
                    # print(index, new_index)
                    # print(i + self.computeCost(new_list))
                if(row_idx + 1 <= rows - 1):
                    new_index = index + cols
                    new_list = list(current_list)
                    new_list[index], new_list[new_index] = new_list[new_index], new_list[index]
                    node = {"g":new_list, "cost":depth + self.computeCost(new_list), "d":depth}
                    f_idx = last_node[all_list.index(OPEN_list[0])]
                    if(f_idx == None or all_list[f_idx]["g"] != node["g"]):
                        last_node[current_id] = all_list.index(OPEN_list[0])
                        current_id = current_id + 1
                        OPEN_list.append(node)
                        all_list.append(node)
                    # print(new_list)
                    # print(index, new_index)
                    # print(i + self.computeCost(new_list))
                if(col_idx + 1 <= cols - 1):
                    new_index = index + 1
                    new_list = list(current_list)
                    new_list[index], new_list[new_index] = new_list[new_index], new_list[index]
                    node = {"g":new_list, "cost":depth + self.computeCost(new_list), "d":depth}
                    f_idx = last_node[all_list.index(OPEN_list[0])]
                    if(f_idx == None or all_list[f_idx]["g"] != node["g"]):
                        last_node[current_id] = all_list.index(OPEN_list[0])
                        current_id = current_id + 1
                        OPEN_list.append(node)
                        all_list.append(node)
                    # print(new_list)
                    # print(index, new_index)
                    # print(i + self.computeCost(new_list))
            
            del OPEN_list[0]
            # return None
            # print(i)

    def construct(self):
        path = self.A()
        path_len = len(path)

        numbers = path[0]["g"]  # 使用 None 代替第九个格子的数字
        # print(numbers)
        rows, cols = 3, 3
        grid = VGroup(*[Square() for _ in range(rows * cols)])
        grid.arrange_in_grid(rows, cols, buff=0.5)

        number_text = [Text(str(num)) if num is not None else None for num in numbers]

        number_group = VGroup(*[num for num in number_text if num is not None])

        # Position numbers within the squares
        for i, number in enumerate(number_text):
            if number is not None:
                number.move_to(grid[i])
        
        print(number_text)
        number_dict = {
            1: numbers.index(1),
            2: numbers.index(2),
            3: numbers.index(3),
            4: numbers.index(4),
            5: numbers.index(5),
            6: numbers.index(6),
            7: numbers.index(7),
            8: numbers.index(8),
        }

        self.play(Create(grid), Create(number_group))
        self.wait(1)

        last_numbers = numbers
        for i in range(1, path_len):
            print(path[i]["g"])
            empty_square_index = last_numbers.index(None)
            number_index = number_dict[path[i]["g"][empty_square_index]]
            print(empty_square_index, number_index)

            number_text[number_index].generate_target()
            number_text[number_index].target.move_to(grid[empty_square_index])

            last_numbers = path[i]["g"]
            self.play(MoveToTarget(number_text[number_index]))

            self.wait(1)
