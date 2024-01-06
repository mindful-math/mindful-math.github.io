from collections.abc import Iterable
from uuid import uuid4


def create_dict_with_duplicates(dict1: dict, dict2: dict) -> dict:
    """Returns a dictionary where shared keys get a list of values
    rather than just one value"""
    new_dict = {key: [value] for key, value in dict1.items()}
    for key, value in dict2.items():
        if key in new_dict:
            new_dict[key] = [new_dict[key], value]
        else:
            new_dict[key] = value

    return new_dict


class SQL:
    """SQL Aggregate Functions in Python"""

    def __init__(self, database: dict[str, Iterable[dict]]) -> None:
        self.database = database

    def COUNT(self, data: Iterable) -> int:
        """Returns the number of data given.

        Note that some databases do not store this
        as metadata, so really it's not O(1)
        like we have below in Python.
        """
        return len(data)

    def SUM(self, data: Iterable[float]) -> float:
        """Returns the sum of float data given.
        """
        return sum(data)

    def AVG(self, data: Iterable[float]) -> float:
        """Returns the average of float data given."""
        return self.SUM(data) / self.COUNT(data)

    def MIN(self, data: Iterable[float]) -> float:
        """Returns the minimum of float data given."""
        return min(data)

    def MAX(self, data: Iterable[float]) -> float:
        """Returns the maximum of float data given."""
        return max(data)

    def COALESCE(self, default=None, *data):
        """Returns the first non-null element in DATA
        and if there is none, it returns DEFAULT."""
        for element in data:
            if element is not None:
                return element

        return default

    def DECODE(self, data: Iterable, target, results: Iterable, default):
        """Returns RESULTS[i] if TARGET equals DATA[i]
        otherwise it returns DEFAULT (i.e. it's an if-else clause)
        """
        for (element, result) in zip(data, results):
            if element == target:
                return result

        return default

    def NULLIF(self, expr1, expr2):
        """Returns null if EXPR1 equals EXPR2 else EXPR1"""
        return self.DECODE([expr1], expr2, [None], expr1)

    def SELECT(self, data: Iterable[dict], column_names: Iterable[str]) -> Iterable[dict]:
        """Returns the subset of COLUMN_NAMES data specified in DATA."""
        new_table = []
        for row in data:
            new_table.append({key: row[key] for key in column_names})

        return new_table

    def INNER_JOIN(self, left_table_name: str, right_table_name: str, on_column: str) -> Iterable[dict]:
        """Returns LEFT_TABLE_NAME joined with RIGHT_TABLE_NAME where their ON_COLUMNS agree"""
        new_table = []
        for left_row in self.database[left_table_name]:
            for right_row in self.database[right_table_name]:
                if left_row[on_column] == right_row[on_column]:
                    join_data = create_dict_with_duplicates(left_row, right_row)
                    new_table.append(join_data)

        return new_table

    def LEFT_JOIN(self, left_table_name: str, right_table_name: str, on_column: str) -> Iterable[dict]:
        """Returns all rows of the LEFT_TABLE_NAME with the rows of the RIGHT_TABLE_NAME only in the
        case where they have matching ON_COLUMN"""
        new_table = []
        for left_row in self.database[left_table_name]:
            match_found = False
            for right_row in self.database[right_table_name]:
                if left_row[on_column] == right_row[on_column]:
                    join_data = create_dict_with_duplicates(left_row, right_row)
                    new_table.append(join_data)
                    match_found = True

            if not match_found:
                new_right_row = {key: None for key, _ in right_row.items()}
                join_data = create_dict_with_duplicates(left_row, new_right_row)
                new_table.append(join_data)

        return new_table

    def RIGHT_JOIN(self, left_table_name: str, right_table_name: str, on_column: str) -> Iterable[dict]:
        """Returns all rows of the LEFT_TABLE with the rows of the RIGHT_TABLE only in the case where they have matching ON_COLUMN"""
        return self.LEFT_JOIN(right_table_name, left_table_name, on_column)

    def FULL_JOIN(self, left_table_name: str, right_table_name: str, on_column: dict) -> Iterable[dict]:
        """Returns all rows of both tables where non-matches from either table are filled with None values"""
        new_left_table = self.LEFT_JOIN(left_table_name, right_table_name, on_column)
        new_table_name = str(uuid4())
        self.database[new_table_name] = new_left_table
        new_table = self.RIGHT_JOIN(new_table_name, right_table_name, on_column)
        del self.database[new_table_name]

    def CROSS_JOIN(self, table1: Iterable[dict], table2: Iterable[dict]) -> Iterable[dict]:
        """Returns all possible combinations of rows from table1 and table2"""
        new_table = []
        for row1 in table1:
            for row2 in table2:
                join_data = create_dict_with_duplicates(row1, row2)
                new_table.append(join_data)

        return new_table
