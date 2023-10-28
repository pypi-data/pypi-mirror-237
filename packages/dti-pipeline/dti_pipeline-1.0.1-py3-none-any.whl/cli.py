from .main import Pipeline
import os
from os.path import expanduser

def main():
	instance = Pipeline()
	instance.run()


if __name__ == '__main__':
	main()