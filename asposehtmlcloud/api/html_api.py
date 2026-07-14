# coding: utf-8
"""Copyright
--------------------------------------------------------------------------------------------------------------------
<copyright company="Aspose" file="html_api.py">
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

import time
from shutil import copy2

from asposehtmlcloud.alias import aliased
from asposehtmlcloud.alias import alias
from asposehtmlcloud.api.storage_api import StorageApi
from asposehtmlcloud.api_client import ApiClient

# python 2 and python 3 compatibility library
import six

import os.path

from asposehtmlcloud.models.conversion_request import ConversionRequest


@aliased
class HtmlApi(object):

    def __init__(self, config=None):
        if config is None:
            api_client = ApiClient()
        else:
            api_client = ApiClient(config)
        self.api_client = api_client
        self.storage = StorageApi(self.api_client)

    ##########################################################
    #                  Conversion API
    ##########################################################

    @alias('convertLocalToLocal', 'ConvertLocalToLocal')
    def convert_local_to_local(self, input_file, output_file, options=None, pdf_metadata=None):
        """Convert a documents from the local file by its name to the specified formats.
        The result will be saved to the local path.

        :param str input_file: Full path to the input file for conversion. (required)
        :param str output_file: Resulting full path to the result file. (required)
        :param object options: Options for conversion. (optional)
        :param PdfMetadata pdf_metadata: PDF /Info metadata applied when output is PDF. (optional)
        :return: ConversionResult. If the method is called asynchronously, returns the request thread.
        """
        return self.convert(
            input_file,
            output_file,
            src_in_local=True,
            dest_in_local=True,
            is_url=False,
            options=options,
            storage_name=None,
            pdf_metadata=pdf_metadata
        )

    @alias('convertLocalToStorage', 'ConvertLocalToStorage')
    def convert_local_to_storage(self, input_file, output_file, storage_name, options=None, pdf_metadata=None):
        """Convert a documents from the local file by its name to the specified formats.
        The result will be saved to the storage.

        :param str input_file: Full path to the input file for conversion(html, epub formats). (required)
        :param str output_file: Resulting full path to the result file. (required)
        :param str storage_name: Name of the storage. None if it has default name.
        :param object options: Options for conversion. (optional)
        :param PdfMetadata pdf_metadata: PDF /Info metadata applied when output is PDF. (optional)
        :return: ConversionResult. If the method is called asynchronously, returns the request thread.
        """
        return self.convert(
            input_file,
            output_file,
            src_in_local=True,
            dest_in_local=False,
            is_url=False,
            options=options,
            storage_name=storage_name,
            pdf_metadata=pdf_metadata
        )

    @alias('convertStorageToLocal', 'ConvertStorageToLocal')
    def convert_storage_to_local(self, input_file, output_file, storage_name, options=None, pdf_metadata=None):
        """Convert a documents from the storage file by its name to the specified formats.
        The result will be saved to the local path.

        :param str input_file: Full path to the input file for conversion(html, epub formats). (required)
        :param str output_file: Resulting full path to the result file. (required)
        :param str storage_name: Name of the storage. None if it has default name.
        :param object options: Options for conversion. (optional)
        :param PdfMetadata pdf_metadata: PDF /Info metadata applied when output is PDF. (optional)
        :return: ConversionResult. If the method is called asynchronously, returns the request thread.
        """
        return self.convert(
            input_file,
            output_file,
            src_in_local=False,
            dest_in_local=True,
            is_url=False,
            options=options,
            storage_name=storage_name,
            pdf_metadata=pdf_metadata
        )

    @alias('convertStorageToStorage', 'ConvertStorageToStorage')
    def convert_storage_to_storage(self, input_file, output_file, storage_name, options=None, pdf_metadata=None):
        """Convert a documents from the storage file by its name to the specified formats.
        The result will be saved to the storage.

        :param str input_file: Full path to the input file for conversion(html, epub formats). (required)
        :param str output_file: Resulting full path to the result file. (required)
        :param object options: Options for conversion. (optional)
        :param str storage_name: Name of the storage. None if it has default name.
        :param PdfMetadata pdf_metadata: PDF /Info metadata applied when output is PDF. (optional)
        :return: ConversionResult. If the method is called asynchronously, returns the request thread.
        """
        return self.convert(
            input_file,
            output_file,
            src_in_local=False,
            dest_in_local=False,
            is_url=False,
            options=options,
            storage_name=storage_name,
            pdf_metadata=pdf_metadata
        )


    @alias('convertUrlToLocal', 'ConvertUrlToLocal')
    def convert_url_to_local(self, input_file, output_file, options=None, pdf_metadata=None):
        """Convert the HTML documents from the URL to the specified formats.
        The result will be saved to the local path.

        :param str input_file: Input URL for conversion(html, epub formats). (required)
        :param str output_file: Resulting full path to the result file. (required)
        :param object options: Options for conversion. (optional)
        :param PdfMetadata pdf_metadata: PDF /Info metadata applied when output is PDF. (optional)
        :return: ConversionResult. If the method is called asynchronously, returns the request thread.
        """
        return self.convert(
            input_file,
            output_file,
            src_in_local=False,
            dest_in_local=True,
            is_url=True,
            options=options,
            storage_name=None,
            pdf_metadata=pdf_metadata
        )

    @alias('convertStorageToStorage', 'ConvertStorageToStorage')
    def convert_url_to_storage(self, input_file, output_file, storage_name, options=None, pdf_metadata=None):
        """Convert the HTML documents from the URL to the specified formats.
        The result will be saved to the storage.

        :param str input_file: Input URL for conversion. (required)
        :param str output_file: Resulting full path to the result file. (required)
        :param str storage_name: Name of the storage. (optional)
        :param object options: Options for conversion. (optional)
        :param PdfMetadata pdf_metadata: PDF /Info metadata applied when output is PDF. (optional)
        :return: ConversionResult. If the method is called asynchronously, returns the request thread.
        """
        return self.convert(
            input_file,
            output_file,
            src_in_local=False,
            dest_in_local=False,
            is_url=True,
            options=options,
            storage_name=storage_name,
            pdf_metadata=pdf_metadata
        )

    @alias('vectorizeLocalToLocal', 'VectorizeLocalToLocal')
    def vectorize_local_to_local(self, input_file, output_file, options=None):
        """Vectorize an image from the local file by its name to the SVG formats.
        The result will be saved to the local path.

        :param str input_file: Full path to the input file for vectorization(png, gif, bmp, jpeg, tiff formats). (required)
        :param str output_file: Resulting full path to the result svg file. (required)
        :param object options: Options for vectorization. (optional)
        :param float options.error_threshold: This parameter defines maximum deviation of points to fitted curve. By default it is 30. (optional)
        :param int options.max_iterations: This parameter defines number of iteration for least-squares approximation method. By default it is 30. (optional)
        :param int options.options.colors_limit: The maximum number of colors used to quantize an image. Default value is 25. (optional)
        :param float options.line_width: The value of this parameter is affected by the graphics scale. Default value is 1. (optional)
        :return: ConversionResult. If the method is called asynchronously, returns the request thread.
        """
        return self.vectorize(
            input_file,
            output_file,
            src_in_local=True,
            dest_in_local=True,
            options=options,
            storage_name=None
        )

    @alias('vectorizeLocalToStorage', 'VectorizeLocalToStorage')
    def vectorize_local_to_storage(self, input_file, output_file, storage_name, options=None):
        """Vectorize an image from the local file by its name to the specified formats.
        The result will be saved to the storage.

        :param str input_file: Full path to the input file for vectorization(png, gif, bmp, jpeg, tiff formats). (required)
        :param str output_file: Resulting full path to the result svg file. (required)
        :param str storage_name: Name of the storage. None if it has default name.
        :param object options: Options for vectorization. (optional)
        :param float options.error_threshold: This parameter defines maximum deviation of points to fitted curve. By default it is 30. (optional)
        :param int options.max_iterations: This parameter defines number of iteration for least-squares approximation method. By default it is 30. (optional)
        :param int options.options.colors_limit: The maximum number of colors used to quantize an image. Default value is 25. (optional)
        :param float options.line_width: The value of this parameter is affected by the graphics scale. Default value is 1. (optional)
        :return: ConversionResult. If the method is called asynchronously, returns the request thread.
        """
        return self.vectorize(
            input_file,
            output_file,
            src_in_local=True,
            dest_in_local=False,
            options=options,
            storage_name=storage_name
        )

    @alias('vectorizeStorageToLocal', 'VectorizeStorageToLocal')
    def vectorize_storage_to_local(self, input_file, output_file, storage_name, options=None):
        """Vectorize an image from the storage file by its name to the specified formats.
        The result will be saved to the local path.

        :param str input_file: Full path to the input file for vectorization(png, gif, bmp, jpeg, tiff formats). (required)
        :param str output_file: Resulting full path to the result svg file. (required)
        :param str storage_name: Name of the storage. None if it has default name.
        :param object options: Options for vectorization. (optional)
        :param float options.error_threshold: This parameter defines maximum deviation of points to fitted curve. By default it is 30. (optional)
        :param int options.max_iterations: This parameter defines number of iteration for least-squares approximation method. By default it is 30. (optional)
        :param int options.options.colors_limit: The maximum number of colors used to quantize an image. Default value is 25. (optional)
        :param float options.line_width: The value of this parameter is affected by the graphics scale. Default value is 1. (optional)
        :return: ConversionResult. If the method is called asynchronously, returns the request thread.
        """
        return self.vectorize(
            input_file,
            output_file,
            src_in_local=False,
            dest_in_local=True,
            options=options,
            storage_name=storage_name
        )

    @alias('vectorizeStorageToStorage', 'VectorizeStorageToStorage')
    def vectorize_storage_to_storage(self, input_file, output_file, storage_name, options=None):
        """Vectorize an image from the storage file by its name to the svg format.
        The result will be saved to the storage.

        :param str input_file: Full path to the input file for vectorization(png, gif, bmp, jpeg, tiff formats). (required)
        :param str output_file: Resulting full path to the result svg file. (required)
        :param object options: Options for vectorization. (optional)
        :param str storage_name: Name of the storage. None if it has default name.
        :param float options.error_threshold: This parameter defines maximum deviation of points to fitted curve. By default it is 30. (optional)
        :param int options.max_iterations: This parameter defines number of iteration for least-squares approximation method. By default it is 30. (optional)
        :param int options.options.colors_limit: The maximum number of colors used to quantize an image. Default value is 25. (optional)
        :param float options.line_width: The value of this parameter is affected by the graphics scale. Default value is 1. (optional)
        :return: ConversionResult. If the method is called asynchronously, returns the request thread.
        """
        return self.vectorize(
            input_file,
            output_file,
            src_in_local=False,
            dest_in_local=False,
            options=options,
            storage_name=storage_name
        )

    @alias('Vectorize')
    def vectorize(self, src, dest, src_in_local, dest_in_local, options=None, storage_name=None):
        """Vectorize an image to the svg format.

        :param str input_file: Full path to the input file for vectorization(png, gif, bmp, jpeg, tiff formats). (required)
        :param str output_file: Resulting full path to the result svg file. (required)
        :param bool src_in_local: Boolean parameter. True if the source file in a local directory. (required)
        :param bool dest_in_local: Boolean parameter. True if the result needs to save to a local directory. (required)
        :param object options: Options for vectorization. (optional)
        :param float options.error_threshold: This parameter defines maximum deviation of points to fitted curve. By default it is 30. (optional)
        :param int options.max_iterations: This parameter defines number of iteration for least-squares approximation method. By default it is 30. (optional)
        :param int options.options.colors_limit: The maximum number of colors used to quantize an image. Default value is 25. (optional)
        :param float options.line_width: The value of this parameter is affected by the graphics scale. Default value is 1. (optional)
        :param str storage_name: Name of the storage. (optional)
        :return: ConversionResult. If the method is called asynchronously, returns the request thread.
        """
        input_format = self.__get_input_format(src)

        if input_format not in ['jpeg', 'tiff', 'bmp', 'png', 'gif']:
            raise RuntimeError('Input format must be an image (jpeg, tiff, bmp, png, gif)')

        output_format = os.path.splitext(dest)[1][1:].strip().lower()
        if output_format != 'svg':
            raise RuntimeError("Output format must be SVG")

        return self.convert(src, dest, src_in_local, dest_in_local, False, options, storage_name)

    @alias('Convert')
    def convert(self, src, dest, src_in_local, dest_in_local, is_url, options=None, storage_name=None, pdf_metadata=None):
        """Convert a document to the specified formats.

        :param str src: Full path to the input file or URL for conversion(html, epub formats). (required)
        :param str dest: Resulting full path to the result file. (required)
        :param bool src_in_local: Boolean parameter. True if the source file in a local directory. (required)
        :param bool dest_in_local: Boolean parameter. True if the result needs to save to a local directory. (required)
        :param bool is_url: Boolean parameter. True if source file is URL. (required)
        :param object options: Options for conversion. (optional)
        :param int options.width: Resulting image width. (optional)
        :param int options.height: Resulting image height. (optional)
        :param int options.options.leftmargin: Left resulting image margin. (optional)
        :param int options.rightmargin: Right resulting image margin. (optional)
        :param int options.topmargin: Top resulting image margin. (optional)
        :param int options.bottommargin: Bottom resulting image margin. (optional)
        :param int options.resolution: DPI of rendered image output (PNG, JPEG, BMP, GIF, TIFF, WEBP). Default 96. Ignored for PDF/XPS/DOC/DOCX/MD/MHTML/HTML/SVG. (optional)
        :param int options.jpegquality: Compression of the result image. (optional)
        :param str storage_name: Name of the storage. (optional)
        :param PdfMetadata pdf_metadata: PDF /Info dictionary metadata (title, author, subject, keywords, creator, producer, creationDate, modificationDate). Only meaningful when target format is PDF. (optional)
        :return: ConversionResult. If the method is called asynchronously, returns the request thread.
        """
        if src_in_local:
            res = self.storage.upload_file("/", src)
            if len(res.uploaded) != 1 or len(res.errors) != 0:
                raise RuntimeError('Unable to upload file')
            file_in_storage = res.uploaded[0]
        else:
            file_in_storage = src

        out_folder, out_file = os.path.split(dest)

        if not dest_in_local:
            out_file = dest

        input_format = 'html'

        if not is_url:
            input_format = self.__get_input_format(src)

        output_format = os.path.splitext(dest)[1][1:].strip().lower()

        if output_format == 'jpg':
            output_format = 'jpeg'
        if output_format == 'mht':
            output_format = 'mhtml'
        if output_format == 'tif':
            output_format = 'tiff'

        path_params = {
            'from': input_format,
            'to': output_format
        }

        query_params = []
        header_params = {}
        local_var_files = {}
        form_params = {}
        collection_formats = {}
        if options is None:
            options = {}

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json'])

        req_body = ConversionRequest(input_path=file_in_storage, storage_name=storage_name, output_file=out_file,
                                     options=options, pdf_metadata=pdf_metadata)

        result = self.api_client.call_api(
            '/html/conversion/{from}-{to}', 'POST',
            path_params,
            query_params,
            header_params,
            body=req_body,
            post_params=form_params,
            files=local_var_files,
            response_type='ConversionResult',
            async_req=False,
            _return_http_data_only=True,
            _preload_content=True,
            _request_timeout=None,
            collection_formats=collection_formats)

        if not isinstance(result.id, str):
            raise RuntimeError("Error create task")

        if not (isinstance(result.code, int)):
            raise RuntimeError("Error get task's id")

        if result.code != 200:
            raise RuntimeError("Error code for create task")

        while True:
            res = self.__get_status(result.id)
            if res.code != 200 or res.status == 'faulted' or res.status == 'canceled':
                raise RuntimeError('Conversion failed')
            if res.status == 'completed':
                break
            time.sleep(3)

        if dest_in_local:
            d = self.storage.download_file(res.file)
            self.__move_file(d, out_folder)
            res.file = out_folder + '/' + os.path.basename(res.file)
        return res

    @classmethod
    def __move_file(cls, src_file, dst_dir):
        if os.path.isfile(src_file):
            copy2(src_file, dst_dir)
            os.remove(src_file)

    def __get_status(self, ident):

        header_params = {}
        form_params = {}
        local_var_files = {}
        body_params = None

        path_params = {'id': ident}

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        return self.api_client.call_api(
            '/html/conversion/{id}', 'GET',
            path_params,
            query_params=[],
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConversionResult',
            async_req=False,
            _return_http_data_only=True,
            _preload_content=True,
            _request_timeout=None,
            collection_formats={}
        )

    @classmethod
    def __get_input_format(cls, path):
        formats = ['HTML', 'HTM', 'MHT', 'MHTML', 'XML', 'XHTML', 'EPUB', 'SVG', 'MD', 'PNG', 'JPG', 'JPEG', 'GIF', 'TIF', 'TIFF', 'BMP']
        ext = os.path.splitext(path)[1][1:].strip().upper()

        if ext in formats:
            return {
                ext == 'HTML' or ext == 'HTM': 'html',
                ext == 'MHT' or ext == 'MHTML': 'mhtml',
                ext == 'XML' or ext == 'XHTML': 'xhtml',
                ext == 'EPUB': 'epub',
                ext == 'SVG': 'svg',
                ext == 'MD': 'md',
                ext == 'PNG': 'png',
                ext == 'JPG' or ext == 'JPEG': 'jpeg',
                ext == 'TIF' or ext == 'TIFF': 'tiff',
                ext == 'GIF': 'gif',
                ext == 'BMP': 'bmp'
            }[True]
        return None
