import time

# from pyopyo3_runtime
import pytest
from py_rust import PySerial, PanicException


def current_milli_time() -> int:
    return round(time.time() * 1000)


def test_connecting_failed() -> None:
    with pytest.raises(PanicException):
        serial = PySerial(460800, "/dev/dontexist")


# @pytest.mark.skip
def test_reading():
    serial = PySerial(460800, "/dev/ttyS0")
    while True:
        buffer = serial.read_line()

        # print(buffer)

        timestamp = current_milli_time()
        data = "".join(buffer).replace(" ", "")

        print(f"{timestamp} -> {data}")
