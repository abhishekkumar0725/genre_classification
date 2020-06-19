from tensorflow.keras.layers import Input, GlobalAvgPool1D, Dense, Bidirectional, GRU, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.python.framework import ops
from tensorflow.python.keras import backend as K
from tensorflow.python.ops import clip_ops
from tensorflow.python.ops import math_ops
from tensorflow.keras.losses import mae