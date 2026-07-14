## convert_storage_to_local

Convert file in the storage to the local file.

Possible conversions: 
- HTML -> PDF, XPS, DOCX, MD, MHTML, JPEG, BMP, PNG, TIFF, GIF, WEBP
- EPUB -> PDF, XPS, DOCX, JPEG, BMP, PNG, TIFF, GIF, WEBP
- MD -> PDF, XPS, DOCX, HTML, MHTML, JPEG, BMP, PNG, TIFF, GIF, WEBP
- MHTML -> PDF, XPS, DOCX, JPEG, BMP, PNG, TIFF, GIF, WEBP
- SVG -> PDF, XPS, JPEG, BMP, PNG, TIFF, GIF, WEBP
- JPEG, BMP, PNG, TIFF, GIF -> SVG

### Parameters
| Parameter        | Type                                      | Description                             |
|------------------|-------------------------------------------|-----------------------------------------|
| **input_file**   | str                                       | Full path in the storage to input file  |
| **output_file**  | str                                       | Full path to output file with extension |
| **storage_name** | str                                       | User's storage name. None if default    |
| **options**      | [ConversionOptions](ConversionOptions.md) | Conversion options (optional)           |
| **pdf_metadata** | [PdfMetadata](PdfMetadata.md)             | PDF /Info metadata (only used when target is PDF) (optional) |

### 

### Convert html file in the storage to pdf and save result to the local file
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
    res = html_api.convert_storage_to_local(input_file="test.html", output_file="test.jpg", storage_name=None)
except ApiException as ex:
    print("Exception")
    print("Info: " + str(ex))
    raise ex

```

### Convert html file in the storage to jpeg with options and save result to local file.
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
    res = html_api.convert_storage_to_local(input_file="test.html", output_file="test.jpeg",
                                                       storage_name=None, options=options)
except ApiException as ex:
    print("Exception")
    print("Info: " + str(ex))
    raise ex

```

### Return value [ConversionResult](ConversionResult.md)