# coding: utf-8

"""
--------------------------------------------------------------------------------------------------------------------
 <copyright company="Aspose" file="test_storage_api.py">
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
import os
import six
import unittest
import datetime

from asposehtmlcloud.rest import ApiException
from test.test_helper import TestHelper


class TestStorageApi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = TestHelper.storage

    # **************************************************
    #                  Test storage Api
    # **************************************************

    def test_object_exists(self):
        """Test case for object_exists

        Check if a specific file or folder exists
        """
        exist_folder = TestHelper.get_folder()

        res = self.api.object_exists(exist_folder)
        res = res.to_dict()

        self.assertTrue('exists' in res)
        self.assertTrue('is_folder' in res)

        self.assertTrue(isinstance(res['exists'], bool))
        self.assertTrue(isinstance(res['is_folder'], bool))

        self.assertTrue(res['exists'])
        self.assertTrue(res['is_folder'])
        print(res)

        non_exist_file = TestHelper.get_folder() + 'non_exist_file.gif'

        res = self.api.object_exists(non_exist_file)
        res = res.to_dict()

        self.assertFalse(res['exists'])
        self.assertFalse(res['is_folder'])
        print(res)

    # **************************************************
    #                  Test file Api
    # **************************************************

    def test_upload_file(self):
        """Test case for upload_file

        Upload a specific file
        """
        file_name = "test_upload_file.jpg"
        src = TestHelper.get_local_folder() + file_name
        folder = TestHelper.get_folder()

        result = self.api.upload_file(folder, src)
        self.assertTrue(len(result.uploaded) == 1)
        self.assertTrue(len(result.errors) == 0)

        # check file exists
        res = self.api.object_exists(result.uploaded[0])
        res = res.to_dict()

        self.assertTrue(res['exists'])
        self.assertFalse(res['is_folder'])
        print (res)

    def test_delete_file(self):
        """Test case for delete_file

        Remove a specific file
        """

        # upload file to storage
        file_name = "test_for_delete.html"
        src = TestHelper.get_local_folder() + file_name
        folder = 'TestDelete'

        res = self.api.upload_file(folder, src)
        self.assertTrue(len(res.uploaded) == 1)
        self.assertTrue(len(res.errors) == 0)

        # delete file in the storage
        self.api.delete_file(folder + '/' + file_name)

    def test_download_file(self):
        """Test case for download_file

        Download a specific file
        """
        file_name = "test_upload_file.jpg"
        size = TestHelper.get_file_size(file_name)

        # put file to storage
        res = TestHelper.upload_file(file_name)
        self.assertTrue(len(res.uploaded) == 1)
        self.assertTrue(len(res.errors) == 0)

        download_file = TestHelper.get_folder() + "/" + file_name
        save_file = TestHelper.get_local_dest_folder() + "test_upload_file.jpg"

        src = self.api.download_file(download_file)

        TestHelper.move_file(src, save_file)

        self.assertTrue(os.path.getsize(save_file) == size)

    def test_download_non_existin_file(self):
        """Test case for download_file

        Download a specific file
        """
        self.assertRaises(ApiException, self.api.download_file, "non_existing_file.txt")

    def test_create_folder(self):
        """Test case for create_folder

        Create the folder
        """
        folder_name = "test_folder"
        self.api.create_folder(folder_name)

        # Checking if the folder has been created
        res = self.api.object_exists(folder_name)
        self.assertTrue(res.exists)
        self.assertTrue(res.is_folder)
        print(res)

        # Delete folder
        self.api.delete_folder(folder_name)

        # Checking if the folder has been deleted
        res = self.api.object_exists(folder_name)
        self.assertFalse(res.exists)
        self.assertFalse(res.is_folder)
        print(res)

    def test_delete_folder(self):
        """Test case for delete_folder

        Remove a specific folder
        """
        # Create test folder
        folder_name = "tmp_folder"
        self.api.create_folder(folder_name)

        # Checking if the folder has been created
        res = self.api.object_exists(folder_name)
        self.assertTrue(res.exists)
        self.assertTrue(res.is_folder)
        print(res)

        # Delete folder
        self.api.delete_folder(folder_name)

        # Checking if the folder has been deleted
        res = self.api.object_exists(folder_name)
        self.assertFalse(res.exists)
        self.assertFalse(res.is_folder)
        print(res)

    def test_get_files_list(self):
        """Test case for get_files_list

        Get the file listing of a specific folder
        """
        folder = TestHelper.get_folder()
        res = self.api.get_files_list(folder)
        self.assertTrue(isinstance(res.value, list))

        one_file = res.value[0]
        self.assertTrue(isinstance(one_file.name, str))
        self.assertTrue(isinstance(one_file.is_folder, bool))
        self.assertTrue(isinstance(one_file.modified_date, datetime.datetime))
        self.assertTrue(isinstance(one_file.size, int))
        self.assertTrue(isinstance(one_file.path, str))
        print (res)


if __name__ == '__main__':
    unittest.main()
