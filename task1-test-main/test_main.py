import unittest
from unittest.mock import patch
from main import check_document_existance, get_doc_owner_name
from main import get_all_doc_owners_names, remove_doc_from_shelf
from main import add_new_shelf, append_doc_to_shelf, delete_doc
from main import get_doc_shelf, move_doc_to_shelf, show_document_info
from main import show_all_docs_info, add_new_doc


class TestMainFunction(unittest.TestCase):
    
    def test_check_document_existance_one(self):
        self.assertEqual(check_document_existance('11-2'), True)
    
    def test_check_document_existance_1(self):
        self.assertIsInstance(check_document_existance(''), bool)
    
    @unittest.expectedFailure
    def test_check_document_existance_3(self):
        self.assertEqual(check_document_existance([]), True)

    @patch('builtins.input', lambda *args: '11-2')
    def test_get_doc_owner_name_1(self):
        self.assertEqual(get_doc_owner_name(), "Геннадий Покемонов")
    
    @patch('builtins.input', lambda *args: '11-2')
    def test_get_doc_owner_name_2(self):
        self.assertIsInstance(get_doc_owner_name(), str)
    
    @unittest.expectedFailure
    @patch('builtins.input', lambda *args: '')
    def test_get_doc_owner_name_3(self):
        self.assertIsInstance(get_doc_owner_name(), str)

    def test_get_all_doc_owners_names(self):
        self.assertIsInstance(get_all_doc_owners_names(), (set, list, tuple))

    def test_remove_doc_from_shelf_1(self):
        self.assertEqual(remove_doc_from_shelf('11-2'), ('1', True))
    
    def test_remove_doc_from_shelf_2(self):
        self.assertEqual(remove_doc_from_shelf(''), ('-1', False))

    @patch('builtins.input', lambda *args: '4')
    def test_add_new_shelf_1(self):
        self.assertEqual(add_new_shelf(), ('4', True))
    
    @patch('builtins.input', lambda *args: '1')
    def test_add_new_shelf_2(self):
        self.assertEqual(add_new_shelf(), ('1', False))
    
    @unittest.expectedFailure
    @patch('builtins.input', lambda *args: 4)
    def test_add_new_shelf_3(self):
        self.assertEqual(add_new_shelf(), ('4', False))

    @patch('builtins.input', lambda *args: '')
    def test_append_doc_to_shelf_1(self):
        self.assertEqual(append_doc_to_shelf('', ''), ('1', True))
    
    @unittest.expectedFailure
    @patch('builtins.input', lambda *args: 7)
    def test_append_doc_to_shelf_2(self):
        self.assertEqual(append_doc_to_shelf('', ''), ('1', True))

    @patch('builtins.input', lambda *args: '11-2')
    def test_delete_doc_1(self):
        self.assertEqual(delete_doc(), ('11-2', True))
    
    @unittest.expectedFailure
    @patch('builtins.input', lambda *args: '')
    def test_delete_doc_2(self):
        self.assertEqual(delete_doc(), ('', True))

    @patch('builtins.input', lambda *args: '11-2')
    def test_get_doc_shelf_1(self):
        self.assertIsInstance(get_doc_shelf(), str)
    
    @patch('builtins.input', lambda *args: '11-2')
    def test_get_doc_shelf_2(self):
        self.assertEqual(get_doc_shelf(), '1')

    @patch('builtins.input', lambda *args: '11-2', '2')
    def test_move_doc_to_shelf_1(self):
        self.assertEqual(move_doc_to_shelf(), '1')
    
    @patch('builtins.input', lambda *args: '', '')
    def test_move_doc_to_shelf_2(self):
        self.assertEqual(move_doc_to_shelf(), '1')

    def test_show_document_info(self):
        doc = {
            "type": "passport", 
            "number": "2207 876234", 
            "name": "Василий Гупкин"
            }
        self.assertEqual(show_document_info(doc), '1')

    def test_show_all_docs_info(self):
        self.assertEqual(show_all_docs_info(), '1')

    @patch('builtins.input', lambda *args: '')
    def test_add_new_doc(self):
        self.assertIsInstance(add_new_doc(), str)