from typing_extensions import Any, Collection, Never


class Universe(set):
    def __contains__(self, item):
        return True


def item(x: Collection) -> Any:
    if len(x) != 1:
        raise ValueError(
            f"Expected a collection of length 1, instead {x} has length {len(x)}"
        )
    return next(iter(x))


def never() -> Never:
    breakpoint()
    raise ValueError("Reached unreachable code.")


def recursive_getattr(obj: Any, name: str) -> Any:
    names = name.split(".")
    for name in names:
        obj = getattr(obj, name)
    return obj


def recursive_setattr(obj: Any, name: str, value: Any) -> None:
    names = name.split(".")
    for name in names[:-1]:
        obj = getattr(obj, name)
    setattr(obj, names[-1], value)
