from PIL import Image, ImageDraw  # grey, color
import pygame
import sys
import os
import random
import time

if "realmap.jpg" in os.listdir():
    os.remove("realmap.jpg")

FPS = 50
WHITE = (255, 255, 255)
pygame.init()  # (заразность,летальность, тяжесть лечения, параметр стойкости в холоде,теплоте)
# формула заразности зараженные+(((заразность+(0,1*уст.к холоду или морозу))*зараженных)+random.randit(1;1+0,01*зараженных)
# начальный кф заразности=0,01   жара = 0,1  холод = 0,06
# летальность  начальный кф = 0,001
# количество умерающих = летальность * зараженных, но если < 30 , то + random.randit(1;1+0,1*зараженных)
contry = {'254, 0, 0': "Канада",  # '':"",
          '0, 0, 254': "Америка",  #
          '0, 150, 149': "Южная Америка",
          '150, 150, 0': "Южная Африка",
          ' 255, 255, 0': "Северная Африка",
          '255, 0, 254': "Южная Европа",
          '0, 254, 0': "Северная Европа",
          '0, 255, 255': "Южная Азия",
          '254, 150, 150': "Северная Азия",
          '100, 0, 0': "Австралия",
          '100, 100, 100': "Гренландия",
          '255, 255, 255': "мир"}

contryinfo = {"Канада": [38000, 0, 0, 1200, -1],  # население, зараженные, мертвые, бюджет страны, температура
              "Америка": [327000, 0, 0, 1500, 0],  #
              "Южная Америка": [428000, 0, 0, 900, 1],
              "Южная Африка": [57000, 0, 0, 500, 0],
              "Северная Африка": [130000, 0, 0, 300, 1],
              "Южная Европа": [60000, 0, 0, 1600, 0],
              "Северная Европа": [25000, 0, 0, 1650, 0],
              "Южная Азия": [1236000, 0, 0, 1400, 0],
              "Северная Азия": [1034000, 0, 0, 1200, -1],
              "Австралия": [24000, 0, 0, 1500, 1],
              "Гренландия": [4000, 0, 0, 1100, -1],
              "мир": [3363000, 0, 0]}


