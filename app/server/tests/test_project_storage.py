import json
import unittest
from io import BytesIO
from unittest.mock import Mock

from bson.objectid import ObjectId
from botocore.exceptions import ClientError

from models.Projects import Projects
from utils.storage import ObjectStorageConnector


class ObjectStorageConnectorTests(unittest.TestCase):
    def setUp(self):
        self.client = Mock()
        self.client.generate_presigned_url.return_value = 'https://signed.example.com/object'
        self.connector = ObjectStorageConnector(
            bucket_name='portfolio-assets',
            endpoint_url='https://example.r2.cloudflarestorage.com',
            access_key_id='access-key',
            secret_access_key='secret-key',
            client=self.client,
        )

    def test_build_download_url_from_storage_key(self):
        signed_url = self.connector.build_download_url('projects/my project/preview image.webp')

        self.assertEqual(signed_url, 'https://signed.example.com/object')
        self.client.generate_presigned_url.assert_called_once_with(
            'get_object',
            Params={
                'Bucket': 'portfolio-assets',
                'Key': 'projects/my project/preview image.webp',
            },
            ExpiresIn=3600,
        )

    def test_build_download_url_accepts_direct_url(self):
        signed_url = self.connector.build_download_url('https://cdn.example.com/projects/preview.webp')

        self.assertEqual(signed_url, 'https://cdn.example.com/projects/preview.webp')
        self.client.generate_presigned_url.assert_not_called()

    def test_read_text_uses_private_bucket_object(self):
        self.client.get_object.return_value = {
            'ContentType': 'text/markdown',
            'Body': BytesIO(b'# Portfolio\n\nStored in R2'),
        }

        content = self.connector.read_text({'storage_key': 'projects/portfolio/details.md'})

        self.assertEqual(content, '# Portfolio\n\nStored in R2')
        self.client.get_object.assert_called_once_with(
            Bucket='portfolio-assets',
            Key='projects/portfolio/details.md',
        )

    def test_update_object_requires_existing_file(self):
        self.client.head_object.side_effect = ClientError(
            {'Error': {'Code': '404'}},
            'HeadObject',
        )

        with self.assertRaises(FileNotFoundError):
            self.connector.update_object('projects/portfolio/details.md', b'updated')

    def test_upload_and_delete_object_use_private_bucket_client(self):
        uploaded_asset = self.connector.upload_object(
            storage_key='projects/portfolio/preview.webp',
            body=b'preview-bytes',
            content_type='image/webp',
            metadata={'alt': 'Portfolio preview'},
        )

        self.assertEqual(uploaded_asset['storage_key'], 'projects/portfolio/preview.webp')
        self.assertEqual(uploaded_asset['url'], 'https://signed.example.com/object')
        self.client.put_object.assert_called_once()

        deleted = self.connector.delete_object('projects/portfolio/preview.webp')

        self.assertTrue(deleted)
        self.client.delete_object.assert_called_once_with(
            Bucket='portfolio-assets',
            Key='projects/portfolio/preview.webp',
        )


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
                'url': 'https://signed.example.com/preview',
                'alt': 'Portfolio preview',
            },
            {
                'storage_key': 'projects/portfolio/details.md',
                'url': 'https://signed.example.com/details',
            },
        ]

        serialized_project = self.projects.serialize_project(
            self.project_document,
            include_details_content=False,
        )

        self.assertEqual(serialized_project['_id'], str(self.project_id))
        self.assertEqual(
            serialized_project['image'],
            'https://signed.example.com/preview',
        )
        self.assertEqual(
            serialized_project['details']['url'],
            'https://signed.example.com/details',
        )
        self.assertEqual(serialized_project['description'], 'Stored in MongoDB')
        self.projects.storage.read_text.assert_not_called()

    def test_get_projects_serializes_list_without_loading_details_content(self):
        self.projects.find_all = Mock(return_value=[self.project_document])
        self.projects.storage.resolve_asset.side_effect = [
            {
                'storage_key': 'projects/portfolio/preview.webp',
                'url': 'https://signed.example.com/preview',
                'alt': 'Portfolio preview',
            },
            {
                'storage_key': 'projects/portfolio/details.md',
                'url': 'https://signed.example.com/details',
            },
        ]

        serialized_projects = json.loads(self.projects.get_projects())

        self.assertEqual(len(serialized_projects), 1)
        self.assertEqual(serialized_projects[0]['image'], 'https://signed.example.com/preview')
        self.assertEqual(serialized_projects[0]['details']['url'], 'https://signed.example.com/details')
        self.assertEqual(serialized_projects[0]['description'], 'Stored in MongoDB')
        self.projects.storage.read_text.assert_not_called()

    def test_serialize_project_reads_private_details_for_single_project(self):
        self.projects.storage.resolve_asset.side_effect = [
            {
                'storage_key': 'projects/portfolio/preview.webp',
                'url': 'https://signed.example.com/preview',
                'alt': 'Portfolio preview',
            },
            {
                'storage_key': 'projects/portfolio/details.md',
                'url': 'https://signed.example.com/details',
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
