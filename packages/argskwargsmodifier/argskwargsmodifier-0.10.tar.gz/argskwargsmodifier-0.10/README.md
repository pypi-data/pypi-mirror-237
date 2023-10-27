# A decorator that modifies the arguments and keyword arguments of a function before calling it.

## Tested against Windows / Python 3.11 / Anaconda

## pip install argskwargsmodifier

```python
A decorator that modifies the arguments and keyword arguments of a function before calling it.

Args:
	f_py (function, optional): Reserved for the function; do not use this argument explicitly.
	args_and_function (tuple of tuples): A tuple of tuples where each tuple contains
		an argument name and a function to transform the argument. The decorator will apply
		the specified function to each argument with a matching name. Each transformation
		function takes two arguments: the argument value and a dictionary containing all
		keyword arguments and arguments (transformed into kwargs) passed to the decorated function.

Returns:
	function: The decorated function.

Example:
	from argskwargsmodifier import change_args_kwargs
	@change_args_kwargs(
		args_and_function=(
			("arg1", lambda arg, allkwargs: arg * 2),
			("arg2", lambda arg, allkwargs: arg * 3 if arg else None),
			("arg3", lambda arg, allkwargs: arg * 5 if allkwargs.get('arg2') else arg * 50 ),
		)
	)
	def example_function(arg1, arg2=None, arg3=None):
		print(arg1, arg2, arg3)
		pass


	# Test the decorated function
	example_function(1, arg3=3)
	# Output: 2 None 150
	example_function(1, 54, arg3=3)
	# Output: 2 162 15

The `change_args_kwargs` decorator allows you to modify arguments and keyword arguments based on
the provided `args_and_function` list before invoking the decorated function. Each transformation
function in `args_and_function` receives the argument's value and a dictionary of all keyword
arguments passed to the decorated function, giving you flexibility in argument modification.

```