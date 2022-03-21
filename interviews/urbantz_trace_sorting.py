from typing import List, Dict

from functools import cmp_to_key


def sort_traces(traces: List[Dict[str, str]]) -> List[Dict[str, str]]:
    traces.sort(key=cmp_to_key(comp_traces))
    return traces


def comp_traces(t1, t2) -> int:
    if t1["id"] > t2["id"]:
        return 1
    elif t1["id"] == t2["id"]:
        return 1 if t1["date_time"] < t2["date_time"] else -1
    return -1


if __name__ == "__main__":
    traces = sort_traces([
        {
            "id": "4jSlWKrFJSPTN",
            "machine": "work02",
            "date_time": "2021-04-03 23:22:11.033",
            "path": "/path/to/file:line",
            "message": "this is message",
        },
        {
            "id": "NjLVI43iizTLF", "machine": "web01",
            "date_time": "2021-04-03 23:22:11.290",
            "path": "/path/to/file:line",
            "message": "this is message",
        },
        {
            "id": "75nERrSwifJKL", "machine": "work02",
            "date_time": "2021-04-03 23:22:11.021",
            "path": "/path/to/file:line",
            "message": "this is message",
        },
        {
            "id": "4jSlWKrFJSPTN", "machine": "web01",
            "date_time": "2021-04-03 23:22:14.544",
            "path": "/path/to/file:line",
            "message": "this is message",
        },
    ])
    for trace in traces:
        print(trace)


