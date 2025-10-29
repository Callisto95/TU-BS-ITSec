from argparse import ArgumentParser
from datetime import datetime
from math import floor
from os import listdir
from pathlib import Path

BASE64_CHARS: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
BASE64_SHIFTS: list[int] = [10, 4, 6, 0]
BASE64_BIT_MASK: int = (2 ** 6) - 1


class Exercise00:
	STUDENT_NAME: str = "Luca Saalfeld"
	
	def __init__(self, name: str | None = None):
		self.name = name if name else ""
	
	@staticmethod
	def deadline(format_: str) -> str:
		return datetime(year=2023, month=11, day=15, hour=9).strftime(format_)
	
	@property
	def txt(self) -> str:
		return f"{self.name[0:17]}..."
	
	@staticmethod
	def format(method: str) -> str:
		if method == "order":
			return "{2} - {1} - {0}"
		
		return "x, y = ({x:.1f}, {y:.4f})"
	
	@staticmethod
	def listfiles(directory: str, type_: str | None = None):
		for file in listdir(directory):
			if not file.endswith(type_):
				continue
			yield file
	
	@staticmethod
	def collatz(start_point: int) -> tuple[list[int], int]:
		if not isinstance(start_point, int):
			return [], 0
		
		current_n: int = start_point
		
		numbers: list[int] = []
		count: int = 0
		
		while current_n != 1:
			count += 1
			
			numbers.append(current_n)
			
			if current_n % 2 == 0:
				current_n = current_n // 2
			else:
				current_n = 3 * current_n + 1
		
		numbers.append(1)
		count += 1
		
		return numbers, count
	
	def __call__(self, /, **kwargs) -> str:
		keys: list[str] = list(kwargs.keys())
		keys.sort()
		
		return "\n".join([f"{key} = {kwargs[key]}" for key in keys])
	
	def __str__(self) -> str:
		output: str = ""
		
		data: bytearray = bytearray(self.name.encode('ascii'))
		base_64_partitions: int = len(data) * 8 // 6
		leftover: int = len(data) * 8 % 6
		
		count: int = -1
		while (count := count + 1) < base_64_partitions:
			data_to_read: int = 1 if (count + 1) % 4 == 0 else 2
			
			shift: int = BASE64_SHIFTS[count % 4]
			offset: int = floor(count * 0.75)
			
			current_data: bytearray = data[offset:offset + data_to_read]
			
			# this can happen on very short strings
			# must be ignored on longer ones
			if len(current_data) == 1 and count == 0:
				current_data.append(0)
			
			current: int = int.from_bytes(current_data) >> shift & BASE64_BIT_MASK
			output += BASE64_CHARS[current]
		
		match leftover:
			case 2:
				output += BASE64_CHARS[(int.from_bytes(data[-1:]) << 4) & BASE64_BIT_MASK]
				output += "=="
			case 4:
				output += BASE64_CHARS[(int.from_bytes(data[-1:]) << 2) & BASE64_BIT_MASK]
				output += "="
		
		return output


# if __name__ == '__main__':
# 	# print(str(Exercise00("Man")))
# 	# print("TWFu")
# 	print(str(Exercise00("ManManMan")))
# 	print("TWFu" * 3)
# 	exit(0)


if __name__ == '__main__':
	parser: ArgumentParser = ArgumentParser()
	parser.add_argument("-b", help="An optional boolean flag (Default: False).", action="store_true", default=False)
	parser.add_argument(
		"-f",
		help="An optional parameter of type float (Default: 0.0).",
		action="store",
		type=float,
		default=0.0,
		metavar="FLOAT"
	)
	parser.add_argument(
		"-i",
		help="An optional parameter of type int (Default: 0).",
		action="store",
		type=int,
		default=0,
		metavar="INT"
	)
	parser.add_argument("FILE", help="The input positional parameter.", action="store", type=Path)
	
	parser.parse_args()
