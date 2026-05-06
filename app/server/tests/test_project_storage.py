import unittest
from unittest.mock import Mock

from bson.objectid import ObjectId

from models.Projects import Projects
from utils.storage import PublicStorageConnector


class PublicStorageConnectorTests(unittest.TestCase):
    def test_build_public_url_from_storage_key(self):
        connector = PublicStorageConnector(base_url='https://assets.example.com')

        public_url = connector.build_public_url('projects/my project/preview image.webp')

        self.assertEqual(
            public_url,
            'https://assets.example.com/projects/my%20project/preview%20image.webp',
        )

    def test_build_public_url_accepts_direct_url(self):
        connector = PublicStorageConnector(base_url='https://assets.example.com')

        public_url = connector.build_public_url('https://cdn.example.com/projects/preview.webp')

        self.assertEqual(public_url, 'https://cdn.example.com/projects/preview.webp')


class ProjectSerializationTests(unittest.TestCase):
    def setUp(self):
        self.projects = Projects()
        self.projects.storage = Mock()
        self.project_id = ObjectId('507f1f77bcf86cd799439011')
        self.project_document = {
            '_id': self.project_id,
            'name': 'Portfolio',
            'description': 'Stored in MongoDB',
            'assets': {
                'preview': {
                    'storage_key': 'projects/portfolio/preview.webp',
                    'alt': 'Portfolio preview',
                },
                'details': {
                    'storage_key': 'projects/portfolio/details.md',
                },
            },
        }

    def test_serialize_project_resolves_preview_for_list_responses(self):
        self.projects.storage.resolve_asset.side_effect = [
            {
                'storage_key': 'projects/portfolio/preview.webp',
                'url': 'https://assets.example.com/projects/portfolio/preview.webp',
                'alt': 'Portfolio preview',
            },
            {
                'storage_key': 'projects/portfolio/details.md',
                'url': 'https://assets.example.com/projects/portfolio/details.md',
            },
        ]

        serialized_project = self.projects.serialize_project(
            self.project_document,
            include_details_content=False,
        )

        self.assertEqual(serialized_project['_id'], str(self.project_id))
        self.assertEqual(
            serialized_project['image'],
            'https://assets.example.com/projects/portfolio/preview.webp',
        )
        self.assertEqual(
            serialized_project['details']['url'],
            'https://assets.example.com/projects/portfolio/details.md',
        )
        self.assertEqual(serialized_project['description'], 'Stored in MongoDB')
        self.projects.storage.read_text.assert_not_called()

    def test_serialize_project_reads_public_details_for_single_project(self):
        self.projects.storage.resolve_asset.side_effect = [
            {
                'storage_key': 'projects/portfolio/preview.webp',
                'url': 'https://assets.example.com/projects/portfolio/preview.webp',
                'alt': 'Portfolio preview',
            },
            {
                'storage_key': 'projects/portfolio/details.md',
                'url': 'https://assets.example.com/projects/portfolio/details.md',
            },
        ]
        self.projects.storage.read_text.return_value = '# Portfolio\n\nStored in R2'

        serialized_project = self.projects.serialize_project(
            self.project_document,
            include_details_content=True,
        )

        self.assertEqual(serialized_project['description'], '# Portfolio\n\nStored in R2')
        self.projects.storage.read_text.assert_called_once_with(serialized_project['details'])


if __name__ == '__main__':
    unittest.main()
