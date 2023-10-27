# A decorator that modifies the arguments and keyword arguments of a function based on the calling instance's attributes.

## Tested against Windows / Python 3.11 / Anaconda

## pip install argskwargsmodifierclass

```python
A decorator that modifies the arguments and keyword arguments of a function based on the calling instance's attributes.

Args:
	f_py (function, optional): Reserved for the function; do not use this argument explicitly.

	args_and_function (tuple of tuples): A tuple of tuples where each tuple contains an argument
	name and a function to transform the argument.
	The decorator will apply the specified function to each argument with a matching name.
	Each transformation function takes three arguments: the argument value,
	a dictionary of keyword arguments, and the instance that called the decorated method.

Returns:
	function: The decorated function.

Example:
	from argskwargsmodifierclass import change_args_kwargs
	class ADBTEST:
		def __init__(self, stripit=True):
			self.stripit = stripit

		@change_args_kwargs(
			args_and_function=(
					(
							"text",
							lambda arg, argdict, instance: arg.strip("x")
							if instance.stripit
							else arg,
					),
			)
		)
		def onefunction(self, text,number=10):
			print(f"{text=}")
			print(f"{number=}")


	t = ADBTEST(stripit=True)
	t.onefunction("bibib    xxxx",number=20)
	t.onefunction("bibibx    xxxx",15)

	t2 = ADBTEST(stripit=False)
	t2.onefunction(text="aaabibib",   number=0x5)
	t2.onefunction("aaaabibibx    xx")

	t.stripit = False
	t.onefunction("bibib    xxxx")
	t.onefunction("bibibx    xxxx")

	t2.stripit = True
	t2.onefunction("aaabibib   xxx")
	t2.onefunction("aaaabibibx    xx")

	# text='bibib    '
	# number=20
	# text='bibibx    '
	# number=15
	# text='aaabibib'
	# number=5
	# text='aaaabibibx    xx'
	# number=10
	# text='bibib    xxxx'
	# number=10
	# text='bibibx    xxxx'
	# number=10
	# text='aaabibib   '
	# number=10
	# text='aaaabibibx    '
	# number=10


The `change_args_kwargs` decorator allows you to modify function arguments and keyword arguments based on
the attributes of the calling instance.
It takes a tuple of argument transformations, each of which is defined as a tuple containing an argument name,
a transformation function, and the instance that called the decorated method.
The decorator dynamically adjusts the arguments according to the instance's attributes,
providing fine-grained control over argument modification.

```