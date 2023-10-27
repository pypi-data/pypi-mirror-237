

![Linux](https://img.shields.io/badge/-Linux-grey?logo=linux)
![Usage](https://img.shields.io/badge/Usage-Terminal%20User%20Interface-yellow)
![Python](https://img.shields.io/badge/Python-v3.8%5E-green?logo=python)
![pyTermTk_version](https://img.shields.io/github/v/tag/ceccopierangiolieugenio/pyTermTk?label=version)
[![Test Status](https://img.shields.io/github/actions/workflow/status/ceccopierangiolieugenio/pyTermTk/testing.yml?branch=main&label=tests)](https://github.com/ceccopierangiolieugenio/pyTermTk/actions?query=workflow%3Atesting)
[![pypi_version](https://img.shields.io/pypi/v/pyTermTk?label=pypi)](https://pypi.org/project/pyTermTk)
[![pypi_version](https://img.shields.io/twitter/follow/Pier95886803?style=social&logo=twitter)](https://twitter.com/hashtag/pyTermTk?src=hashtag_click&f=live)

[![screenshot](https://user-images.githubusercontent.com/8876552/206444177-d7e7eb0f-5651-48c7-a38a-76af02312958.png)](https://pypi.org/project/pyTermTk)

## [pyTermTk](https://github.com/ceccopierangiolieugenio/pyTermTk)

(**py**thon **Term**inal **T**ool**k**it) is a Text-based user interface library ([TUI](https://en.wikipedia.org/wiki/Text-based_user_interface))
Evolved from the discontinued project [pyCuT](https://github.com/ceccopierangiolieugenio/pyCuT)
and inspired by a mix of [Qt5](https://www.riverbankcomputing.com/static/Docs/PyQt5/),[GTK](https://pygobject.readthedocs.io/en/latest/), and [tkinter](https://docs.python.org/3/library/tkinter.html) api definition with a touch of personal interpretation

[pyTermTk.Showcase.002.webm](https://user-images.githubusercontent.com/8876552/206490679-2bbdc909-c9bc-41c1-9a50-339b06dabecd.webm)

## Features
- Self Contained (no external lib required)
- Cross compatible: [Linux](https://en.wikipedia.org/wiki/Linux)🐧, [MacOS](https://en.wikipedia.org/wiki/MacOS)🍎, [MS Windows](https://en.wikipedia.org/wiki/Microsoft_Windows)🪟, [HTML5](https://en.wikipedia.org/wiki/HTML5)🌍([Try](https://ceccopierangiolieugenio.github.io/pyTermTk/sandbox/sandbox.html))
- Basic widgets for [TUI](https://en.wikipedia.org/wiki/Text-based_user_interface) development (Button, Label, checkbox, ...)
- Specialized widgets to improve the usability (Windows, Frames, Tables, ...)
- QT Like Layout system to help arrange the widgets in the terminal
- True color support
- Ful/Half/Zero sized Unicode characters 😎
- I am pretty sure there is something else...

## Limitations
- Only the key combinations forwarded by the terminal emulator used are detected (ALT,CTRL may not be handled)

---

## Try the [Sandbox](https://ceccopierangiolieugenio.github.io/pyTermTk/sandbox/sandbox.html) straight from your browser

[![SandBox](https://user-images.githubusercontent.com/8876552/206438915-fdc868b1-32e0-46e8-9e2c-e29f4a7a0e75.png)](https://ceccopierangiolieugenio.github.io/pyTermTk/sandbox/sandbox.html)

Powered by [Pyodide](https://pyodide.org/) and [xterm.js](https://xtermjs.org/) and [CodeMirror5](https://codemirror.net/5/) and [w2ui](https://w2ui.com/)

---

## [the Tutorials](tutorial) and [the Examples](tutorial/000-examples.rst)
Be inspired by [the Tutorials](https://github.com/ceccopierangiolieugenio/pyTermTk/tree/main/tutorial) and [the Examples](https://github.com/ceccopierangiolieugenio/pyTermTk/tree/main/tutorial/000-examples.rst)

## [Api Definitions](https://ceccopierangiolieugenio.github.io/pyTermTk/)
Don't get bored by the [Api Definitions](https://ceccopierangiolieugenio.github.io/pyTermTk/)

## [ttkDesigner](https://github.com/ceccopierangiolieugenio/pyTermTk/tree/main/ttkDesigner)
Smell deliciousness with the official [pyTermTk](https://github.com/ceccopierangiolieugenio/pyTermTk) tool for designing and building Text-based user interfaces ([TUI](https://en.wikipedia.org/wiki/Text-based_user_interface)s)

---

## Install/Upgrade
[pyTermTk](https://github.com/ceccopierangiolieugenio/pyTermTk) is available on [PyPI](https://pypi.org/project/pyTermTk/)
```bash
pip3 install --upgrade pyTermTk
```
## Quick Test/Try - no install required

#### Clone
```bash
git clone https://github.com/ceccopierangiolieugenio/pyTermTk.git
cd pyTermTk
```

#### Run Basic (non ui) input test
```bash
python3 tests/test.input.py
```

#### Demos
```bash
# Press CTRL-C to exit (CTRL-Break on Windows)

# Showcase Demo
python3 demo/demo.py -f

# run the ttkDesigner
python3 -m ttkDesigner

# Paint demo
python3 demo/paint.py

# VSCode like d'n d layout demo
python3 demo/ttkode.py

# early gittk demo
python3 demo/gittk.py

# Text edit with "Pygments" highlight integrated
# it require pygments
#   pip install pygments
python3 tests/test.ui.018.TextEdit.Pygments.py README.md
```

#### Debug
There are few ENV Variables that can be used to force some debugging features;
##### (TERMTK_FILE_LOG) - Log to a file
To force logging to a file
```bash
TERMTK_FILE_LOG=session.log   python3   demo/demo.py
```
##### (TERMTK_STACKTRACE) - Force stacktrace generation with CTRL+C
Use this env variable to force a stacktrace generation to the file defined (i.e. "**stacktrace.txt**")
```bash
TERMTK_STACKTRACE=stacktrace.txt   python3   demo/demo.py
```

#### Profiling

##### [VizTracer](https://pypi.org/project/viztracer/)
this tool is able to generate a tracker file that can be viewed using [Perfetto](https://perfetto.dev) ([UI](https://ui.perfetto.dev/))
```bash
# install cprofilev:
#     pip3 install viztracer
viztracer --tracer_entries 10000010 tests/test.ui.030.menu.01.py

# View the results
# loading the "result.json" in https://ui.perfetto.dev
# or running
vizviewer result.json
```

##### [cProfile](https://docs.python.org/3/library/profile.html), [cProfilev](https://github.com/ymichael/cprofilev)
```bash
python3 -m cProfile -o profiler.bin tests/test.ui.004.py

# install cprofilev:
#     pip3 install cprofilev
cprofilev -f profiler.bin
# open http://127.0.0.1:4000
```
##### py-spy
```bash
# install
pip install py-spy

# run the application
python3 demo/demo.py

# on another terminal run the py-spy
sudo env "PATH=$PATH" \
    py-spy top \
       --pid  $(ps -A -o pid,cmd | grep demo.py | grep -v grep | sed 's,python.*,,')
```
##### pyroscope
[pyroscope](https://pyroscope.io/) can be used as well for profiling

---

## Projects using [pyTermTk](https://github.com/ceccopierangiolieugenio/pyTermTk)
- [ttkDesigner](https://github.com/ceccopierangiolieugenio/pyTermTk/tree/main/ttkDesigner) - the official [pyTermTk](https://github.com/ceccopierangiolieugenio/pyTermTk) tool for designing and building Text-based user interfaces ([TUI](https://en.wikipedia.org/wiki/Text-based_user_interface)s)
- [tlogg](https://github.com/ceccopierangiolieugenio/tlogg) - A fast, advanced log explorer.
- [ttkode](https://github.com/ceccopierangiolieugenio/ttkode) - TerminalToolKit (Studio) Code (editor)
- [pytest-fold](https://github.com/jeffwright13/pytest-fold) - A Pytest plugin to make console output more manageable when there are multiple failed tests
- [pytest-tui](https://github.com/jeffwright13/pytest-tui) - A Text User Interface (TUI) for Pytest, automatically launched after your test run is finished

## Related Projects
- Honourable mention
  - [bpytop](https://github.com/aristocratos/bpytop) - Linux/OSX/FreeBSD resource monitor <br>
    This was the base inspiration for my core library

- Python
  - [urwid](https://github.com/urwid/urwid) - Console user interface library for Python
  - [pyTermGUI](https://github.com/bczsalba/pytermgui) - A simple yet powerful TUI framework for your Python (3.7+) applications
  - [Textual](https://github.com/Textualize/textual) - TUI (Text User Interface) framework for Python inspired by modern web development
  - [Rich](https://github.com/Textualize/rich) - Python library for rich text and beautiful formatting in the terminal
  - [PyCuT](https://github.com/ceccopierangiolieugenio/pyCuT) - terminal graphic library loosely based on QT api (my previous failed attempt)
  - [pyTooling.TerminalUI](https://github.com/pyTooling/pyTooling.TerminalUI) - A set of helpers to implement a text user interface (TUI) in a terminal.

- Non Python
  - [Turbo Vision](http://tvision.sourceforge.net)
  - [ncurses](https://en.wikipedia.org/wiki/Ncurses)
  - [tui.el](https://github.com/ebpa/tui.el) - An experimental text-based UI framework for Emacs modeled after React
