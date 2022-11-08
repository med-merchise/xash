"""Data driver to manage spreadsheets."""

import io

import pandas as pd

WorksheetFile = pd.ExcelFile
FILE = str | io.IOBase
SHEET_FILE = FILE | WorksheetFile
SHEET_RESULT = pd.DataFrame | dict[int | str, pd.DataFrame]


def _update_argument(target: dict[str, object], name: str, value: object):
    """Update argument for Panda's `read_excel` method (internal function)."""
    if name not in target:
        target[name] = value
    else:
        raise TypeError(
            f"pandas.read_excel() got multiple values for argument '{name}'"
        )


def parse_worksheet_region(region: str | None, target: dict[str, object]):
    """Parse region updating arguments for Panda's `read_excel` method.

    See `read_worksheet_data`:func: for more information.

    """
    import re

    if region:
        region = region.replace('$', '')
        if '.' in region:
            sheet_name, region = region.split('.')
            _update_argument(target, 'sheet_name', sheet_name.strip('"\''))
        col1, row1, col2, row2 = (
            item
            for cell in region.split(':')
            for item in re.match('^([A-Z]+)([0-9]+)$', cell).groups()
        )
        row1, row2 = int(row1), int(row2)
        _update_argument(target, 'usecols', ':'.join((col1, col2)))
        _update_argument(target, 'skiprows', row1 - 1)
        _update_argument(target, 'nrows', row2 - row1)
    target.setdefault('index_col', 0)
    return target


def read_worksheet_data(
    io: SHEET_FILE, region: str = None, **kwargs
) -> SHEET_RESULT:
    """Return a Pandas data-frame reading from a worksheet file.

    The same Panda's `read_excel` method arguments can be specified.  A string
    with the format `[<SHEET-NAME>.]<START-CELL>:<END-CELL>` can be optionally
    specified to parse the 'sheet_name', 'usecols', 'skiprows', and 'nrows'
    arguments.  In this case the 'index_col' argument defaults to `0`.

    """
    data = pd.read_excel(io, **parse_worksheet_region(region, kwargs))
    data.rename(index=str, columns=str, inplace=True)
    data.fillna(0, inplace=True)
    return data


def read_csv_data(io: FILE, **kwargs) -> SHEET_RESULT:
    """Return a Pandas data-frame reading from a CSV file.

    The same Panda's `read_csv` method arguments can be specified.  In this
    case the 'index_col' argument defaults to `0`.

    """
    kwargs.setdefault('index_col', 0)
    return pd.read_csv(io, **kwargs)
