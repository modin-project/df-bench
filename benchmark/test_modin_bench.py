from .base_bench import _BenchmarkLib
import modin.pandas


class TestBenchmarkModin(_BenchmarkLib):
    _lib = modin.pandas
