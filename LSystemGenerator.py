#L System Generator

import sys
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (400,400)

import pygame as pyg
import math

WHITE = (255, 255, 255)

class LSystem():
    
    def __init__(self, axiom, rules, dTheta, start, length, lengthFactor, ratio):
        self.sentence = axiom       
        self.rules = rules
        self.theta = math.pi / 2
        self.dTheta = dTheta
        self.start = start
        self.x, self.y = start
        self.length = length
        self.lengthFactor = lengthFactor 
        self.ratio = ratio
        self.positions = []


    def __str__(self):
        return self.sentence
        
    def generate(self):
        self.x, self.y = self.start
        self.theta = math.pi / 2
        self.length *= self.ratio

        newStr = ''
        for char in self.sentence:
            mapped = char
            try:
                mapped = self.rules[char]
            except:
                pass
            newStr += mapped
        self.sentence = newStr

    def draw(self, win):
        for char in self.sentence:
            
            if char == 'F' or char == 'G': 
                x2 = self.x - ( self.length * math.cos(self.theta) )
                y2 = self.y - ( self.length * math.sin(self.theta) )
                pyg.draw.line(win, WHITE, (self.x, self.y), (x2, y2))
                self.x, self.y = x2, y2
            elif char == '+':
                self.theta += self.dTheta
            elif char == '-':
                self.theta -= self.dTheta
            elif char == '[':
                self.positions.append( 
                    {
                        'x' : self.x, 
                        'y' : self.y, 
                        'theta' : self.theta
                    }  
                )  
            elif char == ']':
                position = self.positions.pop()
                self.x, self.y, self.theta = position['x'], position['y'], position['theta']
            elif char == '>':
                self.length *= self.lengthFactor
            elif char == '<':
                self.length /= self.lengthFactor    

            #   { Open a polygon
            #   } Close a polygon and fill it with fill colour


def main():

    pyg.init()
    l_sys_text = sys.argv[1]
    size = int(sys.argv[2]), int(sys.argv[3])
    start = int(sys.argv[4]), int(sys.argv[5])
    length = int(sys.argv[6])
    ratio = float(sys.argv[7])

    system = None
    with open(l_sys_text, 'r') as f:
        axiom = f.readline()
        numRules = int(f.readline())
        rules = {}
        for i in range(numRules):
            rule = f.readline().split(' ')
            rules[rule[0]] = rule[1]
        dTheta = math.radians(float(f.readline()))
        try: 
            lengthFactor = float(f.readline())
        except ValueError: 
            lengthFactor = 0.0
        system = LSystem(axiom, rules, dTheta, start, length, lengthFactor, ratio)



    win = pyg.display.set_mode(size)

    run = True
    while run:
        for event in pyg.event.get():
            if event.type == pyg.QUIT or event.type == pyg.KEYDOWN:
                run = False
            if event.type == pyg.MOUSEBUTTONDOWN:
                win.fill((0, 0, 0))
                system.draw(win)
                system.generate()
        
        pyg.display.flip()

    pyg.quit()

main()

print('git')