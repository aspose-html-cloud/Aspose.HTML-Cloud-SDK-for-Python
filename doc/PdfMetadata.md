## PdfMetadata

PDF document information (`/Info` dictionary) metadata applied to the produced
PDF file. Only meaningful when the conversion target format is **PDF**; the
server silently ignores it for other output formats.

Any field left as `None` is omitted from the request and the rendering engine
keeps its own default.

### Fields
| Field                 | Type              | PDF /Info key     | Engine default                          | Note     |
|-----------------------|-------------------|-------------------|-----------------------------------------|----------|
| **title**             | str               | /Title            | "Aspose"                                | Optional |
| **author**            | str               | /Author           | "Aspose"                                | Optional |
| **subject**           | str               | /Subject          | "Aspose"                                | Optional |
| **keywords**          | str               | /Keywords         | ""                                      | Optional |
| **creator**           | str               | /Creator          | "Aspose"                                | Optional |
| **producer**          | str               | /Producer         | "Aspose.HTML for .NET <version>"        | Optional |
| **creation_date**     | datetime or str   | /CreationDate     | Current timestamp                       | Optional |
| **modification_date** | datetime or str   | /ModDate          | Current timestamp                       | Optional |

### Example
```python
from datetime import datetime
from asposehtmlcloud.models.pdf_metadata import PdfMetadata

pdf_metadata = PdfMetadata(
    title="Monthly Report",
    author="Jane Doe",
    subject="Q3 Results",
    keywords="report, q3, pdf",
    creator="My Application",
    producer="My Company",
    creation_date=datetime(2024, 1, 15, 10, 30, 0),
    modification_date=datetime(2024, 6, 20, 18, 45, 0)
)
```

### Partial example (only some fields)
Unspecified fields keep engine defaults.

```python
from asposehtmlcloud.models.pdf_metadata import PdfMetadata

pdf_metadata = PdfMetadata(
    title="My Document",
    author="John Doe"
)
```

### Usage with conversion
```python
from asposehtmlcloud.api.html_api import HtmlApi
from asposehtmlcloud.models.pdf_metadata import PdfMetadata

html_api = HtmlApi(client)
pdf_metadata = PdfMetadata(title="My Document", author="John Doe")

html_api.convert_local_to_local(
    input_file="test.html",
    output_file="test.pdf",
    pdf_metadata=pdf_metadata
)
```
