# coding: utf-8
"""
--------------------------------------------------------------------------------------------------------------------
<copyright company="Aspose" file="conversion_request.py">
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

import pprint
import re  # noqa: F401
import six

class ConversionRequest(object):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    model_types = {
        'input_path': 'str',
        'storage_name': 'str',
        'resources': 'list[str]',
        'output_file': 'str',
        'options': 'dict(str, str)',
        'pdf_metadata': 'PdfMetadata'
    }

    attribute_map = {
        'input_path': 'inputPath',
        'storage_name': 'storageName',
        'resources': 'resources',
        'output_file': 'outputFile',
        'options': 'options',
        'pdf_metadata': 'pdfMetadata'
    }

    def __init__(self, input_path=None, storage_name=None, resources=None, output_file=None, options=None, pdf_metadata=None):  # noqa: E501
        self._input_path = None
        self._storage_name = None
        self._resources = None
        self._output_file = None
        self._options = None
        self._pdf_metadata = None
        self.discriminator = None
        self.input_path = input_path
        if storage_name is not None:
            self.storage_name = storage_name
        if resources is not None:
            self.resources = resources
        if output_file is not None:
            self.output_file = output_file
        if options is not None:
            self.options = options
        if pdf_metadata is not None:
            self.pdf_metadata = pdf_metadata

    @property
    def input_path(self):
        """Gets the input_path of this ConversionRequest.  # noqa: E501


        :return: The input_path of this ConversionRequest.  # noqa: E501
        :rtype: str
        """
        return self._input_path

    @input_path.setter
    def input_path(self, input_path):
        """Sets the input_path of this ConversionRequest.


        :param input_path: The input_path of this ConversionRequest.  # noqa: E501
        :type: str
        """
        if input_path is None:
            raise ValueError("Invalid value for `input_path`, must not be `None`")  # noqa: E501

        self._input_path = input_path

    @property
    def storage_name(self):
        """Gets the storage_name of this ConversionRequest.  # noqa: E501


        :return: The storage_name of this ConversionRequest.  # noqa: E501
        :rtype: str
        """
        return self._storage_name

    @storage_name.setter
    def storage_name(self, storage_name):
        """Sets the storage_name of this ConversionRequest.


        :param storage_name: The storage_name of this ConversionRequest.  # noqa: E501
        :type: str
        """

        self._storage_name = storage_name

    @property
    def resources(self):
        """Gets the resources of this ConversionRequest.  # noqa: E501


        :return: The resources of this ConversionRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this ConversionRequest.


        :param resources: The resources of this ConversionRequest.  # noqa: E501
        :type: list[str]
        """

        self._resources = resources

    @property
    def output_file(self):
        """Gets the output_file of this ConversionRequest.  # noqa: E501


        :return: The output_file of this ConversionRequest.  # noqa: E501
        :rtype: str
        """
        return self._output_file

    @output_file.setter
    def output_file(self, output_file):
        """Sets the output_file of this ConversionRequest.


        :param output_file: The output_file of this ConversionRequest.  # noqa: E501
        :type: str
        """

        self._output_file = output_file

    @property
    def options(self):
        """Gets the options of this ConversionRequest.  # noqa: E501


        :return: The options of this ConversionRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this ConversionRequest.


        :param options: The options of this ConversionRequest.  # noqa: E501
        :type: dict(str, str)
        """

        self._options = options

    @property
    def pdf_metadata(self):
        """Gets the pdf_metadata of this ConversionRequest.  # noqa: E501

        PDF document information (/Info dictionary) metadata applied to the
        produced PDF file. Only meaningful when the conversion target is PDF;
        ignored by the server for other output formats.

        :return: The pdf_metadata of this ConversionRequest.  # noqa: E501
        :rtype: PdfMetadata
        """
        return self._pdf_metadata

    @pdf_metadata.setter
    def pdf_metadata(self, pdf_metadata):
        """Sets the pdf_metadata of this ConversionRequest.


        :param pdf_metadata: The pdf_metadata of this ConversionRequest.  # noqa: E501
        :type: PdfMetadata
        """

        self._pdf_metadata = pdf_metadata

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.model_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ConversionRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ConversionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
