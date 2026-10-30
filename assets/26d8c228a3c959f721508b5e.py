import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as _practice_fm
import copy as _practice_copy
import sys as _practice_sys
import time as _practice_time
_practice_font_path = '/practice_fonts/PracticeCJK-Regular.ttf'
_practice_fm.fontManager.addfont(_practice_font_path)
_practice_font_name = _practice_fm.FontProperties(fname=_practice_font_path).get_name()
# Preserve the user's common font settings without depending on Windows fonts.
for _practice_alias in ['SimHei', 'Microsoft YaHei', 'SimSun']:
    if not any(entry.name == _practice_alias and entry.fname == _practice_font_path for entry in _practice_fm.fontManager.ttflist):
        _practice_fm.fontManager.ttflist.append(_practice_fm.FontEntry(
            fname=_practice_font_path, name=_practice_alias,
            style='normal', variant='normal', weight=400, stretch='normal'))
_practice_fm.fontManager._findfont_cached.cache_clear()
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = [_practice_font_name, 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

_plot_index = 0
def _save_plots(*args, **kwargs):
    global _plot_index
    for number in plt.get_fignums():
        _plot_index += 1
        plt.figure(number).savefig('figure_%02d.png' % _plot_index, dpi=120, bbox_inches='tight')
    plt.close('all')
plt.show = _save_plots

def _practice_trace(frame, event, arg):
    if _practice_time.monotonic() > _practice_deadline:
        raise TimeoutError('代码运行超过30秒，已停止')
    return _practice_trace
