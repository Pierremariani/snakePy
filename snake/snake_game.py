import tkinter as tk
import random


class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")
        self.width = 400
        self.height = 400
        self.cell_size = 20
        self.direction = 'Right'
        self.running = True

        self.canvas = tk.Canvas(master, width=self.width, height=self.height, bg='black')
        self.canvas.pack()

        self.snake = [(self.width // 2, self.height // 2)]

        self.score = 0

        self.nb = 0

        self.food = 999

        self.firstime = False

        self.master.bind("<KeyPress>", self.change_direction)

    def change_direction(self, event):
        if event.keysym in ["Up", "Down", "Left", "Right"]:
            if (event.keysym == "Up" and self.direction != "Down") or \
                    (event.keysym == "Down" and self.direction != "Up") or \
                    (event.keysym == "Left" and self.direction != "Right") or \
                    (event.keysym == "Right" and self.direction != "Left"):
                self.direction = event.keysym
                if self.nb == 0:
                    self.update()
                    self.nb = 1

    def update(self):
        if self.running:
            if not self.firstime:
                self.place_food()
                self.firstime = True
            self.move_snake()
            self.check_collisions()
            self.update_canvas()
            self.master.after(150, self.update)
        else:
            self.game_over()

    def move_snake(self):
        head_x, head_y = self.snake[0]
        if self.direction == 'Up':
            head_y -= self.cell_size
        elif self.direction == 'Down':
            head_y += self.cell_size
        elif self.direction == 'Left':
            head_x -= self.cell_size
        elif self.direction == 'Right':
            head_x += self.cell_size

        self.snake = [(head_x, head_y)] + self.snake[:-1]

        if (head_x, head_y) == self.food:
            print("mangé")
            self.snake.append(self.snake[-1])
            self.food = self.place_food()
            self.score += 1
            print(self.score)

    def place_food(self):
        while True:
            x = random.randint(0, (self.width // self.cell_size) - 1) * self.cell_size
            y = random.randint(0, (self.height // self.cell_size) - 1) * self.cell_size
            if (x, y) not in self.snake:
                self.food = x,y
                return (x, y)

    def check_collisions(self):
        head_x, head_y = self.snake[0]
        if head_x < 0 or head_x >= self.width or head_y < 0 or head_y >= self.height or (head_x, head_y) in self.snake[1:-1]:
            #or (head_x, head_y) in self.snake[1:]
            self.running = False

    def update_canvas(self):
        self.canvas.delete(tk.ALL)
        a,b = self.snake[0]
        for x, y in self.snake:
            if x == a and y == b:
                self.canvas.create_rectangle(x, y, x + self.cell_size, y + self.cell_size, fill='yellow')
            else:
                self.canvas.create_rectangle(x, y, x + self.cell_size, y + self.cell_size, fill='orange')
        x, y = self.food
        self.canvas.create_rectangle(x, y, x + self.cell_size, y + self.cell_size, fill='red')
    def game_over(self):
        self.canvas.create_text(self.width // 2, self.height // 2, text=f"Game Over! Score: {self.score}", fill='white',font=('Arial', 20))


if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
