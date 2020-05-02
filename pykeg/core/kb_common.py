"""System constants and defaults."""

# FT330-RJ default.
DEFAULT_TICKS_PER_ML = 2.724

# Minimum session size, in milliliters, to display
MIN_SESSION_VOLUME_DISPLAY_ML = 177  # 6 ounces

# Maximum time between consecutive drinks to be considered in the same 'session'
# (see UserDrinkingSession table)
DRINK_SESSION_TIME_MINUTES = 3 * 60

# Minimum and maximum thermo sensor readings (degrees C).
THERMO_SENSOR_RANGE = (-20.0, 80.0)

# Maximum number of readings to keep.
THERMO_SENSOR_HISTORY_MINUTES = 60 * 24

# Device names
AUTH_MODULE_CORE_ONEWIRE = "core.onewire"
AUTH_MODULE_CORE_RFID = "core.rfid"
AUTH_MODULE_CONTRIB_PHIDGET_RFID = AUTH_MODULE_CORE_RFID

# Auth modules whose token values should be interpreted as lower-case hex.
AUTH_MODULE_NAMES_HEX_VALUES = (AUTH_MODULE_CORE_ONEWIRE, AUTH_MODULE_CORE_RFID)

# Low volume threshold: 15% full
KEG_VOLUME_LOW_PERCENT = 0.15

# Valid usernames.
USERNAME_REGEX = "^[\w.@+-]+$"
