"""Init helpers."""

from packaging.version import Version


def name(**kwargs) -> str:
    """Init name for *RseVlanGroup*."""
    name_ = kwargs.get("name")
    if name_ is None:
        name_ = ""
    if not isinstance(name_, str):
        raise TypeError(f"{name_=}, {str} expected")
    return name_


def role(**kwargs) -> str:
    """Init role for *Net*."""
    role_ = kwargs.get("role")
    if role_ is None:
        role_ = ""
    if not isinstance(role_, str):
        raise TypeError(f"{role_=}, {str} expected")
    return role_


def site(**kwargs) -> str:
    """Init site for *Net*."""
    site_ = kwargs.get("site")
    if site_ is None:
        site_ = ""
    if not isinstance(site_, str):
        raise TypeError(f"{site_=}, {str} expected")
    return site_


def ipam(**kwargs) -> str:
    """Init ipam for *Net*: "aggregate", "prefix", "address"."""
    ipam_ = kwargs.get("ipam")
    if ipam_ is None:
        if snet_ := kwargs.get("snet"):
            items = snet_.split("/")
            if len(items) == 1:
                return "address"
            if len(items) == 2 and items[1] == "32":
                return "address"
        return "prefix"
    if not isinstance(ipam_, str):
        raise TypeError(f"{ipam_=}, {str} expected")
    expected = ["aggregate", "prefix", "address"]
    if ipam_ not in expected:
        raise TypeError(f"invalid {ipam_=}, {expected=}")
    return ipam_


def repr_params(*args, **kwargs) -> str:
    """Make params for __repr__() method."""
    args_ = ", ".join([f"{v!r}" for v in args if v])
    kwargs_ = ", ".join([f"{k}={v!r}" for k, v in kwargs.items() if v])
    params = [s for s in (args_, kwargs_) if s]
    return ", ".join(params)


def version(**kwargs) -> Version:
    """Init Netbox version for *Net*."""
    version_ = kwargs.get("version")
    if version_ is None:
        version_ = Version("0")
    if isinstance(version_, Version):
        return version_
    if isinstance(version_, str):
        return Version(version_)
    raise TypeError(f"{version_=}, {Version} expected")
