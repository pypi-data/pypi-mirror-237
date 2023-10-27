.. rst syntax: https://deusyss.developpez.com/tutoriels/Python/SphinxDoc/
.. version conv: https://peps.python.org/pep-0440/
.. icons: https://specifications.freedesktop.org/icon-naming-spec/latest/ar01s04.html or https://www.pythonguis.com/faq/built-in-qicons-pyqt/
.. pyqtdoc: https://www.riverbankcomputing.com/static/Docs/PyQt6/

***********
CutCutCodec
***********

.. image:: https://img.shields.io/badge/License-MIT-green.svg
    :target: https://opensource.org/licenses/MIT

.. image:: https://img.shields.io/badge/code_quality-pylint_10/10-green
    :target: https://github.com/pylint-dev/pylint

.. image:: https://img.shields.io/badge/tests-pass-green
    :target: https://docs.pytest.org/


Description
===========

This **video editing software** has a graphical interface powered by qtpy (run ``cutcutcodec-qt``).
It has been designed for speed and to implement some effects that are hard to find elsewhere.
The kernel is written in python and C, so it's easy to integrate it in your own project (module ``cutcutcodec.core``).
Although it allows you to fine-tune many parameters, it's smart enough to find the settings that are best suited to your project.

This software is **light**, **fast** and **highly configurable** for the following reasons:

#. Based on ffmpeg, this software supports an incredible number of formats and codecs.
#. This software allows editing the assembly graph. Compared to a timeline, this representation permits to do everything.
#. This software doesn't export the final video directly from the graphic interface. Instead, it generates a python script. You can edit this script yourself, giving you infinite possibilities!
#. A complete test benchmark guarantees an excelent kernel reliability.
#. Powered by `torch <https://pytorch.org/>`_, this software efficiently exploits the CPU and GPU in order to make it very fast.
#. Video export is performed without a graphical interface, releasing a large part of computer resources to speed up export.
#. This software is able to optimize the assembly graph in order to limit calculation waste.

.. image:: https://framagit.org/robinechuca/cutcutcodec/-/raw/main/doc/gui.png
    :alt: An example of the cutcutcodec GUI.


Features
========

Audio
-----

* General properties
    #. Supports a large number of channels (mono, stereo, 5.1, 7.1, ...) with all sampeling rate.
    #. Automatic detection of the optimal sample frequency.
* Generation
    #. White-noise generation.
    #. Generate any audio signal from any equation.
* Filters
    #. Cutting, translate and concatenate.
    #. Add multiple tracks.
    #. Arbitrary equation on several channels of several tracks. (dynamic volume, mixing, wouawoua, ...)
    #. Finite Impulse Response (FIR) invariant filter. (reverb, equalizer, echo, delay, volume, ...)

Video
-----

* General properties
    #. Unlimited support of all image resolutions. (FULL HD, 4K, 8K, ...)
    #. No limit on fps. (60fps, 120fps, ...)
    #. Automatic detection of the optimal resolution and fps.
    #. Support for the alpha transparency layer.
    #. Floating-point image calculation for greater accuracy.
* Generation
    #. White-noise generation.
    #. Generate any video signal from any equation.
    #. Mandelbrot fractal generation.
* Filters
    #. Cutting, translate and concatenate.
    #. Overlaying video tracks (with transparency control).
    #. Apply an arbitrary equation one several video streams.


Installation
============

Dependencies
------------

cutcutcodec has hard dependency on the ffmpeg package (version >= 4.0). You should install it first, please refer to the `FFmpeg download page <https://ffmpeg.org/download.html>`_.

In many cases, these commands should work:

.. code:: bash

    $ sudo apt install ffmpeg

Although it is installed automatically, it is better to install **av** manually to avoid redundancy with ffmpeg. Please refer to the `PyAv installation guide <https://pyav.org/docs/develop/overview/installation.html>`_.

If you have a GPU, please install CUDA or ROC then follow the `PyTorch installation guide <https://pytorch.org/>`_. Without CUDA or ROC, the software is not able to use the GPU (CPU only).


Installation of the lastest development version
-----------------------------------------------

To install cutcutcodec from `Framagit <https://framagit.org/robinechuca/cutcutcodec>`_ source, clone cutcutcodec using ``git`` and install it using ``pip``:

.. code:: bash

    git clone https://framagit.org/robinechuca/cutcutcodec.git
    cd cutcutcodec/
    pip install -e ./[optional]
    $SHELL
    cutcutcodec-test


Installation of the stable version
----------------------------------

To install cutcutcodec using `PyPI <https://pypi.org/project/cutcutcodec/>`_, just type this in a terminal:

.. code:: bash

    $ pip install cutcutcodec[gui]



Running
-------

In a terminal, just type ``cutcutcodec-qt`` to start the GUI and ``cutcutcodec-test`` for the test banchmark.


Example
=======

In this example we open a video file, add video noise, add audio A and C note, select the subclip between t=0s and t=10s, and write the result to a new file:

.. code:: python

    from cutcutcodec.core.filters.audio.subclip import FilterAudioSubclip
    from cutcutcodec.core.filters.video.add import FilterVideoAdd
    from cutcutcodec.core.filters.video.equation import FilterVideoEquation
    from cutcutcodec.core.filters.video.subclip import FilterVideoSubclip
    from cutcutcodec.core.generation.audio.equation import GeneratorAudioEquation
    from cutcutcodec.core.generation.video.noise import GeneratorVideoNoise
    from cutcutcodec.core.io.read_ffmpeg import ContainerInputFFMPEG
    from cutcutcodec.core.io.write import ContainerOutputFFMPEG

    with ContainerInputFFMPEG("cutcutcodec/examples/video.mp4") as container:
        (transparent,) = FilterVideoEquation(container.out_streams, "b0", "g0", "r0", "0.5").out_streams
        (noise,) = GeneratorVideoNoise().out_streams
        (video,) = FilterVideoAdd([transparent, noise]).out_streams
        (video_trunc,) = FilterVideoSubclip([video], 0, 10).out_streams
        (note_a,) = GeneratorAudioEquation("sin(2*pi*440*t)", "sin(2*pi*523.25*t)").out_streams
        (note_a_trunc,) = FilterAudioSubclip([note_a], 0, 10).out_streams
        ContainerOutputFFMPEG(
            [video_trunc, note_a_trunc],
            "final.mkv",
            [
                {"encodec": "libx264", "rate": 30, "shape": [720, 1080], "options": {"crf": "23"}},
                {"encodec": "libvorbis", "rate": 44100},
            ],
        ).write()


What's new ?
============

For the complete list of changes, refer to the `git commits <https://framagit.org/robinechuca/cutcutcodec/-/network/main?ref_type=heads>`_.
