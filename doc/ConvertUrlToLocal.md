## convert_url_to_local

Convert a website to the local file.

Possible conversions: 
- URL -> PDF, XPS, DOCX, MD, MHTML, JPEG, BMP, PNG, TIFF, GIF, WEBP


### Parameters
| Parameter        | Type                                      | Description                             |
|------------------|-------------------------------------------|-----------------------------------------|
| **input_file**   | str                                       | Address of a website                    |
| **output_file**  | str                                       | Full path to output file with extension |
| **options**      | [ConversionOptions](ConversionOptions.md) | Conversion options (optional)           |
| **pdf_metadata** | [PdfMetadata](PdfMetadata.md)             | PDF /Info metadata (only used when target is PDF) (optional) |


### Convert a website to pdf and save result to the local file
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
    res = html_api.convertApi.convert_url_to_local(input_file=input_url, output_file="test.pdf")
except ApiException as ex:
    print("Exception")
    print("Info: " + str(ex))
    raise ex

```

### Convert a website to jpg with options and save result to the local file.
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
    'rightmargin': 20,
    'jpegquality': 95
}

try:
    input_url = 'https://stallman.org/articles/anonymous-payments-thru-phones.html'
    res = html_api.convertApi.convert_url_to_local(input_file=input_url, output_file="test.jpg",
                                                   options=options)
except ApiException as ex:
    print("Exception")
    print("Info: " + str(ex))
    raise ex

```

### Return value [ConversionResult](ConversionResult.md)