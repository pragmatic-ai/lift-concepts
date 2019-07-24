from typing import TypeVar, Optional
from dataclasses import dataclass
from pragma_universe.thing import Thing

FloatOrInt = TypeVar('NullableValue', float, int, None)

@dataclass
class Number(Thing):
    value: FloatOrInt = None # is ether a float or an int or None
    is_ordinal: Optional[bool] = None  # if is an ordinal number
    is_cardinal: Optional[bool] = None  # if is a cardinal number
    is_a_pure_number: Optional[bool] = None # if is one or π (Pi) or e (Euler's Number)
    is_pi: Optional[bool] = None
    is_euler_number: Optional[bool] = None
    is_avogadro: Optional[bool] = None
    represented_as_binary: Optional[bool] = None  # represented as a boolean number
    represented_as_hexadecimal: Optional[bool] = None  # represented as a hex number

@dataclass
class Interval(Thing):
    from_value: FloatOrInt = None
    to_value: FloatOrInt = None
    start_is_inclusive: Optional[bool] = True  # default
    end_is_inclusive: Optional[bool] = False  # default
    is_discrete: Optional[bool] = None
    step_size: FloatOrInt = None # if the interval is descret, we define an step size

@dataclass
class Ratio(Thing):
    value: TypeVar('NullableValue', float, None) = None   # is ether a float or an int or None
    first_term: TypeVar('NullableValue', float, None) = None  # nominator
    second_term: TypeVar('NullableValue', float, None) = None  # denominator
    is_percentage: Optional[bool] = None
    is_phi: Optional[bool] = False  # golden ratio
