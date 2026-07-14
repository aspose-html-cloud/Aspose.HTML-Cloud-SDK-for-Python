## convert_local_to_local

Convert the file that is placed in the local directory to the local file.

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
| **input_file**   | str                                       | Full path to input file for conversion  |
| **output_file**  | str                                       | Full path to output file with extension |
| **options**      | [ConversionOptions](ConversionOptions.md) | Conversion options (optional)           |
| **pdf_metadata** | [PdfMetadata](PdfMetadata.md)             | PDF /Info metadata (only used when target is PDF) (optional) |


### Convert html file to pdf
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
    res = html_api.convert_local_to_local(input_file="test.html", output_file="test.pdf")
except ApiException as ex:
    print("Exception")
    print("Info: " + str(ex))
    raise ex

```

### Convert local html file to jpg with options and save result to the local file.
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
    res = html_api.convert_local_to_local(input_file="test.html", output_file="test.jpg", options=options)
except ApiException as ex:
    print("Exception")
    print("Info: " + str(ex))
    raise ex

```

### Return value [ConversionResult](ConversionResult.md)