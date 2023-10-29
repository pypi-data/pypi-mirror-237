"""
    Events
"""
from enum import Enum
from typing import Callable, Any

class EventName(Enum):
    TEST_STARTED = 1,
    PROD_STARTED = 2

_event_handler_registry:dict[EventName,list[Callable]] = dict()

def register(eventname:EventName, handler:Callable[[EventName,str,Any],None]):
    if eventname in _event_handler_registry.keys():
        raise KeyError(f'Event {eventname} already registered')
    _event_handler_registry[eventname] = (handler,)

def deregister(handler:Callable[[EventName,str,Any],None], eventname:EventName):
    handlers = _event_handler_registry[eventname]
    if handler in handlers: handlers.remove(handler)

def publish(eventname:EventName, source:str, data:Any):
    handlers = _event_handler_registry.get(eventname)
    if handlers is not None and len(handlers) > 0:
        for handler in handlers: handler(eventname, source, data)
    