 
# mysetup.py
from distutils.core import setup
import glob
import py2exe

setup(console=["helloworld.py"],
      data_files=[("bitmaps",
                   ["bm/large.gif", "bm/small.gif"]),
                  ("fonts",
                   glob.glob("fonts\\*.fnt"))],
)
159 280 101 212 224 379 179 264 222 362 168 250 149 260 485 170
