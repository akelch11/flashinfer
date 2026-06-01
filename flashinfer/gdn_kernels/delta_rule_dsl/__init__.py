try:
    from .delta_rule_sm90 import delta_rule_prefill_dsl_sm90

    _has_sm90_delta_rule_dsl = True
except (ImportError, RuntimeError):
    delta_rule_prefill_dsl_sm90 = None  # type: ignore
    _has_sm90_delta_rule_dsl = False

try:
    from .delta_rule_sm120 import delta_rule_prefill_dsl as delta_rule_prefill_dsl_sm120

    _has_sm120_delta_rule_dsl = True
except (ImportError, RuntimeError):
    delta_rule_prefill_dsl_sm120 = None  # type: ignore
    _has_sm120_delta_rule_dsl = False

try:
    from .delta_rule_cp_sm90 import cp_delta_rule_dsl_sm90

    _has_cp_delta_rule_sm90 = True
except (ImportError, RuntimeError):
    cp_delta_rule_dsl_sm90 = None  # type: ignore
    _has_cp_delta_rule_sm90 = False


__all__ = [
    "delta_rule_prefill_dsl_sm90",
    "delta_rule_prefill_dsl_sm120",
    "cp_delta_rule_dsl_sm90",
    "_has_sm90_delta_rule_dsl",
    "_has_sm120_delta_rule_dsl",
    "_has_cp_delta_rule_sm90",
]
