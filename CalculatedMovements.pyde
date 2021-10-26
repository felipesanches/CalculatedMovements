"""
Reimplementation of some of the scenes in
"Calculated Movements" by Larry Cuba, 1982-1985

A video-recording of the original is available here:
https://www.youtube.com/watch?v=OkyqP-g_LrY

The original animation was implemented using
the ZGRASS programming language on a Datamax UV1 computer.

This reimplementation in Python with Processing was written by
Felipe Corrêa da Silva Sanches <juca@members.fsf.org>
and is released to the public domain.

For now, we're using the original audio and only reimplementing the visuals.
Later we could perhaps use SuperCollider or something similar to also
reimplement the music and sound effects.

October 25th, 2021

Note:
    The font file 3270Condensed-Regular.otf
    created by my friend RBanffy
    was copied from its Debian package.
    Learn more about this font family at https://github.com/rbanffy/3270font
"""

add_library('sound')
start_time = 0
font = None
file = None
loading_message = True


def setup():
    global font
    # This is not the exact same font, but it has
    # a similar look and is good enough for now...
    font = createFont('3270Condensed-Regular.otf', 30)
    size(640, 360)


def load_sound_file():
    global start_time
    global file
    file = SoundFile(this, "audio/Larry Cuba - Calculated Movements.mp3")
    file.play()
    start_time = millis()

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
        

def draw_scene1(time, total_time):
    global t
    background(30);
    t = time/(float(total_time)/LENGTH)

    strokeWeight(6);
    stroke(128);
    draw_swarm(shadow=True)

    strokeWeight(6);
    stroke(255);
    draw_swarm(shadow=False)


def draw_countdown(time, total_time):
    background(30);
    textFont(font)
    text("Not Yet Implemented", 40, 150)
    text("5, 4, 3, 2, 1...", 40, 200)
    text("{}%".format(100*time/total_time), 40, 250)


def draw_copyright(time, total_time):
    background(30);
    textFont(font)
    text("Copyright 1985", 15, 150)
    text("Solid State Animation", 15, 200)


def draw_title_screen(time, total_time):
    background(30);
    textFont(font)
    text("Calculated", 180, 150)
    text("Movements", 180, 200)


def draw_tech_support(time, total_time):
    background(30);
    textFont(font)
    text("Tech Support", 140, 150)


def draw_creative_support(time, total_time):
    background(30);
    textFont(font)
    text("Creative Support", 140, 150)
    text("Sound", 140, 250)


def draw_scene2(time, total_time):
    background(30);
    textFont(font)
    text("Not Yet Implemented", 40, 150)
    text("Scene 2: {}%".format(100*time/total_time), 100, 200)


def draw_scene3(time, total_time):
    background(30);
    textFont(font)
    text("Not Yet Implemented", 40, 150)
    text("Scene 3: {}%".format(100*time/total_time), 100, 200)

def draw_scene4(time, total_time):
    background(30);
    textFont(font)
    text("Not Yet Implemented", 40, 150)
    text("Scene 4: {}%".format(100*time/total_time), 100, 200)

def draw_scene5(time, total_time):
    background(30);
    textFont(font)
    text("Not Yet Implemented", 40, 150)
    text("Scene 5: {}%".format(100*time/total_time), 100, 200)

def draw_larry_cuba(time, total_time):
    background(30);
    textFont(font)
    text("Larry Cuba", 180, 150)

def draw_grant(time, total_time):
    background(30);
    textFont(font)
    text("The Filmmaker", 20, 100)
    text("received a production", 20, 150)
    text("grant from", 20, 200)
    text("THE AMERICAN FILM", 20, 250)
    text("INSTITUTE", 20, 300)


def parse_timestamp(ts):
    minutes, seconds = ts.split(":")
    minutes = int(minutes.strip())
    seconds = float(seconds.strip())
    msecs = int((60 * minutes + seconds) * 1000)
    return msecs

scenes = [
    ["00:00.0", "00:04.0", draw_countdown],
    ["00:10.0", "00:14.0", draw_copyright],
    ["00:13.5", "00:21.0", draw_title_screen],
    ["00:21.0", "00:28.0", draw_tech_support],
    ["00:28.0", "00:36.0", draw_creative_support],
    ["00:39.0", "01:32.0", draw_scene1],
    ["01:36.0", "03:22.0", draw_scene2],
    ["03:23.0", "03:55.0", draw_scene3],
    ["03:56.0", "05:42.0", draw_scene4],
    ["05:44.0", "06:05.0", draw_scene5],
    ["06:10.0", "06:14.0", draw_title_screen],
    ["06:14.0", "06:19.0", draw_larry_cuba],
    ["06:19.0", "06:27.0", draw_grant]
]
def draw():
    global loading_message

    if loading_message:
        background(102)
        textFont(font)
        text("Loading", 180, 150)
        text("Sound File...", 180, 200)
        loading_message = False
        return

    if file is None:
        load_sound_file()
        return

    clear()
    time = millis() - start_time
    for scene_start, scene_end, render_callback in scenes:
        t_start = parse_timestamp(scene_start)
        t_end = parse_timestamp(scene_end)
        t_total = t_end - t_start
        if time >= t_start and time < t_end:
            render_callback(time - t_start, t_total)
