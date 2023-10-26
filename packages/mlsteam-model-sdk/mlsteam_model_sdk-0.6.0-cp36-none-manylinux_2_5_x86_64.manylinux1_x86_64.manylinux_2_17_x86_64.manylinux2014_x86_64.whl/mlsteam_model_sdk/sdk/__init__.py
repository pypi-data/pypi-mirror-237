import contextlib
import functools
import sqlite3

import psutil
from mlsteam_model_sdk.utils.db import connect_db


@functools.lru_cache(maxsize=32)
def __ps_exists(pid: int, p_create_time: str) -> bool:
    return psutil.pid_exists(pid) and str(int(psutil.Process(pid).create_time())) == p_create_time


def __cleanup_residual_model_files():
    from mlsteam_model_sdk.sdk.model import MVPackage

    with contextlib.suppress(Exception):
        conn = connect_db()
        conn.row_factory = sqlite3.Row
        live_model_versions = conn.execute('SELECT id, pid, p_create_time FROM lmvs').fetchall()

        for lmv in live_model_versions:
            with contextlib.suppress(Exception):
                if not __ps_exists(lmv['pid'], lmv['p_create_time']):
                    MVPackage._cleanup_lmv(conn, lmv_id=lmv['id'], db_only=False)


__cleanup_residual_model_files()
