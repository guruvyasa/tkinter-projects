from tkinter import *
# directions = ('UP', 'DOWN', 'RIGHT', 'LEFT')
step_dict = {
                    'UP': (1, -4),
                    'DOWN': (1,4),
                    'RIGHT': (4,1),
                    'LEFT': (-4,1),
                    }

class Ball:
    def __init__(self, canvas, radius, xpos=10, ypos=10, color="red", direction='DOWN'):
        self.canvas = canvas
        self.radius = radius
        self.color = color
        self.id = self.canvas.create_oval(xpos,ypos, xpos+(2*radius), ypos+(2*radius), fill=color)
        # self.in_canvas = True #tracks if the ball is in the canvas
        self.curr_direction = direction
        self.center = self.get_center()

    def get_current_coords(self):
        return self.canvas.coords(self.id)

    def get_center(self):
        coords = self.get_current_coords()
        centerX = sum((coords[0],coords[2])) / 2
        centerY = sum((coords[1],coords[3])) / 2
        return centerX,centerY



    def is_in_canvas(self):
        centerX, centerY = self.get_center()
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        if (abs(centerX - canvas_width) <= self.radius) or \
        (abs(centerY - canvas_height) <= self.radius) or \
        centerY <= self.radius or \
        centerX <= self.radius:
            return False
        else:
            return True



    def move(self):
        # print(direction)

        stepX, stepY = step_dict.get(self.curr_direction)
        curr_pos= self.canvas.coords(self.id)
        # self.canvas.winfo_width()
        self.canvas.move(self.id, stepX, stepY)
        # self.in_canvas = True if self.is_in_canvas() else False




    def bounce(self):
        # self.move(direction='RIGHT')
        print(self.is_in_canvas())

        if not self.is_in_canvas():
            curr_pos= self.get_current_coords()
            if curr_pos[2] >= self.canvas.winfo_width():
                self.curr_direction = 'LEFT'

            elif curr_pos[0] <= 0:
                self.curr_direction = 'RIGHT'
            elif curr_pos[3] >= self.canvas.winfo_height():
                self.curr_direction = 'UP'
            else:
                self.curr_direction = 'DOWN'

        self.move()

        self.canvas.after(100, self.bounce)

root = Tk()
canvas = Canvas(root, width=400, height=400)
canvas.pack()
b = Ball(canvas, 20)
b.bounce()
root.mainloop()
