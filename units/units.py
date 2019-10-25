#!/usr/bin/python3

# Conversion is a convenience class that holds the values needed 
# to convert a unit. For more, see #SYMBOLS_TO_VALUES
class Conversion:
	def __init__(self, conversion_value, base_unit):
		self.conversion_value = conversion_value
		self.base_unit = base_unit


# NON_UNIT_CHARS are all characters allowed in a given input 
# that are not explicitly unit values
NON_UNIT_CHARS = "()/*"

""" 
	Base units 
"""
SECOND = "s"
RADIAN = "rad"
METER_SQUARED = "m^2"
METER_CUBED = "m^3"
KILOGRAM = "kg"

""" 
	NAMES_TO_SYMBOLS is a mapping between the long-form name of a unit
	and its corresponding symbol. This is used because the input of units may
	either be a symbol or a name

"""
NAMES_TO_SYMBOLS = {
	"second": "s",
	"minute": "min",
	"hour": "h",
	"day": "d",
	"degree": "°",
	"arcminute": "'",
	"arcsecond": "\"",
	"hectare": "ha",
	"litre": "L",
	"tonne": "t"
}

"""
	SYMBOLS_TO_VALUES is a mapping between a symbol and the conversion between it
	and its base unit. The Conversion it is mapped to has 2 values:
		- conversion_value: str -- 	represents the number of base_unit required
									to convert between the key and the base_unit
		- base_unit: str -- represents the base unit symbol the key must be converted into
"""
SYMBOLS_TO_VALUES = {
	"s": Conversion("1", SECOND),
	"min": Conversion("60", SECOND),
	"h": Conversion("3600", SECOND),
	"d": Conversion("86400", SECOND),
	"rad": Conversion("1", RADIAN),
	"°": Conversion("pi/180", RADIAN),
	"'": Conversion("pi/10800", RADIAN),
	"\"": Conversion("pi/648000", RADIAN),
	"ha": Conversion("10000", METER_SQUARED),
	"L": Conversion(".001", METER_CUBED),
	"t": Conversion("1000", KILOGRAM),

}

# get_symbol returns the Conversion for the given input. The input may 
# be either a symbol itself or the name of the symbol. If no symbol 
# is found, this returns None.
def get_conversion_factor(name_or_symbol):
	symbol = NAMES_TO_SYMBOLS.get(name_or_symbol.lower(), name_or_symbol)
	return SYMBOLS_TO_VALUES.get(symbol)