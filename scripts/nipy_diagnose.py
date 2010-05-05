#!/usr/bin/env python
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
DESCRIP = 'Calculate and write results for diagnostic screen'
EPILOG = \
'''nipy_diagnose will generate a series of diagnostic images for a 4D
fMRI image volume.  The following images will be generated.  <ext> is
the input filename extension (e.g. '.nii'):

    * components_<label>.png : plots of PCA basis vectors
    * max_<label><ext> : max image
    * mean_<label><ext> : mean image
    * min_<label><ext> : min image
    * pca_<label><ext> : 4D image of PCA component images
    * pcnt_var_<label>.png : percent variance scree plot for PCA
      components
    * std_<label><ext> : standard deviation image
    * tsdiff_<label>.png : time series diagnostic plot

The filenames for the outputs are of the form
<out-path>/<some_prefix><label><file-ext> where <out-path> is the path
specified by the --out-path option, or the path of the input filename;
<some_prefix> are the standard prefixes above, <label> is given by
--out-label, or by the filename of the input image (with path and
extension removed), and <file-ext> is '.png' for graphics, or the
extension of the input filename for volume images.  For example,
specifying only the input filename ``/some/path/fname.img`` will
generate filenames of the form ``/some/path/components_fname.png,
/some/path/max_fname.img`` etc.
'''

import os

import numpy as np

import nipy
from nipy.externals.argparse import ArgumentParser, \
    RawDescriptionHelpFormatter
import nipy.algorithms.diagnostics.screens as nads
from nipy.io.imageformats.filename_parser import splitext_addext

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    parser = ArgumentParser(description=DESCRIP,
                            epilog=EPILOG,
                            formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('filename', type=str,
                        help='4D image filename')
    parser.add_argument('--out-path', type=str,
                        help='path for output image files')
    parser.add_argument('--out-fname-label', type=str,
                        help='mid part of output image filenames')
    parser.add_argument('--ncomponents', type=int, default=10,
                        help='number of PCA components to write')
    # parse the command line
    args = parser.parse_args()
    # process inputs
    filename = args.filename
    out_path = args.out_path
    out_root = args.out_fname_label
    ncomps = args.ncomponents
    # collect extension for output images
    froot, ext, gz = splitext_addext(filename)
    pth, fname = os.path.split(froot)
    if out_path is None:
        out_path = pth
    if out_root is None:
        out_root = fname
    img = nipy.load_image(filename)
    res = nads.screen(img, ncomps)
    nads.write_screen_res(res, out_path, out_root, ext + gz)
    

if __name__ == '__main__':
    main()
