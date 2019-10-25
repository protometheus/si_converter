#!/usr/bin/python3
from math import *
from flask import Flask, request

from units import *

app = Flask(__name__)

# hello is a health route
@app.route("/")
def hello():
	return {"msg": "Hello, World!"}

# get_conversion_factor attempts to convert a provided unit of measure into its base units. 
# This unit may be composed of smaller sub-units; all sub-units are converted individually, 
# then evaluated as a collection to provide the multiplicative factor needed to conver the input unit 
# into the output unit.
@app.route("/units/si")
def convert_units() -> str:
	def get_response(output, output_factor, err):
		return {
			"unit_name": output,
			"multiplication_factor": output_factor,
			"error": err,
		}

	# get the input off the query parameter
	inp = request.args.get('units')
	if not inp:
		return get_response("", "", "no valid input given for 'units' query parameter")

	# remove extra whitespace by splitting and rejoining
	inp = ''.join(inp.split())

	# for each character, check if it is an open parantheses
	# if it's not, exchange its name for its symbol
	output = ""
	output_factor = ""
	err = ""
	i = 0
	name_or_symbol = ""
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
		conversion_factor = get_conversion_factor(name_or_symbol)
		if not conversion_factor:
			return get_response("", "", f"invalid name/symbol encountered: {name_or_symbol}")

		output += f"{conversion_factor.base_unit}"
		output_factor += f"{conversion_factor.conversion_value}"

		# set our iterator to be passed the point of the last unit found
		i = j

	# our output_factor must be evaluated and set to 14 decimal places
	try:
		evaluated_output_factor = eval(output_factor)
		evaluated_output_factor = '{0:.14f}'.format(evaluated_output_factor)
	except SyntaxError as err:
		return get_response("", "", f"unable to evaluate multiplicative factor: {err}")

	return get_response(output, evaluated_output_factor, None)


if __name__ == '__main__':
	app.run(debug=True, port=33507)

