#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/william/Documentos/Comunicaciones_2/oot/gr-newoot/python
export PATH=/home/william/Documentos/Comunicaciones_2/oot/gr-newoot/build/python:$PATH
export LD_LIBRARY_PATH=/home/william/Documentos/Comunicaciones_2/oot/gr-newoot/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/home/william/Documentos/Comunicaciones_2/oot/gr-newoot/build/swig:$PYTHONPATH
/usr/bin/python2 /home/william/Documentos/Comunicaciones_2/oot/gr-newoot/python/qa_square_ff.py 
