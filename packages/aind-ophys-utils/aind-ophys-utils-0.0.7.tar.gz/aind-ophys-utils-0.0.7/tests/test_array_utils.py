"""Tests array_utils"""
import tempfile

import h5py
import numpy as np
import pytest

from aind_ophys_utils import array_utils as au


@pytest.mark.parametrize(
    "input_frame_rate, downsampled_frame_rate, expected",
    [
        (22.0, 50.0, 1),
        (100.0, 25.0, 4),
        (100.0, 7.0, 14),
        (100.0, 8.0, 12),
        (100.0, 7.9, 13),
    ],
)
def test_n_frames_from_hz(input_frame_rate, downsampled_frame_rate, expected):
    """Test n_frames_from_hz"""
    actual = au.n_frames_from_hz(input_frame_rate, downsampled_frame_rate)
    assert actual == expected


@pytest.mark.parametrize(
    ("array, input_fps, output_fps, random_seed, strategy, expected"),
    [
        (
            # random downsample 1D array
            np.array([1, 4, 6, 2, 3, 5, 11]),
            7,
            2,
            0,
            "random",
            np.array([2, 5]),
        ),
        (
            # random downsample ND array
            np.array(
                [[1, 3], [4, 4], [6, 8], [2, 1], [3, 2], [5, 8], [11, 12]]
            ),
            7,
            2,
            0,
            "random",
            np.array([[2, 1], [5, 8]]),
        ),
        (
            # first downsample 1D array
            np.array([1, 4, 6, 2, 3, 5, 11]),
            7,
            2,
            0,
            "first",
            np.array([1, 3]),
        ),
        (
            # random downsample ND array
            np.array(
                [[1, 3], [4, 4], [6, 8], [2, 1], [3, 2], [5, 8], [11, 12]]
            ),
            7,
            2,
            0,
            "first",
            np.array([[1, 3], [3, 2]]),
        ),
        (
            # last downsample 1D array
            np.array([1, 4, 6, 2, 3, 5, 11]),
            7,
            2,
            0,
            "last",
            np.array([2, 11]),
        ),
        (
            # last downsample ND array
            np.array(
                [[1, 3], [4, 4], [6, 8], [2, 1], [3, 2], [5, 8], [11, 12]]
            ),
            7,
            2,
            0,
            "last",
            np.array([[2, 1], [11, 12]]),
        ),
        (
            # average downsample 1D array
            np.array([1, 4, 6, 2, 3, 5, 11]),
            7,
            2,
            0,
            "average",
            np.array([13 / 4, 19 / 3]),
        ),
        (
            # average downsample ND array
            np.array(
                [[1, 3], [4, 4], [6, 8], [2, 1], [3, 2], [5, 8], [11, 12]]
            ),
            7,
            2,
            0,
            "average",
            np.array([[13 / 4, 4], [19 / 3, 22 / 3]]),
        ),
        (
            # average downsample ND array
            np.arange(200000).reshape(100, 2000),
            50,
            1,
            0,
            "average",
            np.array([np.arange(49000, 51000), np.arange(149000, 151000)]),
        ),
        (
            # average downsample ND array with only 1 output frame
            np.array([[1, 2], [3, 4], [5, 6]]),
            10,
            1,
            0,
            "average",
            np.array([[3.0, 4.0]]),
        ),
        (
            # maximum downsample 1D array
            np.array([1, 4, 6, 2, 3, 5, 11]),
            7,
            2,
            0,
            "maximum",
            np.array([6, 11]),
        ),
    ],
)
def test_downsample(
    array, input_fps, output_fps, random_seed, strategy, expected
):
    """Test downsample_array"""
    array_out = au.downsample_array(
        array=array,
        input_fps=input_fps,
        output_fps=output_fps,
        strategy=strategy,
        random_seed=random_seed,
    )
    assert np.array_equal(expected, array_out)


@pytest.mark.parametrize(("strategy, expected"),
                         [
    ("average",
     np.array([np.arange(49000, 51000), np.arange(149000, 151000)]),
     ),
    ("maximum",
     np.array([np.arange(98000, 100000), np.arange(198000, 200000)]),
     ),
],
)
def test_downsample_h5(strategy, expected):
    """Test downsample_array"""
    with tempfile.TemporaryDirectory() as tmpdirname:
        with h5py.File(tmpdirname + "/test_gzip.h5", "w") as f:
            f.create_dataset("data", data=np.arange(200000).reshape(100, 2000),
                             chunks=(1, 2000), compression="gzip")
            array = f["data"]
            array_out = au.downsample_array(
                array=array,
                input_fps=50,
                output_fps=1,
                strategy=strategy,
                random_seed=0,
            )
            assert np.array_equal(expected, array_out)
            if strategy == "average":
                f = au._mean_of_group
            else:
                f = au._max_of_group
            array_out = np.array(list(map(
                lambda i: f(i, array.file.filename, array.name, 50),
                range(0, 100, 50))))
            assert np.array_equal(expected, array_out)


