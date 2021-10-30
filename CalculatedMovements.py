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
import gi
gi.require_version('Gst', '1.0')
from gi.repository import GLib, Gst
import os
import py5


start_time = 0
playbin = None
font = None
loading_message = True


def setup():
    py5.size(640, 360)

    global font
    # This is not the exact same font, but it has
    # a similar look and is good enough for now...
    font = py5.create_font('3270Condensed-Regular.otf', 30)

    py5.launch_thread(load_sound_file)


def load_sound_file():
    global start_time
    global playbin

    Gst.init()
    mainloop = GLib.MainLoop()

    # setting up a single "playbin" element which
    # handles every part of the playback by itself
    playbin = Gst.ElementFactory.make("playbin", "player")
    playbin.set_property('uri',
                        'file://' + \
                         os.path.abspath('audio/Larry Cuba - Calculated Movements.mp3'))

    #running the playbin
    playbin.set_state(Gst.State.PLAYING)
    start_time = py5.millis()
    mainloop.run()


shape = [[9, 1, 1], [5, -1, 1], [4, 1, 1], [11, 1, -1], [5, -1, -1],
         [2, 1, -1], [4, 1, 1], [3, -1, 1], [3, -1, -1], [2, 1, -1],
         [2, 1, 1], [6, -1, 1], [3, -1, 0], [3, 0, 1], [3, -1, 0],
         [3, 0, 1], [3, -1, 0], [3, 0, -1], [3, -1, 0], [3, 0, 1],
         [3, -1, 0], [3, 0, -1], [3, 1, -1], [3, 1, 0], [3, 1, -1],
         [2, 1, 0], [2, 1, -1], [2, -1, 0], [2, 1, -1], [2, -1, 0],
         [2, 1, -1], [2, -1, 0], [2, -1, 1], [1, 1, 0], [1, -1, 1],
         [1, 1, 0], [3, -1, 1], [1, 0, -1], [1, 1, -1], [1, -1, 0],
         [1, -1, 1], [1, -1, 0], [1, 1, -1], [1, 0, -1], [1, -1, 1],
         [1, 0, -1], [1, -1, 1], [1, 0, 1], [1, -1, 1], [1, 0, 1],
         [1, -1, 1], [1, -1, 0], [1, 0, 1], [1, -1, 0], [1, 0, 1],
         [1, -1, 0], [1, 0, -1], [1, 1, -1], [1, 0, -1], [1, 1, 0],
         [1, 0, -1], [1, 1, 0], [1, 0, -1], [1, 1, 0], [1, 0, -1],
         [13, 1, 1], [5, 1, -1], [2, -1, 0], [2, 1, 1], [3, 1, -1],
         [5, -1, 0], [2, -1, 1], [3, 1, 1], [3, 1, -1], [4, 1, 1]]

LENGTH = 0
for L, dx, dy in shape:
   LENGTH += L

t = 0
p_scene1 = [[0, 4], [11, 4], [22, 4], [28, 2],
            [33, 4], [44, 4], [55, 4], [66, 4],
            [78, 3], [89, 4], [101, 4], [112, 4],
            [123, 4], [134, 4], [145, 4], [156, 4],
            [162, 4], [173, 4]]
p_scene3 = [[0, 20], [30, 20]]

LENGTH_scene1 = LENGTH + p_scene1[-1][0] + p_scene1[-1][1]
LENGTH_scene3 = LENGTH + p_scene3[-1][0] + p_scene3[-1][1]


def draw_swarm(p, grid_size=18, t_delay=0):
    x = 7
    y = 1
    pos = 0
    for L, dx, dy in shape:
        for i in range(len(p)):
            k1 = L
            k2 = 0
            p1 = (t - t_delay) - p[i][0]
            p2 = p1 - p[i][1]
            if p1 < pos+L:
                k1 = (p1-pos)
            if p2 > pos:
                k2 = (p2-pos)
            if pos < p1 and (pos + L) > p2:
                py5.line(grid_size * (x + k2*dx),
                         360 - (grid_size * (y + k2*dy)),
                         grid_size * (x + k1*dx),
                         360 - (grid_size * (y + k1*dy)))
        pos += L
        x += dx*L
        y += dy*L


def draw_scene1(time, total_time):
    global t
    py5.background(30);
    py5.stroke_weight(4);
    t = time/(float(total_time)/LENGTH_scene1)

    def content():
        draw_swarm(p_scene1)
    
    shadowed(content, fill=py5.stroke)


def shadowed(content, x=0, y=0, fill=py5.fill):
    for offs in reversed(range(6)):
        fill(128 + (offs == 0) * 127);
        py5.push_matrix()
        py5.translate(x - offs, y + offs)
        content()
        py5.pop_matrix()


def print_text(text_string, line_spacing=40):
    py5.text_font(font)
    py5.text(text_string, 0, 0)
    py5.translate(0, line_spacing)


