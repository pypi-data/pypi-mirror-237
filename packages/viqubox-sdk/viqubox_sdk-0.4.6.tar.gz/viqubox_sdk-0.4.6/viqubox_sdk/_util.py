import json
import mimetypes
import os.path as path
from typing import Any, Dict, List, Tuple


def write_to_file(location: str, data: str, mode: str = "w") -> str:
    with open(location, mode) as f:
        f.write(data)
    return location


def write_dict_to_file(location: str, data: Dict[str, Any], mode: str = "w") -> str:
    with open(location, mode) as f:
        f.write(json.dumps(data, indent=4))
    return path.abspath(location)


def read_file(file: str) -> str:
    """Read file and split data in lines."""
    if path.exists(file):  # noqa
        with open(file) as f:
            return f.read()
    else:
        return ""


def is_audio_file(file: str) -> bool:
    """Check if the given file is an audio file.

    :param file: _description_
    :return: _description_
    """
    ftype = mimetypes.guess_type(file)[0]
    if not ftype:
        return False
    elif "audio" in ftype:
        return True
    return False


def prepare_audio_pairs(
    audio_pairs: List[Tuple[str, str]], ignore_missing: bool = False
) -> Tuple[dict, list]:
    """Prepare and validate input audio files to send to API audio processing.
    Check if files are audio type and exist on system.

    :param audio_pairs: Local system paths leading to files in format List[Tuple(reference: str, degraded: str)]
    :param ignore_missing: Continue flow if some paths are not found on local system, defaults to False
    :raises Exception: Invalid audio file pair.
    :raises Exception: Audio files not found on system.
    :return: (API input files, Mapping of local input files and API input files)
    """
    input_files = {}
    translate = []
    for i, pair in enumerate(audio_pairs):
        ref = pair[0]
        degr = pair[1]
        if not all([is_audio_file(f) for f in pair]) and not len(pair) == 2:
            raise Exception(f"Invalid audio file pair: {pair}")
        if not all([path.exists(f) for f in pair]):
            if not ignore_missing:
                raise Exception(f"Audio files not found on system: {pair}")
            print(f"Files not found on system, ignoring them: {pair}")
            continue
        refname = f"SMPL{i}.wav"
        degrname = f"degr_SMPL{i}.wav"
        input_files[f"a{i}"] = (refname, open(ref, "rb"), mimetypes.guess_type(ref))
        input_files[f"b{i}"] = (degrname, open(degr, "rb"), mimetypes.guess_type(ref))
        translate.extend([(ref, refname), (degr, degrname)])
    return (input_files, translate)
