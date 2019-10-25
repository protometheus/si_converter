#!/usr/bin/python3

class Conversion:
	def __init__(self, conversion_value, base_unit):
		self.conversion_value = conversion_value
		self.base_unit = base_unit


""" 
	Base units 
"""
SECOND = "s"
RADIAN = "rad"
METER_SQUARED = "m^2"
METER_CUBED = "m^3"
KILOGRAM = "kg"

""" 
	NAMES_TO_SYMBOLS is a mapping between 

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
def get_conversion(name_or_symbol):
	symbol = NAMES_TO_SYMBOLS.get(name_or_symbol.lower(), name_or_symbol)
	return SYMBOLS_TO_VALUES.get(symbol)