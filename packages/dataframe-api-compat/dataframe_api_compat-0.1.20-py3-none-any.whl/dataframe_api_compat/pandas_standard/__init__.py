from __future__ import annotations

import re
from typing import Any
from typing import TYPE_CHECKING

import pandas as pd

from dataframe_api_compat.pandas_standard.pandas_standard import LATEST_API_VERSION
from dataframe_api_compat.pandas_standard.pandas_standard import null
from dataframe_api_compat.pandas_standard.pandas_standard import PandasColumn
from dataframe_api_compat.pandas_standard.pandas_standard import PandasDataFrame
from dataframe_api_compat.pandas_standard.pandas_standard import PandasGroupBy

if TYPE_CHECKING:
    from collections.abc import Sequence
    from dataframe_api._types import DType


Column = PandasColumn
DataFrame = PandasDataFrame
GroupBy = PandasGroupBy


class Int64:
    ...


class Int32:
    ...


class Int16:
    ...


class Int8:
    ...


class UInt64:
    ...


class UInt32:
    ...


class UInt16:
    ...


class UInt8:
    ...


class Float64:
    ...


class Float32:
    ...


class Bool:
    ...


class String:
    ...


class Date:
    ...


class Datetime:
    def __init__(self, time_unit, time_zone=None):
        self.time_unit = time_unit
        # todo validate time zone
        self.time_zone = time_zone


class Duration:
    def __init__(self, time_unit):
        self.time_unit = time_unit


def map_pandas_dtype_to_standard_dtype(dtype: Any) -> DType:
    if dtype == "int64":
        return Int64()
    if dtype == "Int64":
        return Int64()
    if dtype == "int32":
        return Int32()
    if dtype == "Int32":
        return Int32()
    if dtype == "int16":
        return Int16()
    if dtype == "Int16":
        return Int16()
    if dtype == "int8":
        return Int8()
    if dtype == "Int8":
        return Int8()
    if dtype == "uint64":
        return UInt64()
    if dtype == "UInt64":
        return UInt64()
    if dtype == "uint32":
        return UInt32()
    if dtype == "UInt32":
        return UInt32()
    if dtype == "uint16":
        return UInt16()
    if dtype == "UInt16":
        return UInt16()
    if dtype == "uint8":
        return UInt8()
    if dtype == "UInt8":
        return UInt8()
    if dtype == "float64":
        return Float64()
    if dtype == "Float64":
        return Float64()
    if dtype == "float32":
        return Float32()
    if dtype == "Float32":
        return Float32()
    if dtype == "bool":
        # 'boolean' not yet covered, as the default dtype in pandas is still 'bool'
        return Bool()
    if dtype == "object":
        return String()
    if dtype == "string":
        return String()
    if dtype == "datetime64[s]":
        return Date()
    if dtype.startswith("datetime64["):
        time_unit = re.search(r"datetime64\[(\w{1,2})", dtype).group(1)
        return Datetime(time_unit)
    if dtype.startswith("timedelta64["):
        time_unit = re.search(r"timedelta64\[(\w{1,2})", dtype).group(1)
        return Duration(time_unit)
    raise AssertionError(f"Unsupported dtype! {dtype}")


def map_standard_dtype_to_pandas_dtype(dtype: DType) -> Any:
    if isinstance(dtype, Int64):
        return "int64"
    if isinstance(dtype, Int32):
        return "int32"
    if isinstance(dtype, Int16):
        return "int16"
    if isinstance(dtype, Int8):
        return "int8"
    if isinstance(dtype, UInt64):
        return "uint64"
    if isinstance(dtype, UInt32):
        return "uint32"
    if isinstance(dtype, UInt16):
        return "uint16"
    if isinstance(dtype, UInt8):
        return "uint8"
    if isinstance(dtype, Float64):
        return "float64"
    if isinstance(dtype, Float32):
        return "float32"
    if isinstance(dtype, Bool):
        return "bool"
    if isinstance(dtype, String):
        return "object"
    if isinstance(dtype, Datetime):
        if dtype.time_zone is not None:  # pragma: no cover (todo)
            return f"datetime64[{dtype.time_unit}, {dtype.time_zone}]"
        return f"datetime64[{dtype.time_unit}]"
    if isinstance(dtype, Duration):
        return f"timedelta64[{dtype.time_unit}]"
    raise AssertionError(f"Unknown dtype: {dtype}")


