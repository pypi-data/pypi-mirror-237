from enum import Enum

from tecton_core import conf
from tecton_core.query.sql_compat import Dialect
from tecton_proto.common import compute_mode_pb2


class ComputeMode(str, Enum):
    """Represents the compute mode for training data generation queries."""

    SPARK = "spark"
    SNOWFLAKE = "snowflake"
    ATHENA = "athena"
    DUCK_DB = "duckdb"


def get_compute_mode() -> ComputeMode:
    """Returns the default ComputeMode based on the environment."""

    compute_mode = conf.get_or_raise("TECTON_COMPUTE_MODE")
    if compute_mode == ComputeMode.DUCK_DB:
        return ComputeMode.DUCK_DB
    elif conf.get_bool("ALPHA_SNOWFLAKE_COMPUTE_ENABLED") or compute_mode == ComputeMode.SNOWFLAKE:
        return ComputeMode.SNOWFLAKE
    elif conf.get_bool("ALPHA_ATHENA_COMPUTE_ENABLED") or compute_mode == ComputeMode.ATHENA:
        return ComputeMode.ATHENA
    elif compute_mode == ComputeMode.SPARK:
        return ComputeMode.SPARK
    else:
        msg = f"Invalid Tecton compute mode: {compute_mode}. Must be one of {[[e.value for e in ComputeMode]]}"
        raise ValueError(msg)


class BatchComputeMode(Enum):
    """Represents that compute mode for batch jobs associated with a FeatureView."""

    SPARK = compute_mode_pb2.ComputeMode.COMPUTE_MODE_SPARK
    SNOWFLAKE = compute_mode_pb2.ComputeMode.COMPUTE_MODE_SNOWFLAKE
    TECTON = compute_mode_pb2.ComputeMode.COMPUTE_MODE_TECTON

    @classmethod
    def from_string(cls, string: str) -> "BatchComputeMode":
        modes = {
            "spark": BatchComputeMode.SPARK,
            "snowflake": BatchComputeMode.SNOWFLAKE,
            "tecton": BatchComputeMode.TECTON,
        }
        if string in modes:
            return modes[string]
        else:
            choices = ", ".join(modes.keys().map(repr))
            msg = f"Invalid BatchComputeMode {repr(string)}. Must be one of: ${choices}."
            raise ValueError(msg)


def default_dialect():
    # TODO: Make this based only on TECTON_COMPUTE_MODE and on function-level overrides
    d = conf.get_or_none("SQL_DIALECT")
    try:
        return Dialect(d)
    except Exception:
        msg = f"Unsupported sql dialect: set SQL_DIALECT to {[x.value for x in Dialect]}"
        raise Exception(msg)
