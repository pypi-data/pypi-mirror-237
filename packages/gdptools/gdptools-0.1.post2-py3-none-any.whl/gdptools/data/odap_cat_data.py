"""OpenDAP Catalog Data classes."""
from __future__ import annotations

from typing import Any
from typing import Optional
from typing import Tuple

import pandas as pd
from pydantic import BaseModel
from pydantic import Field
from pydantic import field_validator
from pydantic import ValidationInfo


class CatParams(BaseModel):
    """Class representing elements of Mike Johnsons OpenDAP catalog params.

    https://mikejohnson51.github.io/opendap.catalog/cat_params.json
    """

    id: Optional[str] = None
    URL: str
    grid_id: Optional[int] = Field(default_factory=lambda: -1)
    variable: Optional[str] = None
    varname: str
    long_name: Optional[str] = None
    T_name: Optional[str] = None
    duration: Optional[str] = None
    units: Optional[str] = None
    interval: Optional[str] = None
    nT: Optional[int] = Field(default_factory=lambda: 0)  # noqa
    tiled: Optional[str] = None
    model: Optional[str] = None
    ensemble: Optional[str] = None
    scenario: Optional[str] = None

    @field_validator("*", mode="before")
    @classmethod
    def handle_nan(cls, value: Any, info: ValidationInfo):
        """Handle nans."""
        if pd.isnull(value):
            if info.field_name in [
                "id",
                "variable",
                "long_name",
                "T_name",
                "units",
                "interval",
                "tiled",
                "model",
                "ensemble",
                "scenario",
            ]:
                return "None"
            elif info.field_name in ["grid_id", "nt"]:
                return -1
        elif info.field_name == "grid_id":
            return int(value)
        else:
            return value


class CatGrids(BaseModel):
    """Class representing elements of Mike Johnsons OpenDAP catalog grids.

    https://mikejohnson51.github.io/opendap.catalog/cat_grids.json
    """

    grid_id: Optional[int] = None
    X_name: str
    Y_name: str
    X1: Optional[float] = None
    Xn: Optional[float] = None
    Y1: Optional[float] = None
    Yn: Optional[float] = None
    resX: Optional[float] = None  # noqa
    resY: Optional[float] = None  # noqa
    ncols: Optional[int] = None
    nrows: Optional[int] = None
    proj: str
    toptobottom: int
    tile: Optional[str] = None
    grid_id_1: Optional[str] = Field(None, alias="grid.id")

    @field_validator("tile", "grid_id_1", mode="before")
    @classmethod
    def handle_nan(cls, value: Any, info: ValidationInfo):
        """Handl nans."""
        if pd.isnull(value):
            if info.field_name == "tile":
                return "None"
            elif info.field_name == "grid_id_1":
                return "None"
        else:
            return value

    @field_validator("toptobottom", mode="before", check_fields=True)
    @classmethod
    def get_toptobottom(cls, v: int) -> int:  # noqa:
        """Convert str to int."""
        return int(v)

    @field_validator("proj", mode="before")
    @classmethod
    def convert_int_to_string(cls, value):
        """Convert ints to string."""
        if isinstance(value, int):
            return str(value)
        return value


class CatClimRItem(BaseModel):
    """Mike Johnson's CatClimRItem class.

    Source data from which this is derived comes from:
        'https://mikejohnson51.github.io/climateR-catalogs/catalog.json'
    """

    id: str
    asset: Optional[str] = None
    URL: str
    varname: str
    variable: Optional[str] = None
    description: Optional[str] = None
    units: Optional[str] = None
    model: Optional[str] = None
    ensemble: Optional[str] = None
    scenario: Optional[str] = None
    T_name: Optional[str] = None
    duration: Optional[str] = None
    interval: Optional[str] = None
    nT: Optional[int] = 0  # noqa
    X_name: str  # noqa
    Y_name: str  # noqa
    X1: float
    Xn: float
    Y1: float
    Yn: float
    resX: float  # noqa
    resY: float  # noqa
    ncols: int
    nrows: int
    crs: str
    toptobottom: bool
    tiled: Optional[str] = None

    @field_validator("crs")
    @classmethod
    def _default_crs(cls, val: str) -> str:
        """Sets to a default CRS if none is provided."""
        if val is None or not val:
            return "EPSG:4326"
        return val

    # @field_validator("toptobottom", check_fields=False)
    # @classmethod
    # def _toptobottom_as_bool(cls, val: str) -> bool:
    #     """Convert to python boolean type."""
    #     return val.upper() == "TRUE"  # type: ignore

    @field_validator("tiled", check_fields=False)
    @classmethod
    def _tiled(cls, val: str) -> str:
        """Must be one of just a few options.  Returns NA if left blank."""
        if val.upper() not in ["", "NA", "T", "XY"]:
            raise ValueError("tiled must be one of ['', 'NA', 'T', 'XY']")
        if val == "":
            return "NA"
        return val.upper()

    class Config:
        """interior class to direct pydantic's behavior."""

        anystr_strip_whitespace = True
        allow_mutations = False


def climr_to_odap(climr: CatClimRItem) -> Tuple[CatParams, CatGrids]:
    """Convert a CatClimRItem to a CatParams and CatGrids object.

    Parameters
    ----------
    climr : CatClimRItem
        The CatClimRItem object to convert.

    Returns
    -------
    CatParams, CatGrids
        The CatParams and CatGrids objects.

    """
    params = CatParams(
        id=climr.id,
        URL=climr.URL,
        grid_id=0,
        variable=climr.variable,
        varname=climr.varname,
        long_name=climr.description,
        T_name=climr.T_name,
        duration=climr.duration,
        units=climr.units,
        interval=climr.interval,
        nT=climr.nT,
        tiled=climr.tiled,
        model=climr.model,
        ensemble=climr.ensemble,
        scenario=climr.scenario,
    )
    grids = CatGrids(
        X_name=climr.X_name,
        Y_name=climr.Y_name,
        X1=climr.X1,
        Xn=climr.Xn,
        Y1=climr.Y1,
        Yn=climr.Yn,
        resX=climr.resX,
        resY=climr.resY,
        ncols=climr.ncols,
        nrows=climr.nrows,
        proj=climr.crs,
        toptobottom=climr.toptobottom,
        tile=climr.tiled,
    )
    return params, grids