@pytest.mark.parametrize(
    ("array, input_fps, output_fps, random_seed, strategy, expected"),
    [
        (
            # upsampling not defined
            np.array([1, 4, 6, 2, 3, 5, 11]),
            7,
            11,
            0,
            "maximum",
            np.array([6, 11]),
        ),
    ],
)
def test_downsample_exceptions(
    array, input_fps, output_fps, random_seed, strategy, expected
):
    """Test Exception raised by downsample_array"""
    with pytest.raises(ValueError):
        au.downsample_array(
            array=array,
            input_fps=input_fps,
            output_fps=output_fps,
            strategy=strategy,
            random_seed=random_seed,
        )


@pytest.mark.parametrize("input_fps", [3, 4, 5])
def test_decimate_video(input_fps):
    """
    This is another test of downsample array to make sure that
    it treats video-like arrays the way our median_filtered_max_projection
    code expects
    """
    rng = np.random.default_rng(62134)
    video = rng.random((71, 40, 40))

    expected = []
    for i0 in range(0, 71, input_fps):
        frame = np.mean(video[i0: i0 + input_fps], axis=0)
        expected.append(frame)
    expected = np.array(expected)

    actual = au.downsample_array(
        video, input_fps=input_fps, output_fps=1, strategy="average"
    )
    np.testing.assert_array_equal(expected, actual)


@pytest.mark.parametrize(
    "array, lower_cutoff, upper_cutoff, expected",
    [
        (
            np.array(
                [
                    [0.0, 100.0, 200.0],
                    [300.0, 400.0, 500.0],
                    [600.0, 700.0, 800.0],
                ]
            ),
            250,
            650,
            np.uint8([[0, 0, 0], [32, 96, 159], [223, 255, 255]]),
        )
    ],
)
def test_normalize_array(array, lower_cutoff, upper_cutoff, expected):
    """Test normalize_array"""
    normalized = au.normalize_array(
        array, lower_cutoff=lower_cutoff, upper_cutoff=upper_cutoff
    )
    np.testing.assert_array_equal(normalized, expected)
    assert normalized.dtype == np.uint8


@pytest.mark.parametrize(
    "input_array, expected_array",
    [
        (
            np.array([0, 1, 2, 3, 4, 5]).astype(int),
            np.array([0, 51, 102, 153, 204, 255]).astype(np.uint8),
        ),
        (
            np.array([-1, 0, 1, 2, 4]).astype(int),
            np.array([0, 51, 102, 153, 255]).astype(np.uint8),
        ),
        (
            np.array([-1.0, 1.5, 2, 3, 4]).astype(float),
            np.array([0, 128, 153, 204, 255]).astype(np.uint8),
        ),
    ],
)
def test_scale_to_uint8(input_array, expected_array):
    """
    Test normalize_array when cutoffs are not specified
    """
    actual = au.normalize_array(input_array)
    np.testing.assert_array_equal(actual, expected_array)
    assert actual.dtype == np.uint8


@pytest.mark.parametrize(
    "input_array, lower, upper, input_dtype, expected",
    [
        (
            np.array([22, 33, 44, 11, 39]),
            12.0,
            40.0,
            np.uint16,
            np.array([23405, 49151, 65535, 0, 63194]),
        ),
        (
            np.array([22, 33, 44, 11, 39]),
            12.0,
            40.0,
            np.int16,
            np.array([-9363, 16383, 32767, -32768, 30426]),
        ),
        (
            np.array([22, 33, 44, 11, 39]),
            None,
            40.0,
            np.int16,
            np.array([-7910, 16948, 32767, -32768, 30507]),
        ),
        (
            np.array([22, 33, 44, 11, 39]),
            12.0,
            None,
            np.int16,
            np.array([-12288, 10239, 32767, -32768, 22527]),
        ),
        (
            np.array([2, 11, 32, 78, 99]),
            20.0,
            61.0,
            np.uint32,
            np.array([0, 0, 1257063599, 4294967295, 4294967295]),
        ),
        (
            np.array([2, 11, 32, 78, 99]),
            10.0,
            None,
            np.uint32,
            np.array([0, 48258059, 1061677309, 3281548046, 4294967295]),
        ),
        (
            np.array([2, 11, 32, 78, 99]),
            None,
            61.0,
            np.uint32,
            np.array([0, 655164503, 2183881675, 4294967295, 4294967295]),
        ),
        (
            np.array([2, 11, 32, 78, 99]),
            20.0,
            61.0,
            np.int32,
            np.array(
                [-2147483648, -2147483648, -890420049, 2147483647, 2147483647]
            ),
        ),
        (
            np.array([2, 11, 32, 78, 99]),
            10.0,
            None,
            np.int32,
            np.array(
                [-2147483648, -2099225589, -1085806339, 1134064398, 2147483647]
            ),
        ),
        (
            np.array([2, 11, 32, 78, 99]),
            None,
            61.0,
            np.int32,
            np.array(
                [-2147483648, -1492319145, 36398027, 2147483647, 2147483647]
            ),
        ),
    ],
)
def test_scale_to_other_types(
    input_array, lower, upper, input_dtype, expected
):
    """
    Test that normalize_array works for datatypes other than np.uint8
    """
    actual = au.normalize_array(
        array=input_array,
        lower_cutoff=lower,
        upper_cutoff=upper,
        dtype=input_dtype,
    )
    np.testing.assert_array_equal(actual, expected)
    assert actual.dtype == input_dtype
