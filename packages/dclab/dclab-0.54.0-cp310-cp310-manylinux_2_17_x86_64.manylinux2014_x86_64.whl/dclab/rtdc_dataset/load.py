"""Load RT-DC datasets"""
import errno
import io
import os
import pathlib

from .core import RTDCBase
from . import fmt_s3, fmt_dict, fmt_dcor, fmt_hdf5, fmt_tdms, fmt_hierarchy


def load_file(path, identifier=None, **kwargs):
    path = pathlib.Path(path).resolve()
    for fmt in [fmt_hdf5.RTDC_HDF5, fmt_tdms.RTDC_TDMS]:
        if fmt.can_open(path):
            return fmt(path, identifier=identifier, **kwargs)
    else:
        raise ValueError("Unknown file format: '{}'".format(path.suffix))


def new_dataset(data, identifier=None, **kwargs):
    """Initialize a new RT-DC dataset

    Parameters
    ----------
    data:
        can be one of the following:

        - dict
        - .tdms file
        - .rtdc file
        - subclass of `RTDCBase`
          (will create a hierarchy child)
        - DCOR resource URL
        - URL to file in S3-compatible object store
    identifier: str
        A unique identifier for this dataset. If set to `None`
        an identifier is generated.
    kwargs: dict
        Additional parameters passed to the RTDCBase subclass

    Returns
    -------
    dataset: subclass of :class:`dclab.rtdc_dataset.RTDCBase`
        A new dataset instance
    """
    if isinstance(data, dict):
        return fmt_dict.RTDC_Dict(data, identifier=identifier, **kwargs)
    elif isinstance(data, io.BytesIO):
        return fmt_hdf5.RTDC_HDF5(data, **kwargs)
    elif fmt_dcor.is_dcor_url(data):
        return fmt_dcor.RTDC_DCOR(data, identifier=identifier, **kwargs)
    elif fmt_s3.is_s3_url(data):
        return fmt_s3.RTDC_S3(data, identifier=identifier, **kwargs)
    elif isinstance(data, RTDCBase):
        return fmt_hierarchy.RTDC_Hierarchy(data, identifier=identifier,
                                            **kwargs)
    elif isinstance(data, (pathlib.Path, str)):
        path = pathlib.Path(data).resolve()
        if not path.exists():
            raise FileNotFoundError(
                errno.ENOENT, os.strerror(errno.ENOENT), str(path))
        else:
            return load_file(data, identifier=identifier, **kwargs)
    else:
        msg = "data type not supported: {}".format(data.__class__)
        raise NotImplementedError(msg)
