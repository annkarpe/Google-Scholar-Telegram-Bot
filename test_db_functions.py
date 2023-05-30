import unittest
from unittest.mock import patch

import db_functions
import sqlite3


class TestDbFunctions(unittest.TestCase):

    @patch('db_functions.sqlite3.connect')
    def test_run_query(self, mock_connect):
        query = "TEST QUERY"
        db_functions.run_query(query)
        mock_connect.assert_called_once_with('users_queries.db')


    @patch('db_functions.run_query')
    def test_insert_query(self, mock_run_query):
        db_functions.insert_query(321, 'my_query')
        mock_run_query.assert_called_once_with("INSERT OR IGNORE INTO user_records (user_id, user_query) VALUES(?, ?);",
                        (321, 'my_query'))
        

    @patch('db_functions.run_query')
    def test_remove_record(self, mock_run_query):
        db_functions.remove_record(123, 'test_record')
        mock_run_query.assert_called_once_with("DELETE FROM user_records WHERE user_id = ? AND user_query = ?;",
                        (123, 'test_record'))


    @patch('db_functions.run_query')
    def test_remove_all_records(self, mock_run_query):
        db_functions.remove_all_records()
        mock_run_query.assert_called_once_with("DELETE FROM user_records;")
    


if __name__ == '__main__':
    unittest.main()
        