class Map(pygame.sprite.Sprite):  # класс работа с картой
    def __init__(self, filename):
        pygame.sprite.Sprite.__init__(self)
        self.only_color = Image.open("onlycolor.jpg")  # карта определяющая страны
        self.map = Image.open("realmap22.jpg")  # карта у которой только цвета
        self.map.save("realmap.jpg")
        self.map = Image.open("realmap.jpg")  # карта у которой только цвета
        self.map.save("realmap.jpg")
        fullname = os.path.join('bolesn.png')
        pygame.sprite.Sprite.__init__(self)
        self.imagebolesn = pygame.image.load(fullname)
        self.power = 0  # переменная которая следит за кликами на карту
        self.openimage(filename)

    def openimage(self, filename):
        fullname = os.path.join(filename)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(fullname)
        #
        # self.image = self.image.copy()
        # this works on images with per pixel alpha too
        # alpha = 128
        # self.image.fill((255, 255, 255, alpha), None, pygame.BLEND_RGBA_MULT)

        #
        screen.blit(self.image, (0, 0))
        return True
        # self.rect = self.image.get_rect(center=(0, 0))
        # self.panel() подправить
        #

        # image = pygame.image.load("realmap.jpg").convert(24)
        # image.set_alpha(128)
        # screen.fill((255, 255, 255))
        # screen.blit(image, (0, 0))
        # pygame.display.flip()

    def loadpic(self):
        fullname = os.path.join("realmap.jpg")
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(fullname)
        screen.blit(self.image, (0, 0))
        return True

    def panel(self):
        width, height = 1280, 713
        font = pygame.font.Font(None, 30)
        text = font.render("Болезнь", 1, (255, 0, 0))
        text_w = text.get_width()
        text_h = text.get_height()
        #print(text_w + 20, text_h + 20,'лина ширина')
        pygame.draw.rect(screen, (0, 255, 0), (50, 660,
                                               text_w + 20, text_h + 20))
        screen.blit(text, (60, 670))

    def changeimage(self, x, y):  # функция накладывающая оттенок на нажатую страну
        global flag, flug
        if 45 <= x <=157 and 655 <= y <= 713:
            flug = 1
        if flug == 0:
            if self.power == 0:
                name = self.mape(x, y)  # нажатая страна,часть света
                print('{}:{},'.format(name, (x, y)))
                if name != "мир" and name != 'панель':
                    self.power = 1
                    fullname = os.path.join('страны', '{}.{}'.format(name, 'png'))
                    self.image3 = pygame.image.load(fullname).convert_alpha()
                    image = Image.open('{}.{}'.format(name, 'png'))
                    x, y = image.size
                    self.image3 = pygame.transform.scale(self.image3, (int(x * 0.7115), int(0.71 * y)))
                    self.rect = self.image3.get_rect(center=(0, 0))
                    screen.blit(self.image3, (0, 0))
                    pygame.display.flip()
                    # print(name, contryinfo[name])
                elif name == 'панель':
                    self.menupanel()
                else:
                    flag = 0
            elif self.power == 1:
                self.power = 0
                flag = 0
                self.update(1)
        else:
            self.menumape(x, y)

    def mape(self, x, y):  # функция определяющая страну, часть света
        pixels = self.only_color.load()  # переменная которая содерит все пиксели
        r, g, b = pixels[x, y]  # определение цвет пикселя на который нажали
        if ('{}, {}, {}'.format(r, g, b)) in contry:
            znach = contry[('{}, {}, {}'.format(r, g, b))]

        else:
            znach = self.searchznach(('{}, {}, {}'.format(r, g, b)))
        return znach

    def searchznach(self, x):  # ищет страну которая обладает ,приблеженным к основному цвету, оттенком
        x = x.split(", ")
        znachen = ['254, 0, 0', '0, 0, 254', '0, 150, 149', '150, 150, 0', ' 255, 255, 0', '255, 0, 254', '0, 254, 0',
                   # список
                   '0, 255, 255', '254, 150, 150', '100, 0, 0', '100, 100, 100', '255, 255, 255']
        c = []
        for i in znachen:
            i = i.split(", ")
            r = []
            if int(i[0]) - int(x[0]) < 0:
                r.append((int(i[0]) - int(x[0])) * -1)
            else:
                r.append((int(i[0]) - int(x[0])))
            if int(i[1]) - int(x[1]) < 0:

                r.append((int(i[1]) - int(x[1])) * -1)
            else:
                r.append((int(i[1]) - int(x[1])))
            if int(i[2]) - int(x[2]) < 0:
                r.append((int(i[2]) - int(x[2])) * -1)
            else:
                r.append((int(i[2]) - int(x[2])))
            c.append(sum(r))
        ui = min(c)
        h = -1
        for i in c:
            h += 1
            if i == ui:
                break
        return contry[znachen[h]]

    def update(self, flag):  # мена стран
        if flag % 2 == 1:
            screen.blit(self.image, (0, 0))
            pygame.display.flip()
        else:
            screen.blit(self.image3, (0, 0))
            pygame.display.flip()

    def menupanel(self):
        global flug
        flug = 1

    def menumape(self, x, y):
        self.imagebolesn = pygame.transform.scale(self.imagebolesn, (1180, 617))
        screen.blit(self.imagebolesn, (50, 50))


