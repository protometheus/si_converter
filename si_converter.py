#!/usr/bin/python3
from decimal import *
from math import pi
from enum import Enum
from units import *
from flask import Flask, request
# from '../units.py' import *

app = Flask(__name__)


PRECISION_MULT = '1.00000000000000'
NON_UNIT_CHARS = "()/*"

def get_rsp(output, output_factor, err):
	return {
		"unit_name": output,
		"multiplicative_factor": output_factor,
		"error": err,
	}

@app.route("/units/si")
def get_conversion_factor() -> str:
	inp = request.args.get('units')

	if len(inp) == 0:
		return inp

	# remove extra whitespace by splitting and rejoining
	inp = "".join(inp.split())
	print(f"input: {inp}")

	# for each character, check if it is an open parantheses
	# if it's not, exchange its name for its symbol
	output = ""
	output_factor = ""
	err = ""
	i = 0
	while i < len(inp):
		# if we found a non_unit character, just copy it over
		if inp[i] in NON_UNIT_CHARS:
			output += inp[i]
			output_factor += inp[i]
			i+=1
			continue

		# If we hit a unit_char, iterate until we hit the next non-unit char
		# This should give us the entire unit
		j = i
		while j < len(inp):
			if inp[j] in NON_UNIT_CHARS:
				break

			j+=1

		# The unit is either a name or a symbol
		# Take the unit we gathered and get the corresponding symbol
		name_or_symbol = inp[i:j]

		# Find the conversion factor for the symbol
		conversion = get_conversion(name_or_symbol)
		if not conversion:
			return get_rsp("", "", f"invalid name/symbol encountered: {name_or_symbol}")
		output += f"{conversion.base_unit}"
		output_factor += f"({conversion.conversion_value})"

		# set our iterator to be passed the point of the last unit found
		i = j

	# our output_factor must be evaluated and set to 14 decimal places
	try:
		v = eval(output_factor)
		output_factor = '{0:.14f}'.format(v)
	except SyntaxError as err:
		return get_rsp("", "", f"unable to evaluate multiplicative factor: {err}")

	return get_rsp(output, output_factor, "")

	# return output, output_factor, ""





def main():
	pass



if __name__ == "__main__":
	main()

