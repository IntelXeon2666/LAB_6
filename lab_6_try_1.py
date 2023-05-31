from tkinter import *
import math

# задание ширины и длины окна, потребуются для размещения планет
WIDTH, HEIGHT = 1280, 900

# создаем окно
root = Tk()
root.geometry("1280x1024")
root.configure(bg="black")
root.title("Солнечная система")

# создаем холст
canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg='black')
canvas.pack()

#функция, закрывающая окно
def close_window(event=None):
    root.destroy()

# Создаем ползунок
slider = Scale(root, from_=1, to=10, orient=HORIZONTAL)

# Функция, которая связывает значение ползунка со значением переменной
def update_speed(speed):
    global cur_speed
    cur_speed = speed

# Прикрепляем функцию к изменению положения ползунка
slider.config(command=update_speed)

# Значение переменной, которую мы будем изменять
cur_speed = 1

class Planet:
    def __init__(self, name, size, color, radius, speed, angle, temp):
        self.name = name  # имя планеты
        self.size = size  # размер планеты
        self.color = color  # цвет планеты
        self.radius = radius  # расстояние от солнца\центра
        self.speed = speed  # скорость вращения вокруг своей оси
        self.angle = math.radians(angle)  # начальный угол
        
        #описание характеристик планеты при наведении на нее мышью
        self.temp = temp
        
        # создаем планету на canvas
        self.body = canvas.create_oval(0, 0, size, size, fill=color, outline=color, tags = "planet")

        # начальные координаты
        if self.name == "Солнце":
            self.x, self.y = WIDTH/2-size/2, HEIGHT/2-size/2
        else:
            orbit_x = self.radius * math.cos(self.angle)
            orbit_y = self.radius * math.sin(self.angle)
            self.x = WIDTH/2-size/2 + orbit_x
            self.y = HEIGHT/2-size/2 + orbit_y
            
        canvas.coords(self.body, self.x, self.y, self.x + self.size/2, self.y + self.size/2)
        
    def update(self):
        # изменяем позицию планеты
        orbit_x = self.radius * math.cos(self.angle)
        orbit_y = self.radius * math.sin(self.angle)
        self.x = WIDTH//2 + orbit_x
        self.y = HEIGHT//2 + orbit_y
        canvas.coords(self.body, self.x - self.size/2, self.y - self.size/2, self.x + self.size/2, self.y + self.size/2)

        # изменяем угол для следующего шага
        self.angle = (self.angle + math.radians(self.speed+int(cur_speed))) % (2*math.pi)
    
    #попробую написать описание к планетам
    def desc(self, event):
        frame = Frame(root, bg="white")
        frame.place(relx=0.67, rely=0.03, relwidth=0.3, relheight=0.4)
        
        title = Label(frame, font = ('Times New Roman',20,'bold'), bg = 'white', text=self.name)
        title.grid(row=1,column=3)
        
        temperature = Label(frame, font = ('Times New Roman',20,'bold'), bg = 'white', text = ('Температура: ',self.temp, ' градусов'))
        temperature.grid(row=2,column=3)
     
    def draw_orbit(self):
        if self.name != "Солнце":
            x, y = WIDTH/2, HEIGHT/2
            canvas.create_oval(x - self.radius, y - self.radius,
                            x + self.radius, y + self.radius,
                            width=1, outline="gray")

# создаем сами планеты, задавая параметры (имя, размер, цвет, радиус орбиты, скорость вращения, начальный угол) в таком порядке
sun =     Planet("Солнце",  50, "yellow",0,   0,   0,  15500000)
mercury = Planet("Меркурий",10, "gray",  50,  1,   0,  167)
venus =   Planet("Венера",  20, "orange",100, 0.5, 45, 464)
earth =   Planet("Земля",   25, "blue",  150, 0.3, 90, 15)
mars =    Planet("Марс",    20, "red",   200, 0.2, 135,-65)
jupiter = Planet("Юпитер",  40, "brown", 250, 0.3, 180,-110)
saturn =  Planet("Сатурн",  37, "brown", 300, 0.2, 225,-140)
uranus =  Planet("Уран",    24, "blue",  350, 0.2, 270,-195)
neptune = Planet("Нептун",  23, "blue",  400, 0.13, 315,-200)

# записываем планеты в массив
planets = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

root.bind("<Escape>", close_window)

slider.pack()

def animation():
    for planet in planets:
        planet.draw_orbit()
        planet.update()
    root.after(15, animation)

animation()
root.mainloop()


