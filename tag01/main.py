from browser import document, window, alert
import random

import test

def sketch(p): 
  # this p is needed. it will be the processing sketch itself.
  # to do things like background(0) instead do p.background(0)

    def setup():
        p.createCanvas(700, 410)

        # Die Hintergrundfarbe kann verändert werden, in dem wir den übergebenen Wert Verändern.
        # Diesen übergebenen Wert nennt man einen Parameter.
        # Die runden Klammern >()< die diesen Wert umschließen, bezeichnet man als Parameterliste.
        p.background(55)
        p.rectMode(p.CENTER)
        
    p.setup = setup
    
myp5 = window.p5.new(sketch)