class RasprBolesn():  # класс работа с картой перемещение болезни
    def __init__(self):

        # self.only_color = Image.open("onlycolor.jpg")  # карта определяющая страны
        # self.map = Image.open("realmap.jpg")  # карта у которой только цвета
        self.y = 0
        self.image3 = Image.open("realmap.jpg")
        self.cordinat = {'Австралия': [(1234, 584), (1089, 469), (1035, 496), (1127, 416)],
                         'Южная Азия': [(1030, 391), (1049, 285), (936, 252), (760, 296)],
                         'Северная Азия': [(1047, 70), (541, 99)],
                         'Северная Европа': [(776, 123), (678, 63)],
                         'Северная Африка': [(592, 292), (561, 354)],
                         'Южная Африка': [(665, 485), (775, 473)],
                         'Южная Америка': [(465, 416), (398, 434), ],
                         'Америка': [(284, 325), (161, 223), (365, 205)],
                         'Канада': [(133, 83)],
                         'Гренландия': [(453, 100)],
                         'Южная Европа': [(628, 169)]}
        fullname = os.path.join("realmap.jpg")
        self.image = pygame.image.load(fullname)
        # self.cordinat = {'Америка': (282, 227),
        #                 'rfr':(1100,30),
        #                 'Канада': (200, 122),
        #                 'Южная Америка': (391, 426),
        #                 'Северная Африка': (632, 313),
        #                 'Южная Европа': (669, 177),
        #                 'Северная Европа': (786, 109),
        #                 'Южная Азия': (924, 212),
        #                 'Австралия': (1075, 478),
        #                'Северная Азия': (950, 71)}
        self.contry = ["Канада", "Америка", "Южная Америка", "Северная Африка", "Южная Европа",
                       "Северная Европа", "Южная Азия", "Северная Азия", "Австралия"]
        self.allinfo = [[0] * 6 for _ in range(6)]  # [координаты:(верхняя),(нижняя),(возрастающ,убывающая),(x),(y)]
        for i in range(len(self.allinfo)):  # 5
            self.choice(i)
        self.vib = []

    def choice(self, arg):  # аргумент который поможет заменить не нужный самолет
        global contryinfo
        from1 = random.choice(self.contry)
        into1 = random.choice(self.contry)
        if into1 == from1:
            while into1 == from1:  # 0население, 1зараженные, 2мертвые, 3бюджет страны, 4температура//contryinfo
                into1 = random.choice(self.contry)
        if contryinfo[from1][1] >= contryinfo[from1][0] * 0.35:
            e = contryinfo[from1][1] / contryinfo[from1][0]
            if random.random() < e:
                self.allinfo[arg][5] = 1

        else:
            self.allinfo[arg][5] = 0
            #  'Австралия': [(1234, 584), (1089, 469), (1035, 496), (1127, 416)],
        into1 = self.cordinat[into1]  # [random.randit(0,len())]
        into1 = into1[random.randint(0, len(into1) - 1)]
        from1 = self.cordinat[from1]
        from1 = from1[random.randint(0, len(from1) - 1)]
        self.allinfo[arg][0] = from1
        self.allinfo[arg][1] = into1
        self.allinfo[arg][2] = from1[0]  # [координаты:(верхняя),нижняя,(возрастающ,убывающая),(x),(y),(нижняя)]
        self.allinfo[arg][3] = from1[0]  # x
        self.allinfo[arg][4] = from1[1]  # y
        if from1[0] < into1[0]:
            self.allinfo[arg][2] = 1
        else:
            self.allinfo[arg][2] = 0
        return True

    def uravnenia(self, num):
        if self.allinfo[num][2] == 1:
            self.allinfo[num][3] = self.allinfo[num][3] + 15  # random.randint(15, 25)
            if self.allinfo[num][3] + 5 >= self.allinfo[num][1][0]:  # если координат заходит за границу конечного

                if self.allinfo[num][5] == 1:  # self.allinfo[arg][5] = 1

                    for i in self.cordinat:

                        if self.cordinat[i] == self.allinfo[num][1]:
                            contryinfo[i][1] = 3 * random.randint(1, 5)
                            car2.dobavka(i)
            self.allinfo[num][3] = self.allinfo[num][1][0]  # то меняем
            self.choice(num)



        else:
            self.allinfo[num][3] = self.allinfo[num][3] - random.randint(15, 25)
            if self.allinfo[num][3] - 5 <= self.allinfo[num][1][0]:
                if self.allinfo[num][5] == 1:  # self.allinfo[arg][5] = 1
                    for i in self.cordinat:
                        if self.cordinat[i] == self.allinfo[num][1]:
                            contryinfo[i][1] = 3 * random.randint(1, 5)
                            car2.dobavka(i)
                self.allinfo[num][3] = self.allinfo[num][1][0]  ##
                self.choice(num)

        self.allinfo[num][4] = (((self.allinfo[num][3] - self.allinfo[num][0][0]) * (
                self.allinfo[num][1][1] - self.allinfo[num][0][1])) // (
                                        self.allinfo[num][1][0] - self.allinfo[num][0][0])) + self.allinfo[num][0][
                                   1]  # + random.randint(1,5)  # [координаты:(верхняя),(нижняя),(возрастающ,убывающая),(x),(y)]
        return 'ок'

    def update(self):
        h = 0
        for i in self.allinfo:  # замена
            r = self.uravnenia(h)
            h += 1

        for i in range(len(self.allinfo)):  # tttttttuuuuuuuuu
            self.draw(i)

    def draw(self, num):
        # exec('screen.blit(self.image{}, (self.allinfo[num][2], self.allinfo[num][2]))'.format(num))
        if self.allinfo[num][5] == 1:
            color = (255, 0, 0)
        else:
            color = (255, 255, 255)
        pygame.draw.circle(screen, color, (self.allinfo[num][3], self.allinfo[num][4]), 2)
        pygame.draw.circle(screen, color, (1000, 600), 30)
        # draw = ImageDraw.Draw(self.image3)  # Image.open("realmap.jpg")
        # draw.ellipse((10, 10, 3, 3), fill="red", outline="red")
        # self.image3.save("realmap.jpg")
        # e = car1.loadpic()
        # fullname = os.path.join("realmap.jpg")
        # self.image2 = pygame.image.load(fullname)
        # screen.blit(self.image2, (0, 0))