def draw_countdown(time, total_time):
    def content():
        print_text("Not Yet Implemented")
        print_text("5, 4, 3, 2, 1...")
        print_text("{}%".format(100*time//total_time))

    py5.background(30);
    shadowed(content, 40, 150)


def draw_copyright(time, total_time):
    def content():
        print_text("Copyright 1985")
        print_text("Solid State Animation")

    py5.background(30);
    shadowed(content, 15, 150);


def draw_title_screen(time, total_time):
    def content():
        print_text("Calculated")
        print_text("Movements")

    py5.background(30);
    shadowed(content, 180, 150);


def draw_tech_support(time, total_time):
    def content():
        print_text("TECHNICAL SUPPORT")
        py5.translate(0, 20)
        print_text("Antenna Audio")
        print_text("Peter Broadwell")
        print_text("Donald Day")
        print_text("Tom DeFanti")
        print_text("Lou Katz")
        print_text("Lyon Lamb Video Animation")

    py5.background(30);
    shadowed(content, 140, 50);


def draw_creative_support(time, total_time):
    def content():
        print_text("CREATIVE SUPPORT")
        print_text("Rob Meyers")
        print_text("Sara Petty")

        py5.translate(0, 50)
        print_text("SOUND")
        print_text("Larry Simon")
        print_text("Liza Kitchell")

    py5.background(30);
    shadowed(content, 140, 50);


def draw_scene2(time, total_time):
    def content():
        print_text("Not Yet Implemented")
        print_text("Scene 2: {}%".format(100*time//total_time))

    py5.background(30);
    shadowed(content, 40, 150)


def draw_scene3(time, total_time):
    global t
    py5.background(30);
    py5.stroke_weight(4);
    t = time/(float(total_time)/LENGTH_scene3)

    def content():
        py5.push_matrix()
        py5.translate(320, -180)

        py5.push_matrix()
        for i in range(6):
            py5.translate(-30, 15)
            draw_swarm(p_scene3, grid_size=9, t_delay=i*0.3)
        py5.pop_matrix()

        py5.translate(-15, 45)
        for i in range(6):
            py5.translate(-30, 15)
            draw_swarm(p_scene3, grid_size=9, t_delay=(5+i)*0.3)

        py5.pop_matrix()

    shadowed(content, fill=py5.stroke)


def draw_scene4(time, total_time):
    def content():
        print_text("Not Yet Implemented")
        print_text("Scene 4: {}%".format(100*time//total_time))

    py5.background(30);
    shadowed(content, 40, 150)


def draw_scene5(time, total_time):
    def content():
        print_text("Not Yet Implemented")
        print_text("Scene 5: {}%".format(100*time//total_time))

    py5.background(30);
    shadowed(content, 40, 150)


def draw_larry_cuba(time, total_time):
    def content():
        print_text("Larry Cuba")

    py5.background(30);
    shadowed(content, 180, 150)


def draw_grant(time, total_time):
    def the_american_film_institute():
        print_text("THE AMERICAN FILM")
        print_text("INSTITUTE")

    def the_national_endownment_for_the_arts():
        print_text("THE NATIONAL ENDOWMENT")
        print_text("FOR THE ARTS")

    py5.background(30);
    py5.translate(250, 50)
    print_text("The Filmmaker")
    print_text("received a production")
    print_text("grant from")
    shadowed(the_american_film_institute)

    py5.translate(0, 80)
    print_text("in association with")
    shadowed(the_national_endownment_for_the_arts)


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
    if start_time == 0:
        return

    #FIXME: py5.clear()
    time = py5.millis() - start_time
    for scene_start, scene_end, render_callback in scenes:
        t_start = parse_timestamp(scene_start)
        t_end = parse_timestamp(scene_end)
        t_total = t_end - t_start
        if time >= t_start and time < t_end:
            render_callback(time - t_start, t_total)


def key_pressed():
    if py5.is_key_pressed:
        if py5.key in ['n', 'N']:
           next_scene()
        elif py5.key in ['p', 'P']:
           prev_scene()


def prev_scene():
    global start_time
    time = py5.millis() - start_time
    for i, scene in enumerate(scenes):
        scene_start, scene_end, _ = scene
        t_start = parse_timestamp(scene_start)
        t_end = parse_timestamp(scene_end)
        if time >= t_start and time < t_end:
            if i > 0:
                prev_start = parse_timestamp(scenes[i-1][0])
                start_time = py5.millis() - prev_start
                seek_time_secs = prev_start / 1000
                playbin.seek_simple(Gst.Format.TIME,
                                    Gst.SeekFlags.FLUSH | Gst.SeekFlags.KEY_UNIT,
                                    seek_time_secs * Gst.SECOND)


def next_scene():
    global start_time
    time = py5.millis() - start_time
    for i, scene in enumerate(scenes):
        scene_start, scene_end, _ = scene
        t_start = parse_timestamp(scene_start)
        t_end = parse_timestamp(scene_end)
        if time >= t_start and time < t_end:
            if i+1 < len(scenes):
                next_start = parse_timestamp(scenes[i+1][0])
                start_time = py5.millis() - next_start
                seek_time_secs = next_start / 1000
                playbin.seek_simple(Gst.Format.TIME,
                                    Gst.SeekFlags.FLUSH | Gst.SeekFlags.KEY_UNIT,
                                    seek_time_secs * Gst.SECOND)


def exiting():
    import sys
    py5.stop_all_threads()
    print("\n"
          "\n"
          "Thanks for watching!\n"
          "\n"
          "If you think you can improve this sketch,"
          " please send a pull request to:\n"
          "https://github.com/felipesanches/CalculatedMovements\n"
          "\n"
          "Press CTRL+C to stop music and close the program.\n"
          "\n")
    sys.exit(0)

py5.run_sketch()
