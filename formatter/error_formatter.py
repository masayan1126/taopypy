import dataclasses
import sys
import traceback


@dataclasses.dataclass
class ErrorFormatter:
    def format(self, ex: Exception):
        ex_type, ex_value, ex_traceback = sys.exc_info()

        # Extract unformatter stack traces as tuples
        trace_back = traceback.extract_tb(ex_traceback)

        # Format stacktrace
        stack_trace = list()

        for trace in trace_back:
            stack_trace.append(
                "File : %s , Line : %d, Func.Name : %s, Message : %s"
                % (trace[0], trace[1], trace[2], trace[3])
            )

        return {
            "type": ex_type.__name__,
            "message": ex_value,
            "stack_trace": stack_trace,
        }
