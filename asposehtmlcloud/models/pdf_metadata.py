# coding: utf-8
"""
--------------------------------------------------------------------------------------------------------------------
<copyright company="Aspose" file="pdf_metadata.py">
Copyright (c) 2025 Aspose.HTML for Cloud
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

import datetime
import pprint
import re  # noqa: F401
import six


class PdfMetadata(object):
    """PDF document information (/Info dictionary) metadata applied to a
    produced PDF file.

    Only meaningful when the target conversion format is PDF. Fields left
    as ``None`` (the default) are omitted from the request body and the
    server keeps its own engine defaults.

    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    model_types = {
        'title': 'str',
        'author': 'str',
        'subject': 'str',
        'keywords': 'str',
        'creator': 'str',
        'producer': 'str',
        'creation_date': 'datetime',
        'modification_date': 'datetime'
    }

    attribute_map = {
        'title': 'title',
        'author': 'author',
        'subject': 'subject',
        'keywords': 'keywords',
        'creator': 'creator',
        'producer': 'producer',
        'creation_date': 'creationDate',
        'modification_date': 'modificationDate'
    }

    def __init__(self, title=None, author=None, subject=None, keywords=None,
                 creator=None, producer=None, creation_date=None,
                 modification_date=None):  # noqa: E501
        self._title = None
        self._author = None
        self._subject = None
        self._keywords = None
        self._creator = None
        self._producer = None
        self._creation_date = None
        self._modification_date = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if author is not None:
            self.author = author
        if subject is not None:
            self.subject = subject
        if keywords is not None:
            self.keywords = keywords
        if creator is not None:
            self.creator = creator
        if producer is not None:
            self.producer = producer
        if creation_date is not None:
            self.creation_date = creation_date
        if modification_date is not None:
            self.modification_date = modification_date

    @property
    def title(self):
        """Gets the title of this PdfMetadata.

        :return: PDF document title (/Title).
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this PdfMetadata.

        :param title: PDF document title (/Title).
        :type: str
        """
        self._title = title

    @property
    def author(self):
        """Gets the author of this PdfMetadata.

        :return: PDF author (/Author).
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this PdfMetadata.

        :param author: PDF author (/Author).
        :type: str
        """
        self._author = author

    @property
    def subject(self):
        """Gets the subject of this PdfMetadata.

        :return: PDF subject (/Subject).
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this PdfMetadata.

        :param subject: PDF subject (/Subject).
        :type: str
        """
        self._subject = subject

    @property
    def keywords(self):
        """Gets the keywords of this PdfMetadata.

        :return: PDF keywords (/Keywords).
        :rtype: str
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this PdfMetadata.

        :param keywords: PDF keywords (/Keywords).
        :type: str
        """
        self._keywords = keywords

    @property
    def creator(self):
        """Gets the creator of this PdfMetadata.

        :return: PDF creator (/Creator).
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this PdfMetadata.

        :param creator: PDF creator (/Creator).
        :type: str
        """
        self._creator = creator

    @property
    def producer(self):
        """Gets the producer of this PdfMetadata.

        :return: PDF producer (/Producer).
        :rtype: str
        """
        return self._producer

    @producer.setter
    def producer(self, producer):
        """Sets the producer of this PdfMetadata.

        :param producer: PDF producer (/Producer).
        :type: str
        """
        self._producer = producer

    @property
    def creation_date(self):
        """Gets the creation_date of this PdfMetadata.

        :return: PDF creation date (/CreationDate), ISO 8601 datetime.
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this PdfMetadata.

        Accepts either a ``datetime`` instance or an ISO 8601 string.

        :param creation_date: PDF creation date (/CreationDate).
        :type: datetime or str
        """
        self._creation_date = creation_date

    @property
    def modification_date(self):
        """Gets the modification_date of this PdfMetadata.

        :return: PDF modification date (/ModDate), ISO 8601 datetime.
        :rtype: datetime
        """
        return self._modification_date

    @modification_date.setter
    def modification_date(self, modification_date):
        """Sets the modification_date of this PdfMetadata.

        Accepts either a ``datetime`` instance or an ISO 8601 string.

        :param modification_date: PDF modification date (/ModDate).
        :type: datetime or str
        """
        self._modification_date = modification_date

    def to_dict(self):
        """Returns the model properties as a dict.

        Fields that are ``None`` are omitted so that the server keeps its
        engine defaults instead of overriding them with ``null``.
        """
        result = {}

        for attr, _ in six.iteritems(self.model_types):
            value = getattr(self, attr)
            if value is None:
                continue
            if isinstance(value, (datetime.datetime, datetime.date)):
                result[attr] = value.isoformat()
            elif isinstance(value, list):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PdfMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
