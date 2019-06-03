import pytest

test_files = ["f.csv"]


class _BenchmarkLib(object):
    @pytest.mark.parametrize("file", test_files)
    def test_read_csv(self, benchmark, file):
        def compute():
            df = self._lib.read_csv(file)
            # Force computation if it's not forced
            df.head()
            df.tail()

        benchmark(compute)
