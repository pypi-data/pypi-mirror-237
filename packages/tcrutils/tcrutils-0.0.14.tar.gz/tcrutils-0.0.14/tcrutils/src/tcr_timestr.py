import datetime
import re as regex
from collections.abc import Iterable, Mapping

from .tcr_console import console
from .tcr_extract_error import extract_error

timestr_lookup = {
    's':       (second := 1),
    'sec':     second,
    'secs':    second,
    'sex':     second, # >:3
    'second':  second,
    'seconds': second,

    'm':       (minute := 60*second),
    'min':     minute,
    'mins':    minute,
    'minute':  minute,
    'minutes': minute,

    'h':     (hour := 60*minute),
    'hr':    hour,
    'hrs':   hour,
    'hour':  hour,
    'hours': hour,

    'd':    (day := 24*hour),
    'day':  day,
    'days': day,

    'w':     (week := 7*day),
    'week':  week,
    'weeks': week,

    'y':     (year := 365*day),
    'year':  year,
    'years': year,

    'pul':   (pul := (11*hour + 30*minute)),
    'pull':  pul,
    'puls':  pul,
    'pulls': pul,
    'card':  pul,
    'cards': pul,

    'res':     (rescue := 6*hour),
    'reses':   rescue,
    'resees':  rescue,
    'rescue':  rescue,
    'rescues': rescue,

    'rev':         (revolution := 133*day), # 1 revolution = 133 days, nice if you get the reference hihi :>
    'revs':        revolution,
    'revolution':  revolution,
    'revolutions': revolution,
  }

def split_string_at_indices(s: str, indices: Iterable[int]) -> tuple[str]:
  substrings = []
  start = 0
  for index in indices:
    if index >= start and index <= len(s):
      substrings.append(s[start:index])
      start = index
    else:
      msg = f"Invalid split index: {index}"
      raise ValueError(msg)
  if start < len(s):
    substrings.append(s[start:])
  return tuple(substrings)

def split_string_on_change(s: str) -> tuple[tuple[str]]:
  splits = []
  for i in range(len(s)-1): # Not using enumerate because i also need the next letter
    if not s[i].isnumeric() and s[i+1].isnumeric(): # If there happens to be a NON-numer on the left and a number on the right...
      splits.append(i+1) # ...place a split point there

  return [_split_string_on_change2(x) for x in split_string_at_indices(s, splits)]

def _split_string_on_change2(s: str) -> tuple[str]:
  splits = []
  for i in range(len(s)-1): # Not using enumerate because i also need the next letter
    if s[i].isnumeric() and not s[i+1].isnumeric(): # If there happens to be a NON-numer on the left and a number on the right...
      splits.append(i+1) # ...place a split point there

  return split_string_at_indices(s, splits)

def seconds_until_time(target_time):
  # Get the current time
  current_time = datetime.datetime.now()

  # Create a datetime object for the target time
  target_datetime = datetime.datetime(  # noqa: DTZ001
    current_time.year, current_time.month, current_time.day,
    target_time[0], target_time[1], target_time[2],
  )

  # Calculate the time difference in seconds
  time_difference = target_datetime - datetime.datetime.now()
  seconds_until_target = time_difference.total_seconds()

  # Ensure the result is positive and represents the time until the next occurrence
  if seconds_until_target < 0:
    seconds_until_target += 24 * 3600  # Add 24 hours in seconds to get the next occurrence

  return int(seconds_until_target)

def is_valid_date(date_tuple: tuple[int, int, int]) -> bool:
  try:
    datetime.date(date_tuple[2], date_tuple[1], date_tuple[0])
  except ValueError:
    return False
  else:
    return True

def days_until_due(due_date):
  current_datetime = datetime.datetime.now().date()
  due_datetime = datetime.date(due_date[2], due_date[1], due_date[0])
  delta = due_datetime - current_datetime
  return delta.days

