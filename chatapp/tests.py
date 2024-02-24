import unittest
from django.test import TestCase
from django.contrib.auth.models import User
from pymongo import MongoClient
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

class TestDatabaseConnection(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = MongoClient('mongodb+srv://kristinaer304:Kris0192@cluster0.vuekyu7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
        cls.db = cls.client['Author']
        cls.collection = cls.db['users']

    @classmethod
    def tearDownClass(cls):

        cls.client.close()
        super().tearDownClass()

    def test_user_collection_exists(self):

        self.assertIn('users', self.db.list_collection_names())

    def test_user_insertion(self):

        test_user = {
            'username': 'test_user',
            'email': 'test@example.com',
            'password': 'tЕest_password123%'
        }
        self.collection.insert_one(test_user)


        self.assertIsNotNone(self.collection.find_one({'username': 'test_user'}))

    def test_user_retrieval(self):

        user_data = self.collection.find_one({'username': 'Alena_r'})
        self.assertIsNotNone(user_data)

    


    

if __name__ == '__main__':
    unittest.main()

