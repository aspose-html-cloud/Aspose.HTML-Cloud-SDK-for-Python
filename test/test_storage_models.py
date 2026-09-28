# coding: utf-8

"""
--------------------------------------------------------------------------------------------------------------------
 <copyright company="Aspose" file="test_storage_models.py">
   Copyright (c) 2022 Aspose.HTML for Cloud
 </copyright>
 <summary>
  Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all
 copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE.
</summary>
--------------------------------------------------------------------------------------------------------------------
"""

from __future__ import absolute_import
import unittest
import datetime
from asposehtmlcloud.models import *


class TestStorageModels(unittest.TestCase):

    """Parameters
        'name': 'str',
        'is_folder': 'bool',
        'modified_date': 'datetime',
        'size': 'int',
        'path': 'str'
    """
    def test_storage_file(self):
        model1 = StorageFile(name='test', is_folder=False, modified_date=datetime.date.today(),
                             size=100, path='test_path')
        model2 = StorageFile(name='test', is_folder=False, modified_date=datetime.date.today(),
                             size=100, path='test_path')
        model3 = StorageFile(name='test', is_folder=True, modified_date=datetime.date.today(),
                             size=0, path='test_path')

        self.assertTrue(isinstance(model1, StorageFile))
        self.assertTrue(isinstance(model1.name, str))
        self.assertTrue(isinstance(model1.is_folder, bool))
        self.assertTrue(isinstance(model1.modified_date, datetime.date))
        self.assertTrue(isinstance(model1.size, int))
        self.assertTrue(isinstance(model1.path, str))
        self.assertTrue(isinstance(model3.to_dict(), dict))

        dictionary = model3.to_dict()
        self.assertTrue('name' in dictionary)
        self.assertTrue('is_folder' in dictionary)
        self.assertTrue('modified_date' in dictionary)
        self.assertTrue('size' in dictionary)
        self.assertTrue('path' in dictionary)

        self.assertEqual(model1, model2)
        self.assertNotEqual(model1, model3)

    """Parameters
        'request_id': 'str',
        '_date': 'datetime'
    """
    def test_error_details(self):
        date = datetime.date.today()
        model1 = ErrorDetails(request_id="ID111111111", _date=date)
        model2 = ErrorDetails(request_id="ID222222222", _date=date)
        model3 = ErrorDetails(request_id="ID111111111", _date=date)

        self.assertTrue(isinstance(model1, ErrorDetails))
        self.assertTrue(isinstance(model1.request_id, str))
        self.assertTrue(isinstance(model1._date, datetime.date))

        dictionary = model3.to_dict()
        self.assertTrue(isinstance(dictionary, dict))

        self.assertTrue('request_id' in dictionary)
        self.assertTrue('_date' in dictionary)

        self.assertEqual(model1, model3)
        self.assertNotEqual(model1, model2)

    """Parameters
        'code': 'str',
        'message': 'str',
        'description': 'str',
        'inner_error': 'ErrorDetails'
    """
    def test_error(self):
        inner = ErrorDetails(request_id="ID111111111", _date=datetime.date.today())

        model1 = Error(code="200", message="Message1", description="Descr", inner_error=None)
        model2 = Error(code="400", message="Message2", description="Descr", inner_error=inner)
        model3 = Error(code="200", message="Message1", description="Descr", inner_error=None)

        self.assertTrue(isinstance(model1, Error))
        self.assertTrue(isinstance(model1.code, str))
        self.assertTrue(isinstance(model1.message, str))
        self.assertTrue(isinstance(model1.description, str))
        self.assertTrue(isinstance(model2.inner_error, ErrorDetails))

        dictionary = model3.to_dict()
        self.assertTrue(isinstance(dictionary, dict))

        self.assertTrue('code' in dictionary)
        self.assertTrue('message' in dictionary)
        self.assertTrue('description' in dictionary)
        self.assertTrue('inner_error' in dictionary)

        self.assertEqual(model1, model3)
        self.assertNotEqual(model1, model2)

    """Parameters
        'name': 'str',
        'is_folder': 'bool',
        'modified_date': 'datetime',
        'size': 'int',
        'path': 'str'
        'version_id': 'str',
        'is_latest': 'bool'
    """
    def test_file_version(self):
        date = datetime.date.today()

        model1 = FileVersion(name='test.txt', is_folder=False, modified_date=date, size=100, path='/',
                             version_id="1.0.1", is_latest=False)

        model2 = FileVersion(name='Folder', is_folder=True, modified_date=date, size=0, path='/',
                             version_id="1.0.1", is_latest=False)

        model3 = FileVersion(name='test.txt', is_folder=False, modified_date=date, size=100, path='/',
                             version_id="1.0.1", is_latest=False)

        self.assertTrue(isinstance(model1, FileVersion))
        self.assertTrue(isinstance(model1.version_id, str))
        self.assertTrue(isinstance(model1.is_latest, bool))

        dictionary = model3.to_dict()
        self.assertTrue(isinstance(dictionary, dict))

        self.assertTrue('version_id' in dictionary)
        self.assertTrue('is_latest' in dictionary)
        self.assertEqual(model1, model3)
        self.assertNotEqual(model1, model2)

    """Parameters
        'value': 'list[FileVersion]'
    """
    def test_file_versions(self):
        date = datetime.date.today()

        model1 = FileVersion(name='test.txt', is_folder=False, modified_date=date, size=100, path='/',
                             version_id="1.0.1", is_latest=False)

        model2 = FileVersion(name='Folder', is_folder=True, modified_date=date, size=0, path='/',
                             version_id="1.0.1", is_latest=False)

        model3 = FileVersion(name='test.txt', is_folder=False, modified_date=date, size=100, path='/',
                             version_id="1.0.1", is_latest=False)

        model_ver1 = FileVersions(value=[model1, model2, model3])
        model_ver2 = FileVersions(value=[model3, model2])
        model_ver3 = FileVersions(value=[model1, model2, model3])

        self.assertTrue(isinstance(model_ver1, FileVersions))
        self.assertTrue(isinstance(model_ver1.value, list))

        dictionary = model_ver1.to_dict()
        self.assertTrue(isinstance(dictionary, dict))

        self.assertEqual(model_ver1, model_ver3)
        self.assertNotEqual(model_ver1, model_ver2)

    """Parameters
        'value': 'list[StorageFile]'
    """
    def test_files_list(self):
        date = datetime.date.today()
        sf1 = StorageFile(name='test', is_folder=False, modified_date=date,
                          size=100, path='test_path')
        sf2 = StorageFile(name='test', is_folder=False, modified_date=date,
                          size=100, path='test_path')
        sf3 = StorageFile(name='test', is_folder=True, modified_date=date,
                          size=0, path='test_path')

        model1 = FilesList(value=[sf1, sf2, sf3])
        model2 = FilesList(value=[sf1, sf3])
        model3 = FilesList(value=[sf1, sf2, sf3])

        self.assertTrue(isinstance(model1, FilesList))
        self.assertTrue(isinstance(model1.value, list))

        dictionary = model1.to_dict()
        self.assertTrue(isinstance(dictionary, dict))

        self.assertEqual(model1, model3)
        self.assertNotEqual(model1, model2)

    """Parameters
        'uploaded': 'list[str]',
        'errors': 'list[Error]'
    """
    def test_files_upload_result(self):
        err = Error(code="400", message="Message2", description="Descr", inner_error=None)

        model1 = FilesUploadResult(uploaded=["file1.txt", "file2.txt"], errors=[])
        model2 = FilesUploadResult(uploaded=[], errors=[err])
        model3 = FilesUploadResult(uploaded=["file1.txt", "file2.txt"], errors=[])

        self.assertTrue(isinstance(model1, FilesUploadResult))
        self.assertTrue(isinstance(model1.uploaded, list))
        self.assertTrue(isinstance(model1.errors, list))

        dictionary = model1.to_dict()
        self.assertTrue(isinstance(dictionary, dict))

        self.assertEqual(model1, model3)
        self.assertNotEqual(model1, model2)

    """Parameters
        'exists': 'bool',
        'is_folder': 'bool'
    """
    def test_object_exist(self):
        model1 = ObjectExist(exists=True, is_folder=True)
        model2 = ObjectExist(exists=False, is_folder=False)
        model3 = ObjectExist(exists=True, is_folder=True)

        self.assertTrue(isinstance(model1, ObjectExist))
        self.assertTrue(isinstance(model1.exists, bool))
        self.assertTrue(isinstance(model1.is_folder, bool))

        dictionary = model3.to_dict()
        self.assertTrue(isinstance(dictionary, dict))
        self.assertTrue('exists' in dictionary)
        self.assertTrue('is_folder' in dictionary)
        self.assertEqual(model1, model3)
        self.assertNotEqual(model1, model2)


if __name__ == '__main__':
    unittest.main()
