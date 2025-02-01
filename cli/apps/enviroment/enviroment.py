from dotenv import load_dotenv, dotenv_values
import os
from pathlib import Path

PATH_ENV = Path(__file__).parent / '.env'

"""1st way"""

load_dotenv(override=True)

password: str = os.getenv('PASSWORD')
print(f"{password}")

"""2nd way"""
configurations: dict = dotenv_values(PATH_ENV)
print(f"{configurations=}")