#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/william/Documentos/Comunicaciones_2/oot/gr-newoot/lib
export PATH=/home/william/Documentos/Comunicaciones_2/oot/gr-newoot/build/lib:$PATH
export LD_LIBRARY_PATH=/home/william/Documentos/Comunicaciones_2/oot/gr-newoot/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-newoot 
