from importlib.resources import files

def greet(name: str) -> str:
    """Return a friendly greeting using a template stored as data."""
    # Locate the data file included in the package
    data_dir = files("toy_lib").joinpath("data")
    template = (data_dir / "greeting.txt").read_text(encoding="utf-8").strip()
    return template.format(name=name)
