"""
Reimplementation of one of the scenes in
"Calculated Movements" by Larry Cuba, 1982-1985

A video-recording of the original is available here:
https://www.youtube.com/watch?v=OkyqP-g_LrY

The original animation was implemented using
the ZGRASS programming language on a Datamax UV1 computer.

This reimplementation in Python with Processing was written by
Felipe Corrêa da Silva Sanches <juca@members.fsf.org>
and is released to the public domain.

October 25th, 2021
"""

def setup():
    size(640, 360)
    background(102)

shape = [
    [9, 1, 1],
    [5, -1, 1],
    [4, 1, 1],
    [11, 1, -1],
    [5, -1, -1],
    [2, 1, -1],
    [4, 1, 1],
    [3, -1, 1],
    [3, -1, -1],
    [2, 1, -1],
    [2, 1, 1],
    [6, -1, 1],
    [3, -1, 0],
    [3, 0, 1],
    [3, -1, 0],
    [3, 0, 1],
    [3, -1, 0],
    [3, 0, -1],
    [3, -1, 0],
    [3, 0, 1],
    [3, -1, 0],
    [3, 0, -1],
    [3, 1, -1],
    [3, 1, 0],
    [3, 1, -1],
    [2, 1, 0],
    [2, 1, -1],
    [2, -1, 0],
    [2, 1, -1],
    [2, -1, 0],
    [2, 1, -1],
    [2, -1, 0],
    [2, -1, 1],
    [1, 1, 0],
    [1, -1, 1],
    [1, 1, 0],
    [3, -1, 1],
    [1, 0, -1],
    [1, 1, -1],
    [1, -1, 0],
    [1, -1, 1],
    [1, -1, 0],
    [1, 1, -1],
    [1, 0, -1],
    [1, -1, 1],
    [1, 0, -1],
    [1, -1, 1],
    [1, 0, 1],
    [1, -1, 1],
    [1, 0, 1],
    [1, -1, 1],
    [1, -1, 0],
    [1, 0, 1],
    [1, -1, 0],
    [1, 0, 1],
    [1, -1, 0],
    [1, 0, -1],
    [1, 1, -1],
    [1, 0, -1],
    [1, 1, 0],
    [1, 0, -1],
    [1, 1, 0],
    [1, 0, -1],
    [1, 1, 0],
    [1, 0, -1],
    [13, 1, 1],
    [5, 1, -1],
    [2, -1, 0],
    [2, 1, 1],
    [3, 1, -1],
    [5, -1, 0],
    [2, -1, 1],
    [3, 1, 1],
    [3, 1, -1],
    [4, 1, 1]
]

LENGTH = 0
for L, dx, dy in shape:
   LENGTH += L

t = 0
p = [
     [0, 4],
     [11, 4],
     [22, 4],
     [28, 2],
     [33, 4],
     [44, 4],
     [55, 4],
     [66, 4],
     [78, 3],
     [89, 4],
     [101, 4],
     [112, 4],
     [123, 4],
     [134, 4],
     [145, 4],
     [156, 4],
     [162, 4],
     [173, 4]
]

LENGTH += p[-1][0] + p[-1][1]


def draw_swarm(shadow=False):
    x = 7
    y = 1
    zoom = 360/20
    pos = 0
    for L, dx, dy in shape:
        for i in range(len(p)):
            k1 = L
            k2 = 0
            p1 = t - p[i][0]
            p2 = p1 - p[i][1]
            if p1 < pos+L:
                k1 = (p1-pos)
            if p2 > pos:
                k2 = (p2-pos)
            if pos < p1 and (pos + L) > p2:
                for n in [0.15, 0.3, 0.45, 0.6, 0.75]:
                    line(zoom * (x + k2*dx - shadow*n), 360 - (zoom * (y + k2*dy - shadow*n)),
                         zoom * (x + k1*dx - shadow*n), 360 - (zoom * (y + k1*dy - shadow*n)))
        pos += L
        x += dx*L
        y += dy*L
        
        
def draw():
    global t
    background(30);
    t = millis()/(53000.0/LENGTH) # The original animation takes roughly 53 seconds

    while t > LENGTH:
        t -= LENGTH

    strokeWeight(6);
    stroke(128);
    draw_swarm(shadow=True)

    strokeWeight(6);
    stroke(255);
    draw_swarm(shadow=False)
    
