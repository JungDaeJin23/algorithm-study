class DrawingPaper:
    def __init__(self, n=10):
        self.drawing_paper = [[0] * 10 for _ in range(10)]

    def coloring(self, start, end, color_type):
        for i in range(start[0], end[0] + 1):
            for j in range(start[1], end[1] + 1):
                self.drawing_paper[i][j] += color_type

    def get_colored_area(self, color_type):
        cnt = 0
        for i in range(len(self.drawing_paper)):
            for j in range(len(self.drawing_paper[i])):
                if self.drawing_paper[i][j] == color_type:
                    cnt += 1
        return cnt


# input and output
T = int(input())
for tc in range(1, T + 1):
    Q = int(input())
    drawing_paper_instance = DrawingPaper()
    for _ in range(Q):
        start_r, start_c, end_r, end_c, color = map(int, input().split())
        drawing_paper_instance.coloring((start_r, start_c), (end_r, end_c), color)

    print("#{0} {1}".format(tc, drawing_paper_instance.get_colored_area(3)))