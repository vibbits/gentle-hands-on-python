from evaluation_utils import EvaluationResult
from datetime import datetime


def evaluate_test(context, the_input):
    expected = {
        "Time": datetime.strptime(the_input["Time"]),
        "Temperature": float(the_input["Anomaly (deg C)"]),
    }
    return EvaluationResult(
        result=expected == context.actual,
        dsl_expected=repr(expected),
        dsl_actual=repr(context.actual),
        messages=[],
    )
