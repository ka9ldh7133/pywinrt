import timeit

COUNT = 100_000
REPEAT = 10

times = timeit.repeat(
    "unbox(box(test))",
    setup="""
from uuid import uuid4
from winrt.windows.foundation.interop import box, unbox

test = uuid4()
""",
    number=COUNT,
    repeat=REPEAT,
)

print(f"{int(min(times) / COUNT * 1e9):_} ns per iteration average")