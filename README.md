# santander-cycles

This project makes use of Transport for London (TfL) open data to analyse Santander Cycle hire journeys across London.

## Data preparation

The first step is to download journey extracts from TfL's public-facing [S3 bucket](https://cycling.data.tfl.gov.uk/). TfL provides weekly extracts stretching back to January 2015 in csv format. The scrape_journey_extracts.py script uses [Boto](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html), the Amazon Web Services SDK for Python to scrape all csv files from the bucket.

The journey extract data does not contain spatial attributes; however, TfL provides the locations of all of its cycle docking stations through its [Unified API](https://tfl.gov.uk/info-for/open-data-users/unified-api). The get_bikepoints.py script queries the API using [urllib.request](https://docs.python.org/3/library/urllib.request.html) and forms the data into a Pandas dataframe before exporting to csv.

## Output

These two datasets can then be combined to get an idea of when and where cycle journeys are being taken across London. Currently, I have used Power BI to undertake some analysis of trends across time and produce a map of key docking stations. My next step is to use Uber's [kepler.gl](https://kepler.gl/) tool to render the map more efficiently.
