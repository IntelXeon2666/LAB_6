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
canvas = Canvas(root, width=WIDTH-400, height=HEIGHT, bg='black')
canvas.grid(column=0, row=0, sticky='W')

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
slider.grid(column=0, row=1)

# Значение переменной, которую мы будем изменять
cur_speed = 1

class Planet:
    def __init__(self, name, size, color, radius, speed, angle, temp, T, E, atmo, diam, grav, mass):
        self.name = name  # имя планеты
        self.size = size  # размер планеты
        self.color = color  # цвет планеты
        self.radius = radius  # расстояние от солнца\центра
        self.speed = speed  # скорость вращения вокруг своей оси
        self.angle = math.radians(angle)  # начальный угол
        
        #описание характеристик планеты при наведении на нее мышью
        self.temp = temp
        self.T = T
        self.E = E
        self.atmo = atmo
        self.diam = diam
        self.grav = grav
        self.mass = mass
        # создаем планету на canvas
        self.body = canvas.create_oval(0, 0, size, size, fill=color, outline=color, tags = "planet")

        # начальные координаты
        if self.name == "Солнце":
            self.x, self.y = WIDTH/2-size/2, HEIGHT/2-size/2
        else:
            orbit_x = self.radius * math.cos(self.angle)
            orbit_y = self.radius * math.sin(self.angle)
            self.x = WIDTH/2-200-size/2 + orbit_x
            self.y = HEIGHT/2-size/2 + orbit_y
            
        canvas.coords(self.body, self.x, self.y, self.x + self.size/2, self.y + self.size/2)
        
    def update(self):
        # изменяем позицию планеты
        orbit_x = self.radius * math.cos(self.angle)
        orbit_y = self.radius * math.sin(self.angle)
        self.x = WIDTH//2-200 + orbit_x
        self.y = HEIGHT//2 + orbit_y
        canvas.coords(self.body, self.x - self.size/2, self.y - self.size/2, self.x + self.size/2, self.y + self.size/2)

        # изменяем угол для следующего шага
        self.angle = (self.angle + math.radians(self.speed*int(cur_speed))) % (2*math.pi)
    
    #попробую написать описание к планетам
    def desc(self, event):
        frame = Frame(root, bg="black")
        frame.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)
        
        title = Label(frame, font = ('Times New Roman',20,'bold'), bg = 'black', fg='white', text=self.name)
        title.grid(row=1,column=3)
        
        empty_label1 = Label(frame, text= "____", bg="black", fg="black")
        empty_label1.grid(row=3,column=3)
        
        temperature = Label(frame, font = ('Times New Roman',16,'bold'), bg = 'black', fg='white', text = ('Температура: '+str(self.temp)+' градусов'))
        temperature.grid(row=3,column=3)
        
        empty_label2 = Label(frame, text= "____", bg="black", fg="black")
        empty_label2.grid(row=4,column=3)
        
        orbital = Label(frame, font =('Times New Roman',20,'bold'), bg = 'black', fg='white', text="Орбитальные характеристики:")
        orbital.grid(row=5, column=3)
        
        radius = Label(frame, font = ('Times New Roman',16,'bold'), bg = 'black', fg='white', text = ('Расстояние до Солнца: '+str(self.radius)+' а.е.'))
        radius.grid(row=6, column=3)
        
        T = Label(frame, font = ('Times New Roman',16,'bold'), bg = 'black', fg='white', text = ('Орбитальный период: '+str(self.T)+' з.л.'))
        T.grid(row=7, column=3)
        
        E = Label(frame, font = ('Times New Roman',16,'bold'), bg = 'black', fg='white', text = ('Эксцентриситет: '+str(self.E)))
        E.grid(row=8, column=3)
        
        empty_label3 = Label(frame, text= "____", bg="black", fg="black")
        empty_label3.grid(row=9,column=3)
        
        atmo = Label(frame, font =('Times New Roman',20,'bold'), bg = 'black', fg='white', text=("Атмосфера:"+self.atmo))
        atmo.grid(row=10, column=3)
        
        empty_label4 = Label(frame, text= "____", bg="black", fg="black")
        empty_label4.grid(row=11,column=3)
        
        phis = Label(frame, font =('Times New Roman',20,'bold'), bg = 'black', fg='white', text="Физические характеристики:")
        phis.grid(row=12,column=3)
        
        diam = Label(frame, font = ('Times New Roman',16,'bold'), bg = 'black', fg='white', text = ('Диаметр: '+str(self.diam)+' км.'))
        diam.grid(row=13, column=3)
        
        grav = Label(frame, font = ('Times New Roman',16,'bold'), bg = 'black', fg='white', text = ('Гравитация: '+str(self.grav)+' м/c^2'))
        grav.grid(row=14, column=3)
        
        mass = Label(frame, font = ('Times New Roman',16,'bold'), bg = 'black', fg='white', text = ('Масса: '+str(self.mass)+' кг'))
        mass.grid(row=15, column=3)
        
    def draw_orbit(self):
        if self.name != "Солнце":
            x, y = WIDTH/2-200, HEIGHT/2
            canvas.create_oval(x - self.radius, y - self.radius,
                            x + self.radius, y + self.radius,
                            width=1, outline="gray")

