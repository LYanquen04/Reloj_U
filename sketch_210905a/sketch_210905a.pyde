L = 0
K = 0
def setup():
    size(500, 500)
def draw ():
    background(10,120,10)
    fill(250, 5, 40)
    ellipse(L, height / 2, 150, 150)
    fill(41, 250, 72)
    ellipse(width / 2, K, 100, 100)
    if K > width:
       L = 0 
    else: 
       L = map (second(), 0, 59, 0, width)
    if K > height:
       K = 0
    else:
       K = map(minute(), 0, 59, 0, height)
    global K
    global L 
