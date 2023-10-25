import csv
import io
import chess
from chess import pgn
import hashlib
from os.path import exists
import os

'''
    The following functions manage the buttons of the graphical user interface.
'''

def _createCSV(path, *columns):
    """
    The function creates a CSV file in the desired path and with the desired column names.

    Args:
        a: PGN path
        b: Names of column

    Returns:
        csv file

    """
    csv_exists = os.path.exists(path)
    if not csv_exists:
        with open(path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(columns)