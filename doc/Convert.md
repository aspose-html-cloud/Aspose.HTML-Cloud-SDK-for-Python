## convert

General conversion function

Possible conversions: 
- HTML -> PDF, XPS, DOCX, MD, MHTML, JPEG, BMP, PNG, TIFF, GIF, WEBP
- EPUB -> PDF, XPS, DOCX, JPEG, BMP, PNG, TIFF, GIF, WEBP
- MD -> PDF, XPS, DOCX, HTML, MHTML, JPEG, BMP, PNG, TIFF, GIF, WEBP
- MHTML -> PDF, XPS, DOCX, JPEG, BMP, PNG, TIFF, GIF, WEBP
- SVG -> PDF, XPS, JPEG, BMP, PNG, TIFF, GIF, WEBP
- JPEG, BMP, PNG, TIFF, GIF -> SVG


### Parameters
| Parameter         | Type                                      | Description                                 |
|-------------------|-------------------------------------------|---------------------------------------------|
| **input_file**    | str                                       | Full path to the source file                |
| **output_file**   | str                                       | Full path to the output file with extension |
| **src_in_local**  | bool                                      | Source in the local disk                    |
| **dest_in_local** | bool                                      | Destination in the local disk               |
| **is_url**        | bool                                      | Source is URL                               |
| **options**       | [ConversionOptions](ConversionOptions.md) | Conversion options                          |
| **storage_name**  | str                                       | Storage name                                |
| **pdf_metadata**  | [PdfMetadata](PdfMetadata.md)             | PDF /Info metadata (only used when target is PDF) (optional) |

### 

### Convert html file in the local disk to pdf and save result to the local disk
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
    res = html_api.convert(input_file="c://test.html", output_file="c://test.pdf", src_in_local=True,
                                      dest_in_local=True, is_url=False, options=None, storage_name=None)
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
    res = html_api.convert(input_file=input_url, output_file="test.jpeg", src_in_local=False,
                                      dest_in_local=False, is_url=True, options=options, storage_name=None)
except ApiException as ex:
    print("Exception")
    print("Info: " + str(ex))
    raise ex

```

### Return value [ConversionResult](ConversionResult.md)