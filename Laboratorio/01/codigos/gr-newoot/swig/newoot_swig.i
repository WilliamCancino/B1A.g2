/* -*- c++ -*- */

#define NEWOOT_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "newoot_swig_doc.i"

%{
#include "newoot/square_ff.h"
#include "newoot/square2_ff.h"
%}

%include "newoot/square_ff.h"
GR_SWIG_BLOCK_MAGIC2(newoot, square_ff);
%include "newoot/square2_ff.h"
GR_SWIG_BLOCK_MAGIC2(newoot, square2_ff);
