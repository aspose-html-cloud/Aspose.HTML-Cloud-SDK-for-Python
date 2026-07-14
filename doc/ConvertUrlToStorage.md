## convert_url_to_storage

Convert a website to a file in the storage.

Possible conversions: 
- URL -> PDF, XPS, DOCX, MD, MHTML, JPEG, BMP, PNG, TIFF, GIF, WEBP

### Parameters
| Parameter        | Type                                      | Description                             |
|------------------|-------------------------------------------|-----------------------------------------|
| **input_file**   | str                                       | Address of a website                    |
| **output_file**  | str                                       | Full path to output file with extension |
| **storage_name** | str                                       | User's storage name. None if default    |
| **options**      | [ConversionOptions](ConversionOptions.md) | Conversion options (optional)           |
| **pdf_metadata** | [PdfMetadata](PdfMetadata.md)             | PDF /Info metadata (only used when target is PDF) (optional) |

### 

### Convert website to pdf and save result to the storage
```python
from asposehtmlcloud.configuration import Configuration
from asposehtmlcloud.api.html_api import HtmlApi
from asposehtmlcloud.api_client import ApiClient as Client
from asposehtmlcloud.rest import ApiException

configuration = Configuration(apiKey="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                              appSid="XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
                              basePath="https://api.aspose.cloud/v4.0",
                              authPath="https://api.aspose.cloud/connect/token",
                              debug=True)
client = Client(configuration)
html_api = HtmlApi(client)

try:
    input_url = 'https://stallman.org/articles/anonymous-payments-thru-phones.html'
    res = html_api.convertApi.convert_url_to_storage(input_file=input_url, output_file="test.jpg",
                                                     storage_name=None)
except ApiException as ex:
    print("Exception")
    print("Info: " + str(ex))
    raise ex

```

### Convert a website to jpeg with options and save result to the storage.
```python
from asposehtmlcloud.configuration import Configuration
from asposehtmlcloud.api.html_api import HtmlApi
from asposehtmlcloud.api_client import ApiClient as Client
from asposehtmlcloud.rest import ApiException

configuration = Configuration(apiKey="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                              appSid="XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
                              basePath="https://api.aspose.cloud/v4.0",
                              authPath="https://api.aspose.cloud/connect/token",
                              debug=True)
client = Client(configuration)
html_api = HtmlApi(client)

options = {
    'width': 600,
    'height': 900,
    'topmargin': 20,
    'bottommargin': 20,
    'leftmargin': 20,
    'rightmargin': 20
}

try:
    input_url = 'https://stallman.org/articles/anonymous-payments-thru-phones.html'
    res = html_api.convertApi.convert_url_to_storage(input_file=input_url, output_file="test.jpeg",
                                                     storage_name=None, options=options)
except ApiException as ex:
    print("Exception")
    print("Info: " + str(ex))
    raise ex

```

### Return value [ConversionResult](ConversionResult.md)