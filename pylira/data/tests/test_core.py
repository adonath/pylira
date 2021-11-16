from numpy.testing import assert_allclose
from pylira.data import (
    point_source_gauss_psf,
    disk_source_gauss_psf,
    gauss_and_point_sources_gauss_psf
)


def test_data_point_source_gauss_psf():
    data = point_source_gauss_psf()

    assert_allclose(data["counts"][0][0], 2)
    assert_allclose(data["exposure"][0][0], 1)
    assert_allclose(data["background"][0][0], 2.)
    assert_allclose(data["psf"][0][0], 1.44298e-05, rtol=1e-5)
    assert_allclose(data["flux"][16][16], 1000, rtol=1e-5)


def test_data_disk_source_gauss_psf():
    data = disk_source_gauss_psf()

    assert_allclose(data["counts"][0][0], 1)
    assert_allclose(data["exposure"][0][0], 0.5)
    assert_allclose(data["background"][0][0], 2.)
    assert_allclose(data["psf"][0][0], 1.44298e-05, rtol=1e-5)
    assert_allclose(data["flux"][16][16], 35.367765, rtol=1e-5)


def test_data_gauss_and_point_sources_gauss_psf():
    data = gauss_and_point_sources_gauss_psf()

    assert_allclose(data["counts"][0][0], 1)
    assert_allclose(data["exposure"][0][0], 0.5)
    assert_allclose(data["background"][0][0], 2.)
    assert_allclose(data["psf"][0][0], 4.477632e-09, rtol=1e-5)
    assert_allclose(data["flux"][16][16], 36.664897, rtol=1e-5)
