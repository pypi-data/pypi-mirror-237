import requests
from bs4 import BeautifulSoup
import os
import sys

if os.name == 'nt':
		try:
				import msvcrt
		except ImportError:
				print("Failed to import msvcrt on Windows.")
				exit(1)
else:
		try:
				import termios
				import tty
		except ImportError:
				print("Failed to import termios/tty on Linux.")
				exit(1)

def detect_arrow_key():
		if os.name == 'nt':  # Windows
				while True:
						key = msvcrt.getch()
						if key == b'\xe0':
								key = msvcrt.getch()
								if key == b'H':
										return 'up'
								elif key == b'P':
										return 'down'
						elif key == b'\r':
								return 'enter'
		else:  # Linux
				fd = sys.stdin.fileno()
				old_settings = termios.tcgetattr(fd)
				try:
						tty.setraw(fd)
						while True:
								key = sys.stdin.read(1)
								if key == '\x1b':
										key = sys.stdin.read(2)
										if key == '[A':
												return 'up'
										elif key == '[B':
												return 'down'
								elif key == '\r':
										return 'enter'
				finally:
						termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def white_bg(text):
		white = f"\033[97;40m{text}\033[0m"
		return white

def clear_last_x_lines(lines_to_clear):
	if os.name == 'posix':
			# On Linux, use ANSI escape codes
			for _ in range(lines_to_clear):
					print("\033[F\033[K", end="")  # Move up and clear line
	elif os.name == 'nt':
			# On Windows, use os.system('cls') to clear the console
			for _ in range(lines_to_clear):
					os.system('cls')
	else:
			# For other operating systems, simply print newlines to simulate clearing
			print('\n' * lines_to_clear)
		
def choice_input(choice):
	i = 0
	a = 0
	while True:
		for x in choice:
				if i == a:
						print(white_bg(x))
				else:
						print(x)
				a += 1
				if a == len(choice):  # Reset 'a' to 0 when it reaches the end of the list
						a = 0
		user_input = detect_arrow_key()
		if user_input == 'up' and i > 0:
				i -= 1
		elif user_input == 'down' and i < len(choice) - 1:
				i += 1
		elif user_input == 'enter':
				return choice[i]
		clear_last_x_lines(len(choice))


def matrixify(columns, rows, filler):
	xyz = [[filler]*columns for _ in range(rows)]
	return xyz
def display(matrix):
	for row in matrix:
		print (" ".join(map(str,row)))
def replace_index(matrix, x, y, filler):
	matrix[x][y] = filler
	return matrix
def contains(matrix, string):
	for row in matrix:
		if string in row:
			return True
	return False
def replace(matrix, string, filler):
	for x in range(len(matrix)):
		for y in range(len(matrix[x])):
			if matrix[x][y] == string:
				matrix[x][y] = filler
	return matrix
def webscrape(url):
	try:
		response = requests.get(url)
		if response.status_code == 200:
			html = response.text
			soup = BeautifulSoup(html, 'html.parser')
			return(soup)
		else:
			return response.status_code
	except:
		return "Error while scraping:"+url

