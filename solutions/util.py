from os import path


def getFnIn(args):
    """Check if input filepath in args, if it exists and return filepath."""
    if len(args) != 1:
        raise ValueError("Path to input should be provided as the first and only argument.")
    if not path.exists(args[0]):
        raise ValueError(f"File ({args[0]}) does not exist.")
    return args[0]