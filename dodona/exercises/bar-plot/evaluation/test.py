from evaluation_utils import EvaluationResult, ConvertedOracleContext
from matplotlib.testing.compare import compare_images

def evaluate_test(context: ConvertedOracleContext):
    context.actual.savefig("actual.png")
    result = compare_images("actual.png", "expected.png")
    return EvaluationResult(
        result=result is None,
        readable_expected="",
        readable_actual="",
        messages=[result] if result is not None else [],
    )
