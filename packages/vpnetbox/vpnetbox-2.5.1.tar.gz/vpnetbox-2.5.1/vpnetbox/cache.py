"""Read/write NbData RseData from/to pickle, remove/restore recursions in Net objects."""

from __future__ import annotations

import logging
import os
import pickle
import re
from pathlib import Path
from typing import Any

from vpnetbox.types_ import DAny, LStr


class Cache:
    """Read/write NbData RseData from/to pickle, remove/restore recursions in Net objects."""

    _methods_w_data = [
        "aggregate",
        "prefix",
        "address",
        "ip",
        "super",
        "sub",
        "check",
    ]

    def __init__(self, cache_path: str = "", **kwargs):
        """Init Cache.

        :param cache_path: Path to the pickle file.
        :param kwargs: Optional parameters.
            cache_attrs: Attributed to be cached.
            By default, CACHED_ATTRS used in NbData, RseHandler.
        """
        self.name: str = self.__class__.__name__
        self.cache_path: Path = Path(cache_path) or Path(f"{self.name}.pickle")
        self._cache_attrs: LStr = kwargs.get("cache_attrs") or []

    def __repr__(self) -> str:
        """__repr__."""
        name = self.__class__.__name__
        return f"<{name}: {self.cache_path.name}>"

    # =========================== method =============================

    def is_cache(self) -> bool:
        """Check if a pickle file is present on disk.

        :return: True if the pickle file is present, False otherwise.
        """
        return self.cache_path.is_file()

    def read_cache(self) -> None:
        """Read cached data from a pickle file and restore recursions in Net objects.

        :return: None. Update self object.
        """
        self._read_cache()
        self._restore_recursions()
        self._logging_debug__loaded()

    def write_cache(self) -> None:
        """Write cache to a pickle file and remove recursions in Net objects.

        :return: None. Update a pickle file.
        """
        self._check_cached_attrs()
        data: DAny = self._data_for_cache()
        self._remove_recursions()
        self._write_cache(data)
        self._restore_recursions()
        self._logging_debug__saved()

    # ====================== helpers ======================

    def _check_cached_attrs(self) -> None:
        """Check the attributes of the data to ensure it is ready for caching.

        If the data is invalid, raise an ERROR.
        :return: None. Check the attributes of the data.
        :raise: KeyError if invalid attributes are found.
        """
        reserved = {"__tear__"}
        if invalid_attributes := set(self._cache_attrs).intersection(reserved):
            raise KeyError(f"{invalid_attributes=}, {reserved=}")

    def _create_dir(self) -> None:
        """Create directory for cache."""
        if not self.cache_path:
            return
        path = Path(self.cache_path)
        root = path.resolve().parent
        if not root.is_dir():
            root.mkdir(parents=True, exist_ok=True)

    def _create_file(self, data) -> None:
        """Create pickl file for cache with write permissions 666."""
        os.umask(0)
        descriptor = os.open(
            path=str(self.cache_path),
            flags=(os.O_WRONLY | os.O_CREAT | os.O_TRUNC),
            mode=0o666
        )
        with open(descriptor, "wb") as fh:
            pickle.dump(data, fh)

    def _data_for_cache(self) -> DAny:
        """Return data to be cached without RseData."""
        data: DAny = {}
        for attr in self._cache_attrs:
            data[attr] = getattr(self, attr)
        return data

    def _get_rsehs(self) -> list:
        """Return self RseHandler objects, ready for recursions remove/restore."""
        rsehs = []  # RseHandlers
        obj_name = self.__class__.__name__
        if obj_name == "RseHandler":
            rsehs.append(self)
        for attr in dir(self):
            if not attr.startswith("_"):
                obj = getattr(self, attr)
                obj_name = obj.__class__.__name__
                if obj_name == "RseHandler":
                    rsehs.append(obj)
        return rsehs

    def _remove_recursions(self) -> None:
        """Remove recursion in RseData object."""
        rsehs = self._get_rsehs()
        for rseh in rsehs:
            if rsed := getattr(rseh, "data"):
                rsed.remove_recursions()

    def _restore_recursions(self) -> None:
        """Restore recursion in RseData object."""
        rsehs = self._get_rsehs()
        for rseh in rsehs:
            if rsed := getattr(rseh, "data"):
                rsed.restore_recursions()
                for rse_o_name in self._methods_w_data:
                    rse_o = getattr(rseh, rse_o_name)
                    rse_o.nbd = rsed

    def _read_cache(self):
        """Read cached data from a pickle file."""
        try:
            with self.cache_path.open(mode="rb") as fh:
                data: DAny = pickle.load(fh)
                for attr, value in data.items():
                    if attr in self._cache_attrs:
                        setattr(self, attr, value)
        except FileNotFoundError as ex:
            if hasattr(ex, "args") and isinstance(ex.args, tuple):
                msgs = [s for s in ex.args if isinstance(s, str)]
                for attr in ["filename", "filename2"]:
                    if hasattr(ex, attr):
                        if value := getattr(ex, attr):
                            msgs.append(f"{ex.filename}")
                msg = "To create *.pickle file need to execute vpnetbox without --cache parameter."
                msgs.append(msg)
                msg = ". ".join(msgs)
                raise FileNotFoundError(msg)
            raise FileNotFoundError(*ex.args)

    def _write_cache(self, data) -> None:
        """Write cache to pickle file."""
        try:
            self._create_dir()
            self._create_file(data)
        except PermissionError as ex:
            self._error__cmd_chmod(ex)
            raise type(ex)(*ex.args)

    # =========================== logging ============================

    def _error__cmd_chmod(self, ex: Any) -> None:
        """Log ERROR, with example how to solve problem: chmod {path}."""
        error = f"{type(ex).__name__}: {ex}"
        path = (re.findall(r"(\'.+\')$", str(ex)) or [str(self.cache_path)])[0]
        cmd = f"\"sudo chmod o+rw {path}\""
        msg = f"{error}. Please change permissions by command: {cmd} and try again."
        logging.error(msg)

    def _logging_debug__loaded(self) -> None:
        """Log DEBUG cache loaded."""
        path = str(self.cache_path)
        msg = f"cache loaded from {path=}"
        logging.debug(msg)

    def _logging_debug__saved(self) -> None:
        """Log DEBUG cache saved."""
        path = str(self.cache_path)
        msg = f"cache saved to {path=}"
        logging.debug(msg)


def make_path(**kwargs) -> str:
    """Make path to pickle file.

    :param kwargs: Parameters to make path to picked file.
        name: Parent object name.
        host: Netbox host name.
        var: Pat to var directory.
    :return: Path to pickle file.
    """
    var = str(kwargs.get("var") or "")
    if var.endswith(".pickle"):
        return var
    name = str(kwargs.get("name") or "Cache")
    host = str(kwargs.get("host") or "")
    items = [name, host, "pickle"]
    items = [s for s in items if s]
    name = ".".join(items)
    path = str(Path(var, name))
    return path
