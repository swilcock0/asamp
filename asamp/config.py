import os
import tkinter as tk
import numpy as np
from math import radians
import sys

try:
    import plotly
    PLOTLY_AVAILABLE = True
except ModuleNotFoundError:
    PLOTLY_AVAILABLE = False


# Data folders and locations
src_fldr = os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "resources"))
reachmap = os.path.join(src_fldr, "pickles", "Reachmap.pickle")


#################

INF = np.inf
PI = np.pi
DISASSEMBLY_VERBOSE = False
