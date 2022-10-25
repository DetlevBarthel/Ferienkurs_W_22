from browser import document, window, alert
import random 

def sketch(p): 
  #this p is needed. it will be the processing sketch itself.
  # to do things like background(0) instead do p.background(0)

    def setup():
        p.createCanvas(700, 410)
        p.background(255)
        p.rectMode(p.CENTER)
        
    p.setup = setup
      
myp5 = window.p5.new(sketch)