def convert_to_standard_compliant_column(
    ser: pd.Series, api_version: str | None = None
) -> PandasDataFrame:
    if api_version is None:  # pragma: no cover
        api_version = LATEST_API_VERSION
    if ser.name is not None and not isinstance(ser.name, str):
        raise ValueError(f"Expected column with string name, got: {ser.name}")
    if ser.name is None:
        ser = ser.rename("")
    df = ser.to_frame().__dataframe_consortium_standard__().collect()
    return PandasColumn(df.col(ser.name).column, api_version=api_version, df=df)


def convert_to_standard_compliant_dataframe(
    df: pd.DataFrame, api_version: str | None = None
) -> PandasDataFrame:
    if api_version is None:
        api_version = LATEST_API_VERSION
    return PandasDataFrame(df, api_version=api_version)


def concat(dataframes: Sequence[PandasDataFrame]) -> PandasDataFrame:
    dtypes = dataframes[0].dataframe.dtypes
    dfs = []
    api_versions = set()
    for _df in dataframes:
        try:
            pd.testing.assert_series_equal(_df.dataframe.dtypes, dtypes)
        except Exception as exc:
            raise ValueError("Expected matching columns") from exc
        else:
            dfs.append(_df.dataframe)
        api_versions.add(_df._api_version)
    if len(api_versions) > 1:  # pragma: no cover
        raise ValueError(f"Multiple api versions found: {api_versions}")
    return PandasDataFrame(
        pd.concat(
            dfs,
            axis=0,
            ignore_index=True,
        ),
        api_version=api_versions.pop(),
    )


def dataframe_from_columns(*columns: PandasColumn) -> PandasDataFrame:
    data = {}
    api_version = set()
    for col in columns:
        col._df._validate_is_collected("dataframe_from_columns")
        data[col.name] = col.column
        api_version.add(col._api_version)
    return PandasDataFrame(pd.DataFrame(data), list(api_version)[0])


def column_from_1d_array(
    data: Any, *, dtype: Any, name: str | None = None
) -> PandasColumn[Any]:  # pragma: no cover
    ser = pd.Series(data, dtype=map_standard_dtype_to_pandas_dtype(dtype), name=name)
    df = ser.to_frame().__dataframe_consortium_standard__().collect()
    # todo: propagate api version
    return PandasColumn(df.col(name).column, api_version=LATEST_API_VERSION, df=df)


def column_from_sequence(
    sequence: Sequence[Any], *, dtype: Any, name: str, api_version: str | None = None
) -> PandasColumn[Any]:
    ser = pd.Series(sequence, dtype=map_standard_dtype_to_pandas_dtype(dtype), name=name)
    df = ser.to_frame().__dataframe_consortium_standard__().collect()
    # todo: propagate api version
    return PandasColumn(df.col(name).column, api_version=LATEST_API_VERSION, df=df)


def dataframe_from_2d_array(
    data: Any,
    *,
    names: Sequence[str],
    dtypes: dict[str, Any],
    api_version: str | None = None,
) -> PandasDataFrame:  # pragma: no cover
    df = pd.DataFrame(data, columns=names).astype(  # type: ignore[call-overload]
        {key: map_standard_dtype_to_pandas_dtype(value) for key, value in dtypes.items()}
    )
    return PandasDataFrame(df, api_version=api_version or LATEST_API_VERSION)


def is_null(value: Any) -> bool:
    return value is null


def is_dtype(dtype: Any, kind: str | tuple[str, ...]) -> bool:
    if isinstance(kind, str):
        kind = (kind,)
    dtypes: set[Any] = set()
    for _kind in kind:
        if _kind == "bool":
            dtypes.add(Bool)
        if _kind == "signed integer" or _kind == "integral" or _kind == "numeric":
            dtypes |= {Int64, Int32, Int16, Int8}
        if _kind == "unsigned integer" or _kind == "integral" or _kind == "numeric":
            dtypes |= {UInt64, UInt32, UInt16, UInt8}
        if _kind == "floating" or _kind == "numeric":
            dtypes |= {Float64, Float32}
        if _kind == "string":
            dtypes.add(String)
    return isinstance(dtype, tuple(dtypes))
