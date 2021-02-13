# News Collector

Program that will extract news from StudyIQ and manage acccording to their dates and tags in folders.

## Installation

Use the command.

```bash
git clone https://github.com/Khushiyant/News-Collector.git
```

## Usage

Just run the News_Collector.pyw or
```python
from News_Collector import scrappedData
import datetime

scrappedData("https://currentaffairs.studyiq.com/daily/",datetime.datetime.today().date()-datetime.timedelta(0))

```
Change timedelta parameters for definite date

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
