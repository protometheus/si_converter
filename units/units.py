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
METER_CUBED = "m^3"

""" 
	names_to_symbols is a mapping between 

"""
names_to_symbols = {
	"second": "s",
	"minute": "min",
	"hour": "h",
	"day": "d",
	"litre": "L",
	"degree": "°",
}

symbols_to_values = {
	"s": Conversion("1", SECOND),
	"min": Conversion("60", SECOND),
	"h": Conversion("3600", SECOND),
	"d": Conversion("86400", SECOND),
	"L": Conversion(".001", METER_CUBED),
	"rad": Conversion("1", RADIAN),
	"°": Conversion("pi/180", RADIAN),
	"arcminute": Conversion("pi/10800", RADIAN),
	"arcsecond": Conversion("pi/648000", RADIAN),
}

# get_symbol returns the Conversion for the given input. The input may 
# be either a symbol itself or the name of the symbol. If no symbol 
# is found, this returns None.
def get_conversion(name_or_symbol):
	symbol = names_to_symbols.get(name_or_symbol.lower(), name_or_symbol)
	return symbols_to_values.get(symbol)