class Bolesn():  # класс для анализа болезни и ее распостранения
    def __init__(self, x, y):
        global contryinfo
        self.e1 = car1.mape(x, y)

        contryinfo[self.e1][1] = 2
        self.bolezn = [0.01, 0, 0, 0, 0]  # 0заразность,1летальность,2тяжесть, 3устойч к морозу, 4к жаре,
        if contryinfo[self.e1][4] == -1:
            self.bolezn = [0.01, 0, 0, 0.06, 0]
        elif contryinfo[self.e1][4] == 0:
            self.bolezn = [0.01, 0, 0, 0.03, 0.05]
        else:
            self.bolezn = [0.01, 0, 0, 0, 0.1]
        self.e = []
        self.e.append(self.e1)
        # 0население, 1зараженные, 2мертвые, 3бюджет страны, 4температура//contryinfo
        # 0заразность,1летальность,2тяжесть, 3устойч к морозу, 4к жаре//self.bolezn

    def algoritm(self):
        for i in self.e:
            if contryinfo[i][0] <= contryinfo[i][1]:
                contryinfo[i][1] = contryinfo[i][0]
            else:
                if contryinfo[i][4] == -1 and self.bolezn[3] > 0:  # параметр устойчивости к погодным условиям
                    tem = 0.1 * self.bolezn[3]
                elif contryinfo[i][4] == 1 and self.bolezn[4] > 0:
                    tem = 0.1 * self.bolezn[4]
                elif contryinfo[i][4] == 0 and self.bolezn[4] + self.bolezn[3] > 0.18:
                    tem = 0, 1 * ((self.bolezn[4] + self.bolezn[3]) - 0.012)
                else:
                    tem = 0
                contryinfo[i][1] = contryinfo[i][1] + ((self.bolezn[0] + (tem)) * contryinfo[i][1]) + random.randint(1,
                                                                                                                     int(
                                                                                                                         1 + 0.01 *
                                                                                                                         contryinfo[
                                                                                                                             i][
                                                                                                                             1]))
                if self.bolezn[1] > 0:
                    mertv = self.bolezn[1] * contryinfo[i][1]
                    contryinfo[i][2] = int(mertv)
                    contryinfo[i][0] = contryinfo[i][0] - (mertv)

        # (заразность,летальность, тяжесть лечения, параметр стойкости в холоде,теплоте)
        # формула заразности зараженные+(((заразность+(0,1*уст.к холоду или морозу))*зараженных)+random.randit(1;1+0,01*зараженных)
        # начальный кф заразности=0,01   жара = 0,1  холод = 0,06
        # летальность  начальный кф = 0,001
        # количество умерающих = летальность * зараженных, но если < 30 , то + random.randit(1;1+0,1*зараженных)

    def dobavka(self, contry):
        self.e.append(contry)
        print('добавка стране', contry)


running = True
all_sprites = pygame.sprite.Group()
size = width, c = 1280, 713
screen = pygame.display.set_mode(size)
car1 = Map("realmap.jpg")
car = RasprBolesn()  # Bomb(all_sprites)
flag = 0
flug = 0
b = 0
e = 0
h = 0
b1 = 0
MYEVENTTYPE = 1
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if e == 0:
                x, y = event.pos
                if 45 <= x <= 157 and 655 <= y <= 713:
                    flug = 1
                car2 = Bolesn(x, y)
                e += 1
            else:
                x, y = event.pos
                flag = 1
                car1.changeimage(x, y)
        if flag and event.type == MYEVENTTYPE:
            a = time.time()
            if a - b > 0.02:
                h += 1
                car1.update(h)
            b = time.time()
        pygame.display.update()
    if flug == 0:
        all_sprites.draw(screen)
        a1 = time.time()
        car1.panel()
        pygame.time.delay(200)  # algoritm 300
        if e > 0 and a1 - b1 > 0.3:  # 0.3
            car2.algoritm()
            car.update()
            b1 = time.time()
        if flag:
            pygame.time.set_timer(MYEVENTTYPE, 1)
