"""Date-time stamped names for the files handed to people.

Robot archives, the open-items Excel and the PDF report carry the date and
time they were generated, local time of central Mexico, as YYYY-MM-DD_HHMM:

    658424_R10_2026-10-04_1600.zip
    R10_Puntos_Abiertos_2026-10-04_1600.xlsx
    R10_reporte_2026-10-04_1600.pdf

A generator writing to its default place (dist/) removes the older stamped
copies of the same file there, so dist/ always holds the latest one; git
keeps the history.
"""
import datetime
import glob
import os
import re
from zoneinfo import ZoneInfo

TZ = 'America/Mexico_City'


def now():
    return datetime.datetime.now(ZoneInfo(TZ))


def stamp(t=None):
    return (t or now()).strftime('%Y-%m-%d_%H%M')


def human(t=None):
    """'2026-10-04 08:15 (hora del centro de México)', for covers and sheets."""
    return (t or now()).strftime('%Y-%m-%d %H:%M') + ' (hora del centro de México)'


def dated_path(directory, prefix, ext, t=None):
    return os.path.join(directory, f'{prefix}_{stamp(t)}{ext}')


def remove_older(path, prefix, ext):
    """Delete the other copies of `prefix` in the directory of `path`: stamped
    ones (prefix_YYYY-MM-DD_HHMM.ext) and the old undated prefix.ext."""
    directory = os.path.dirname(os.path.abspath(path))
    pat = re.compile(re.escape(prefix) + r'(_\d{4}-\d{2}-\d{2}_\d{4})?' + re.escape(ext) + '$')
    removed = []
    for other in glob.glob(os.path.join(directory, prefix + '*' + ext)):
        if pat.match(os.path.basename(other)) and not os.path.samefile(other, path):
            os.remove(other)
            removed.append(other)
    return removed
