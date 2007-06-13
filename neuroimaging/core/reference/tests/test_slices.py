from numpy.testing import NumpyTest, NumpyTestCase

from neuroimaging.core.reference.slices import bounding_box, \
  zslice, yslice, xslice
from neuroimaging.core.reference.grid import SamplingGrid

class test_Slice(NumpyTestCase):

    def test_bounding_box(self):
        shape = (10, 10, 10)
        grid = SamplingGrid.identity(shape)
        self.assertEqual(bounding_box(grid), [[0., 9.], [0, 9], [0, 9]])

    def test_box_slice(self):
        zslice(5, [0, 9], [0, 9], [0, 9], (10, 10, 10)).mapping.transform
        yslice(5, [0, 9], [0, 9], [0, 9], (10, 10, 10)).mapping.transform
        xslice(5, [0, 9], [0, 9], [0, 9], (10, 10, 10)).mapping.transform

from neuroimaging.utils.testutils import make_doctest_suite
test_suite = make_doctest_suite('neuroimaging.core.reference.slices')        

if __name__ == '__main__':
    NumpyTest.run()