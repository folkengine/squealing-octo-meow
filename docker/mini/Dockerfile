FROM jupyter/minimal-notebook

# Based on the Jupyter DataScience Notebook
# 
# https://github.com/jupyter/docker-stacks/blob/master/minimal-notebook/Dockerfile
# https://github.com/jupyter/docker-stacks/blob/master/datascience-notebook/Dockerfile
# 

MAINTAINER Chris Baker <ignatz@gmail.com>

# From https://github.com/jupyter/docker-stacks/blob/master/datascience-notebook/Dockerfile

#USER root
#
## R pre-requisites
#RUN apt-get update && \
#    apt-get install -y --no-install-recommends \
#    libxrender1 \
#    fonts-dejavu \
#    gfortran \
#    gcc && apt-get clean
#
## Julia dependencies
#RUN apt-get update && \
#    apt-get install -y --no-install-recommends \
#    julia \
#    libnettle4 && apt-get clean

USER jovyan

# Install Python 3 packages
RUN conda install --yes \
    'ipywidgets=4.0*' \
    'pandas=0.16*' \
    'matplotlib=1.4*' \
    'scipy=0.15*' \
    'seaborn=0.6*' \
    'scikit-learn=0.16*' \
    'scikit-image=0.11*' \
    'sympy=0.7*' \
    'cython=0.22*' \
    'patsy=0.3*' \
    'statsmodels=0.6*' \
    'cloudpickle=0.1*' \
    'dill=0.2*' \
    'numba=0.20*' \
    'bokeh=0.9*' \
    && conda clean -yt

# Install IJulia packages as jovyan and then move the kernelspec out
# to the system share location. Avoids problems with runtime UID change not
# taking effect properly on the .local folder in the jovyan home dir.
#RUN julia -e 'Pkg.add("IJulia")' && \
#    mv /home/$NB_USER/.local/share/jupyter/kernels/* $CONDA_DIR/share/jupyter/kernels/ && \
#    chmod -R go+rx $CONDA_DIR/share/jupyter && \
#    rm -rf /home/$NB_USER/.local/share
#RUN julia -e 'Pkg.add("Gadfly")' && julia -e 'Pkg.add("RDatasets")'

USER root

# Custom

RUN apt-get update && apt-get install -y apt-utils

# To install or upgrade MuseScore:
RUN apt-get install -y musescore

# Add LilyPond Stable
# http://www.lilypond.org/
RUN apt-get install -y lilypond

# Upgrade pip
RUN pip install --upgrade pip

# Add PyAudio
RUN apt-get install -y portaudio19-dev
RUN pip install pyaudio

# install Music21
RUN pip install music21

# Install Python Imaging Library
#RUN pip install image
#RUN $PY2_DIR/bin/pip install image

# Pygame Python 3 install - Does this next bit work?!
RUN apt-get install -y mercurial
RUN apt-get install -y libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev libportmidi-dev
RUN apt-get install -y libswscale-dev libavformat-dev wget curl mc
RUN hg clone https://bitbucket.org/pygame/pygame
RUN cd pygame && python setup.py build && python setup.py install && cd .. && rm -rf pygame

# GDAL
RUN pip install pyproj

RUN conda install --yes basemap pillow && conda clean -yt

# Upgrade matplotlib to 1.5 to remove errors introduced in 1.4.3
# NO LONGER NEEDED
# RUN pip install --upgrade matplotlib
# RUN $PY2_DIR/bin/pip install --upgrade matplotlib

# Upgrade pip AGAIN?!!! Why does it need to do it twice??!
RUN pip install --upgrade pip

RUN pip install httpretty
RUN pip install boto
RUN pip install bz2file
RUN pip install requests
RUN pip install smart-open --no-dependencies

# Gensim
# https://radimrehurek.com/gensim/intro.html
RUN pip install gensim --no-dependencies

# NLTK
RUN pip install nltk
# RUN ME
# RUN python -m nltk.downloader all
# RUN $PY2_DIR/bin/pip install nltk