# Immediate Free Recall using PyEPL

The [Vanderbilt Computational Memory Lab](https://memory.psy.vanderbilt.edu) uses a Python-based library for running psychology studies.  Most of these studies are some variant of a paradigm known as [free recall](https://en.wikipedia.org/wiki/Free_recall), in which participants study a list of items and are then prompted to recall items from the list in any order.

This project is designed to show new lab members how [PyEPL](http://pyepl.sourceforge.net/) can be used to construct a basic immediate free recall task.  It is meant to provide a template from which members can develop new, more complex paradigms (e.g., the [asymmetry free recall](https://github.com/jmccluey/asym-free-recall).


## Dependencies

[PyEPL](http://pyepl.sourceforge.net/) - The **Python Experiment Programming Library** is a library for coding psychology experiments in Python.  Downloads are available on the [PyEPL SourceForge page](http://pyepl.sourceforge.net/), or an updated installer is available from the [UPenn Computational Memory Lab](http://memory.psych.upenn.edu/Software).

Please see the Documentation on the PyEPL SourceForge page for the library's basic usage.

## Usage

From within the exp/ifr directory, the standard PyEPL program call can be used:

**python ifr.py --config=config_ifr.py --archive=_DATA_DIR_ --no-eeg -s _SUBJID_**

where _DATA_DIR_ is a path to the directory where the resulting data should be saved (e.g., data) and _SUBJ_ID_ is the subject ID (e.g., SUBJ001).  As this is a strictly behavioral study, the _--no-eeg_ flag indicates that PyEPL sync pulses should not be issued.

_Note:_ As of OS X Lion, the SDL framework may interrupt the use of full-screen display.  Use the _--no-fs_ flag to disable full-screen mode, and use the _--resolution_ if so desired, as described in the PyEPL documentation.

## Documentation

As this is project is meant to be used as teaching tool (with a more experienced user walking through the code), stand-alone documentation of this simple study is forthcoming.