def evaluate_single_timestr(s: str, *, units: Mapping[str, int]) -> int:
  if not s: return 0

  if regex.match(r'^[0-9]{1,2}:(?:[0-9]{1,2}(?::[0-9]{1,2})?)?$', s):
    s = s
    s = s.split(':')
    s = [x for x in s if x != '']
    s = (lambda x, y=0, z=0: (int(x), int(y), int(z)))(*s)
    if not (0 <= s[0] <= 23):
      msg = f'Time out of range: {s}'
      raise ValueError(msg)
    if not (0 <= s[1] <= 59):
      msg = f'Time out of range: {s}'
      raise ValueError(msg)
    if not (0 <= s[2] <= 59):
      msg = f'Time out of range: {s}'
      raise ValueError(msg)
    return seconds_until_time(s) + 1 # +1 as a correction because it for some reason returned 1 second too little
  if regex.match(r'^[0-9]{1,2}\.(?:[0-9]{1,2}(?:\.[0-9]{2,4})?)?$', s):
    s = s
    s = s.split('.')
    s = [x for x in s if x != '']
    s = (lambda x, y=-1, z=-1: [int(x), int(y), int(z)])(*s)
    now = datetime.datetime.now()
    if s[0] > now.day:
      if s[2] == -1:
        year_manually_passed_in = False
        s[2] = now.year
      else:
        year_manually_passed_in = True
      if s[1] == -1:
        s[1] = now.month
        month_manually_passed_in = False
      else:
        month_manually_passed_in = True
    else: # chosen day is in the past or today
      if s[2] == -1:
        year_manually_passed_in = False
        s[2] = now.year
      else:
        year_manually_passed_in = True
      if s[1] == -1:
        month_manually_passed_in = False
        s[1] = now.month + 1
        if s[1] > 12:
          s[1] = 1
          s[2] = s[2] + 1
      else: # The month was also passed in
        month_manually_passed_in = True
    if not year_manually_passed_in and month_manually_passed_in and s[1] <= now.month:
      s[2] = s[2] + 1
    if s[2] < 1000: s[2] = s[2] + 2000 # 23 -> 2023
    # print(s)
    if not is_valid_date(s):
      msg = f'Invalid date: {s}'
      raise ValueError(msg)
    return days_until_due(s) * 60*60*24 #. *seconds_in_a_day
  else:  # noqa: RET505
    if regex.match(r'^[0-9]+h[0-9]+$', s):
      s = f'{s}m'
    splits = split_string_on_change(s)
    try:
      return sum(int(pair[0]) * units[pair[1]] for pair in splits)
    except KeyError as e:
      raise ValueError('Invalid unit: ' + extract_error(e, raw=True)[1]) from e



class timestr:
  pattern =  \
r"""
^
(?:(?:[0-9]+[a-zA-Z]+)+)|(?:[0-9]+h[0-9]+)
|
(?:[0-9]{1,2}:(?:[0-9]{1,2}(?::[0-9]{1,2})?)?)
|
(?:[0-9]{1,2}\.(?:[0-9]{1,2}(?:\.[0-9]{2,4})?)?)
$
""".replace('\n', '')

  @staticmethod
  def to_int(s: str, units: Mapping[str, int] | None = None, *, segment_splitter='!') -> int:
    """Returns the number of seconds in that timestr"""
    if not s: return 0

    while (segment_splitter + segment_splitter) in s:
      s = s.replace(segment_splitter + segment_splitter, segment_splitter)

    SYNTAX_REGEX = timestr.pattern

    if units is None: units = timestr_lookup

    segments = s.split(segment_splitter)

    if not all(a := [bool(x) for x in [regex.match(SYNTAX_REGEX, x) for x in segments]]):
      msg = f'Invalid timestr: {s!r} ({a})'
      raise ValueError(msg)

    return sum([evaluate_single_timestr(x, units=units) for x in segments])


  @staticmethod
  def to_str(n: int) -> str:
    """Returns nicely formatted time from number of seconds provided"""
    units = [
      ("day", 86400),
      ("hour", 3600),
      ("minute", 60),
      ("second",  1),
    ]

    for unit, value_in_seconds in units:
      if n >= value_in_seconds:
          num_units = n / value_in_seconds
          if num_units == round(num_units): num_units = round(num_units)
          num_units = round(num_units, 2)
          unit_str = unit if num_units == 1 else unit + 's'
          return f"{num_units} {unit_str}"

    # If seconds is 0, return "in 0 seconds"
    return "0 seconds"

