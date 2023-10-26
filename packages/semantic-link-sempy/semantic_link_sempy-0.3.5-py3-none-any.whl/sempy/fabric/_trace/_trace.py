import pandas as pd
import uuid

from typing import Dict, List, Optional, Callable


class Trace():
    """
    Trace object for collecting diagnostic and performance related information from the Microsoft Analysis Services Tabular server.

    Python wrapper around `Microsoft Analysis Services Trace
    <https://learn.microsoft.com/en-us/analysis-services/trace-events/analysis-services-trace-events?view=asallproducts-allversions>`_.

    Parameters
    ----------
    server : Microsoft Analysis Services Tabular Server
        Server object to add trace to.
    event_schema : dict
        Dictionary containing event types as keys and list of column names for that event as values.
        Both event and column names must be specified as strings, without spaces and in PascalCase.
    name : str
        Name identifying trace. If None, the trace name will be "SemanticLinkTrace_<GUID>".
    """
    def __init__(self, server, event_schema: Dict[str, List[str]], name: Optional[str] = None):
        from Microsoft.Fabric.SemanticLink import TraceCollector

        if name is not None and not isinstance(name, str):
            raise TypeError(f"Unexpected type {type(name)} for \"name\" element: not a str")
        if name is None:
            name = f"SemanticLinkTrace_{str(uuid.uuid4())}"

        self.trace_collector = TraceCollector(server, name)
        self.add_events(event_schema)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.drop()

    @property
    def is_started(self) -> bool:
        """
        Whether or not this trace is currently started.
        """
        return self.trace_collector.IsStarted()

    @property
    def name(self) -> str:
        """
        Name of the trace.
        """
        return self.trace_collector.GetName()

    def add_events(self, event_schema: Dict[str, List[str]]) -> None:
        """
        Add events and their corresponding columns to the trace.

        The trace must be stopped in order to add events.

        Parameters
        ----------
        event_schema : dict
            Dictionary containing event types as keys and list of column names for that event as values.
            Both event and column names must be specified as strings, without spaces and in PascalCase.
        """
        from System import ArgumentException

        if self.is_started:
            raise RuntimeError("Cannot add events to trace when trace is started. Stop the trace to add new events.")

        for event_type, columns in event_schema.items():
            if not isinstance(event_type, str):
                raise TypeError(f"Unexpected type {type(event_type)} for \"event_type\" element: not a str")
            if not isinstance(columns, list):
                raise TypeError(f"Unexpected type {type(columns)} for \"columns\" element: not a list")
            for col in columns:
                if not isinstance(col, str):
                    raise TypeError(f"Unexpected type {type(col)} for \"column\" element: not a str")
            if len(columns) == 0:
                raise ValueError(f"Event '{event_type}' must have at least one column specified.")

            try:
                self.trace_collector.AddEvent(event_type, columns)
            except ArgumentException as e:
                raise ValueError(f"{e.Message}\nMake sure that event and column names do not contain spaces and are in PascalCase.")

    def start(self) -> None:
        """
        Start the trace.
        """
        self.trace_collector.Start()

    def stop(self) -> pd.DataFrame:
        """
        Stop the trace and retrieve the trace logs.

        Returns
        -------
        pd.DataFrame
            DataFrame where every row is data from the events added to the trace.
        """
        self.trace_collector.Stop()
        return self.get_trace_logs()

    def get_trace_logs(self) -> pd.DataFrame:
        """
        Retrieve the trace logs as a DataFrame.

        This can be executed while the trace is still running.

        Returns
        -------
        pd.DataFrame
            DataFrame where every row is data from the events added to the trace.
        """
        trace_logs = self.trace_collector.GetTraceLogs()
        return pd.DataFrame(trace_logs)

    def drop(self) -> None:
        """
        Remove the current trace from its parent Server connection.
        """
        self.trace_collector.Drop()

    def add_event_handler(self, on_event_func: Callable) -> None:
        """
        Add a custom handler for trace events.

        Parameters
        ----------
        on_event_func : Callable
            Function to execute on every event.
        """
        from Microsoft.AnalysisServices.Tabular import TraceEventHandler

        trace = self.trace_collector.GetTrace()
        trace.OnEvent += TraceEventHandler(on_event_func)
