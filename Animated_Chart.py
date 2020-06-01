#Copyright information at the bottom of the file

"""
The aim of this script is to animate a bar chart and save it for video editing.
No long term production use intendet! First use of matplotlib.

This is part of a media design video project at HAW Hamburg
The project compares public transport and electric cars
"""
from collections import namedtuple

from numpy import arange, clip
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter, FuncAnimation

plt.set_loglevel("info")

Bar = namedtuple('bar', ['max_height', 'start_height', 'color'])

def split_bars(bars):
    """ splits the bars list into lists of
        max_heights, start_heights, colors"""
    max_heights = [bar.max_height for bar in bars]
    start_heights = [bar.start_height for bar in bars]
    colors = [bar.color for bar in bars]
    return max_heights, start_heights, colors


def bar_chart(bars, title, x_labels, y_labels, total_frames=1800, fps=60,
             save=False, show=True):
    Y_axis_scaling = 1.1
    max_heights, start_heights, colors = split_bars(bars)

    fig, ax = plt.subplots(dpi=300, figsize=(1920/300, 1080/300))
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    heights = start_heights
    position = arange(len(max_heights)) + 0.5
    width = [1.0] * len(max_heights)
    rectangles = plt.bar(position, heights, width=width, color=colors)

    plt.title(title)
    plt.xticks(position, x_labels)
    ax.tick_params(axis='x', which='both', length=0, rotation=30)
    plt.ylim((0, int(max(max_heights) * Y_axis_scaling)))
    plt.xlim((0, len(max_heights)))

    # hardcoded legend
    ax.legend((*rectangles[0:3], rectangles[-2]),
              ['Tesla M3', 'BMW i3', 'Smart EQ', 'HVV'],
              loc='upper left', bbox_to_anchor=(0.5, 1.0),
              fontsize='small', ncol=2, framealpha=1.0, edgecolor='white')

    plt.grid(False)
    plt.tight_layout()

    def animate(i):
        print(i)
        nonlocal heights, max_heights, total_frames, rectangles
        speed = (max(max_heights) / (total_frames / 3))
        # increase bars and clip them at max height
        heights = [h + speed for h in heights]
        heights = [clip(h, h , m_h) for h, m_h in zip(heights, max_heights)]
        # scale y axis dynamicly
        if i > int(total_frames * 0.6) + 1:
            plt.ylim((0, int(max(heights) * Y_axis_scaling)))
        # setup second step of the animation
        if i == int(total_frames * 0.6):  # hardcoded changes
            print('Umschaltung')
            max_heights, start_heights, colors = split_bars(cost_maintenance_start_value_bars)
            heights = start_heights
            plt.title('Jährliche Gesammtkosten')

        for bar_heigt, rectangle in zip(heights,rectangles):
            rectangle.set_height(bar_heigt)
        return rectangles

    anim = FuncAnimation(fig, animate, save_count=total_frames,
                         frames=total_frames, interval=1000//fps, repeat=False)

    if save:
        FFwriter = FFMpegWriter(fps=fps)
        anim.save('basic_animation.mp4', writer=FFwriter)
    if show:
        plt.show()

white_bar = Bar(max_height=0, start_height=0, color='#000000')

# Visual representaion https://paletton.com/#uid=72Y1g0kqPrAguzRlqtvt0m0y4h8
color_tesla = '#DC4724' # '#ff5050'
color_bmw = '#402797' # '#527dff'
color_smart = '#DCBB24' # '#ffff52'
color_hvv_1 = '#0C7E3A' # '#9ba2b5'
color_hvv_2 = '#1A9E4F' # '#8196cf'
color_hvv_3 = '#38A966' # '#708ee1'

# Cost of electricity
tesla_j = Bar(max_height=699.49, start_height=0, color=color_tesla)
tesla_n = Bar(max_height=323.25, start_height=0, color=color_tesla)
tesla_t = Bar(max_height=360.35, start_height=0, color=color_tesla)
bmw_j = Bar(max_height=726.13, start_height=0, color=color_bmw)
bmw_n = Bar(max_height=335.56, start_height=0, color=color_bmw)
bmw_t = Bar(max_height=374.07, start_height=0, color=color_bmw)
e_smart_j = Bar(max_height=697.39, start_height=0, color=color_smart)
e_smart_n = Bar(max_height=322.28, start_height=0, color=color_smart)
e_smart_t = Bar(max_height=359.26, start_height=0, color=color_smart)

# Cost of electricity, maintenance and car value
tesla_m_j = Bar(max_height=4809.59, start_height=0, color=color_tesla)
tesla_m_n = Bar(max_height=4433.35, start_height=0, color=color_tesla)
tesla_m_t = Bar(max_height=4470.45, start_height=0, color=color_tesla)
bmw_m_j = Bar(max_height=4358.63, start_height=0, color=color_bmw)
bmw_m_n = Bar(max_height=3968.06, start_height=0, color=color_bmw)
bmw_m_t = Bar(max_height=4006.57, start_height=0, color=color_bmw)
e_smart_m_j = Bar(max_height=2965.09, start_height=0, color=color_smart)
e_smart_m_n = Bar(max_height=2589.98, start_height=0, color=color_smart)
e_smart_m_t = Bar(max_height=2626.96, start_height=0, color=color_smart)

# Cost of electricity, maintenance and car value with start value
tesla_m_s_j = Bar(max_height=tesla_m_j.max_height,
                  start_height=tesla_j.max_height, color=color_tesla)
tesla_m_s_n = Bar(max_height=tesla_m_n.max_height,
                  start_height=tesla_n.max_height, color=color_tesla)
tesla_m_s_t = Bar(max_height=tesla_m_t.max_height,
                  start_height=tesla_t.max_height, color=color_tesla)
bmw_m_s_j = Bar(max_height=bmw_m_j.max_height,
                start_height=bmw_j.max_height, color=color_bmw)
bmw_m_s_n = Bar(max_height=bmw_m_n.max_height,
                start_height=bmw_n.max_height, color=color_bmw)
bmw_m_s_t = Bar(max_height=bmw_m_t.max_height,
                start_height=bmw_t.max_height, color=color_bmw)
e_smart_m_s_j = Bar(max_height=e_smart_m_j.max_height,
                    start_height=e_smart_j.max_height, color=color_smart)
e_smart_m_s_n = Bar(max_height=e_smart_m_n.max_height,
                    start_height=e_smart_n.max_height, color=color_smart)
e_smart_m_s_t = Bar(max_height=e_smart_m_t.max_height,
                    start_height=e_smart_t.max_height, color=color_smart)

# HVV subscription
hvv_2_seme = Bar(max_height=355.20, start_height=0, color=color_hvv_1)
hvv_abo_ab = Bar(max_height=1093.20, start_height=0, color=color_hvv_2)
hvv_abo_ae = Bar(max_height=2186.40, start_height=0, color=color_hvv_3)

# HVV subscription fixed size
hvv_2_seme_s = Bar(max_height=hvv_2_seme.max_height,
                   start_height=hvv_2_seme.max_height, color=color_hvv_1)
hvv_abo_ab_s = Bar(max_height=hvv_abo_ab.max_height,
                   start_height=hvv_abo_ab.max_height, color=color_hvv_2)
hvv_abo_ae_s = Bar(max_height=hvv_abo_ae.max_height,
                   start_height=hvv_abo_ae.max_height, color=color_hvv_3)

cost_bars = (tesla_j, bmw_j, e_smart_j,
             white_bar,
             tesla_n, bmw_n, e_smart_n,
             white_bar,
             tesla_t, bmw_t, e_smart_t,
             white_bar,
             hvv_2_seme, hvv_abo_ab, hvv_abo_ae)

cost_maintenance_bars = (tesla_m_j, bmw_m_j, e_smart_m_j,
                         white_bar,
                         tesla_m_n, bmw_m_n, e_smart_m_n,
                         white_bar,
                         tesla_m_t, bmw_m_t, e_smart_m_t,
                         white_bar,
                         hvv_2_seme, hvv_abo_ab, hvv_abo_ae)

cost_maintenance_start_value_bars = (tesla_m_s_j, bmw_m_s_j, e_smart_m_s_j,
                                     white_bar,
                                     tesla_m_s_n, bmw_m_s_n, e_smart_m_s_n,
                                     white_bar,
                                     tesla_m_s_t, bmw_m_s_t, e_smart_m_s_t,
                                     white_bar,
                                     hvv_2_seme_s, hvv_abo_ab_s, hvv_abo_ae_s)

if __name__ == '__main__':
    bar_chart(cost_bars, title='Jährliche Fahrtkosten',
              x_labels=('', 'Strecke 1', '', '', '', 'Strecke 2', '', '',
                        '', 'Strecke 3', '', '', 'Student', '\nAB', '\nA-E'),
              y_labels=(''), save=True, show=False)

"""
Copyright 2020 Nico Schaefer

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