# создаем сами планеты, задавая параметры (имя, размер, цвет, радиус орбиты, скорость вращения, начальный угол) в таком порядке
sun =     Planet("Солнце",  50, "yellow",0,    0,   0,  19000,0,     0   ,"-"                                                                       ,1391000,0   ,"1.99x10^30" )
mercury = Planet("Меркурий",10, "gray",  39,   1,   0,  167,  0.24,  0.21,"Крайне разрежена,\n состоит из газов и пыли"                             ,4880   ,3.7 ,"3.3x10^23")
venus =   Planet("Венера",  20, "orange",72,   0.9, 45, 464,  0.62,  0.01,"Плотная, состоит\n в основном из углекислого\n газа"                     ,12104  ,8.9 ,"4.87x10^24")
earth =   Planet("Земля",   21, "blue",  100,  0.3, 90, 15,   1.00,  0.02,"Богата кислородом\n и азотом, с небольшим\n количеством углекислого газа",12742  ,9.8 ,"5.97x10^24")
mars =    Planet("Марс",    10, "red",   152,  0.2, 135,-65,  1.88,  0.09,"Разрежена, состоит\n в основном из углекислого\nгаза и азота"            ,6779   ,3.7 ,"6.42x10^23")
jupiter = Planet("Юпитер",  70, "brown", 200,  0.3, 180,-110, 11.86, 0.05,"Газовый гигант,\n состоит в основном из\nводорода и гелия"               ,139822 ,24.8,"1.90x10^27")
saturn =  Planet("Сатурн",  50, "brown", 300,  0.5, 225,-140, 29.46, 0.06,"Газовый гигант,\nсостоит в основном из\nводорода и гелия"                ,116460 ,10.4,"5.68x10^26")
uranus =  Planet("Уран",    40, "blue",  350, 0.2, 270,-195,  84.01, 0.05,"Газовый гигант,\nсостоит в основном из\nводорода и гелия"                ,50724  ,8.9 ,"8.68x10^25")
neptune = Planet("Нептун",  35, "blue",  400 ,0.13, 315,-200, 164.79,0.01,"Газовый гигант,\nсостоит в основном из\nводорода и гелия"                ,49244  ,11.2,"1.02x10^26")

# записываем планеты в массив
planets = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

root.bind("<Escape>", close_window)

#вывод описания по нажатию ЛКМ на планету
canvas.tag_bind(sun.body, "<Button-1>", sun.desc)
canvas.tag_bind(mercury.body, "<Button-1>", mercury.desc)
canvas.tag_bind(venus.body, "<Button-1>", venus.desc)
canvas.tag_bind(earth.body, "<Button-1>", earth.desc)
canvas.tag_bind(mars.body, "<Button-1>", mars.desc)
canvas.tag_bind(jupiter.body, "<Button-1>", jupiter.desc)
canvas.tag_bind(saturn.body, "<Button-1>", saturn.desc)
canvas.tag_bind(uranus.body, "<Button-1>", uranus.desc)
canvas.tag_bind(neptune.body, "<Button-1>", neptune.desc)

def animation():
    for planet in planets:
        planet.draw_orbit()
        planet.update()
    root.after(15, animation)

animation()
root.mainloop()


