# LSystemGenerator

This python program graphically displays [L-Systems](https://en.wikipedia.org/wiki/L-system) using basic polar-coordinate math, recursion, and a PyGame GUI.

An L-system or Lindenmayer system is a parallel fractal rewriting system and a type of formal grammar. 

An L-system consists of an alphabet of symbols that can be used to make strings _variables_, a collection of production _constants_ that expand each symbol into some larger string of symbols, an initial _axiom_ string from which to begin construction, and a mechanism for translating the generated strings into geometric structures _rules_. Some systems include an angle of rotation _theta_.

This program can display any fractal in L-System notation, from a simple binary fractal tree to complex recursive curves.

The [Fractals](https://github.com/akshaypkbhat/LSystemGenerator/tree/main/Fractals)https://github.com/akshaypkbhat/LSystemGenerator/tree/main/Fractals folder includes .txt files of fractals in an L-Sytstem format

Run the command in a terminal, providing 6 fields:
  filename width height startX startY length ratio *theta*

Ex: python3 LSystemGenerator.py plant1.txt 800 800 400 800 100 .67 
