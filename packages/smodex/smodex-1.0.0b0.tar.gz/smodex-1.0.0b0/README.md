SMODEX Package: A Python package for understanding the evolution of soil moisture anomalies.
===============================================================================================


<!-- [![Build](ci_badge.svg)]() -->
[![License: MIT 0](https://img.shields.io/badge/license-MIT-blue)](https://opensource.org/license/mit-0/)
[![Coverage](https://img.shields.io/badge/coverage-62%25-red)](link_to_test_coverage_report)
[![Python](https://img.shields.io/badge/python-%3D%3E3.6-blue)](https://www.python.org/downloads/)
<!-- [![PEP8](https://img.shields.io/badge/code%20_style-pep8-orange)](https://peps.python.org/pep-0008/) -->
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Documentation](https://img.shields.io/badge/docs-passing-green)](readthedocs.io)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com)


SMODEX is a **package developed to enhance performant computation and understanding of the evolution of soil moisture and soil moisture anomalies using climate datasets.** 
It embraces the principles of FAIR and Open Science in the development of the computational workflow and the data sharing.



Announcements
=============
- **Release!** Version 1.1.0-alpha, October 25, 2023
- **The South Tyrol Free Software Conference (SFSCON)**: presentation on November 11, 2023 at SFSCON NOI Tech Park, Bolzano, Italy



Package Usage
=============
Soil moisture and soil moisture anomalies are critical markers of dryness and agricultural drought. The SMODEX package was designed to aid the performant of this metrics targeting the following categories of users:

1. **Researchers** working on the topics of soil moisture, drought and soil hydrology,
2. **Students** exploring tools for understanding the dynamics of soil moisture and soil hydrology,
3. **Open-source and Open-science scientists** looking for a wrapper to compute these specific anomalies



Installation
==================
The SMODEX package is compatible with Python 3.6+ and would be distributed through the _Python Package Index (PyPI)_ and can installed: 


```bash
pip install smodex
```



Usage examples
===============
Currently, the main subpackages in SMODEX include:
-- **sm_downloader**: contains a request to the ERA5 Climate Datastore for downloading and saving soil water contents based on the specified timeline necessary for computing an anomaly, 
-- **sm_climatology**: contains functionalities for computing soil moisture climatology with a given reference, and rolling mean at a monthly or dekadal scale,
-- **sm_anomaly**: contains functionalities for computing and saving soil moisture anomalies,
-- **sm_visualize**: contains different functionalities for visualizing the soil moisture and soil moisture anomalies across spatial and temporal dimensions (coming soon), 
-- **tests**: test for data handling, and computation moisture and moisture anomalies computation,
-- **docs**: readthedocs implementation



Download Module
---------------
You can use the `sm_downloader` with your python script or notebook this way:



```python 
from smodex import sm_downloader

download = sm_downloader.SMDownload(
    start_date='2020-05-05',
    end_date='2021-05-10',
    api="era5",
    area=[50.775, 2.775, 42.275, 18.025],
    depth=[1, 2, 3, 4],
    download_path= "./sm_downloaded/"
    )

download.downloader()

```



But note, for this module to work locally, you shold have the `ERA5 CDS API` installed on your machine. 
To do this, you simply run:


```bash 
pip install cdsapi
```
Additionally, create  an `.env` file and set:


```yaml
CDSAPI_URL=https://cds.climate.copernicus.eu/api/v2
CDSAPI_KEY=XXXXXX:XXXXXX-XXXXXX-XXXX-XXXXX
```
Remember to change the CDSAPI_KEY to that of your personal or organization's account keys.
You can find more specific details on how to access your personal CDS API key [here](https://cds.climate.copernicus.eu/api-how-to)


Other modules can also be imported and used by:


```python
import smodex
smodex.sm_downloader()
smodex.compute_climatology()
smodex.compute_anomalies()
```


Contributing
================

Currently, the SMODEX package is under development and we solicit the contribution of other developers to make a Merge/Pull Request using the development version on GitLab. You can clone the repository and install the pakcage using:

```bash 
python setup.py install
```

To make a merge/pull request for a major code change, open an issue to discuss what you'd like to change first. And tests your code changes locally with the pre-commit hooks specified before requesting a merge-request, which automatically triggers the execution of all the tests cases in the repo.


Contributors
------------

- [Rufai Omowunmi Balogun](https://rufaibalogun.com/)
- [Peter James Zellner](https://www.eurac.edu/en/people/peter-james-zellner)
- [Felix Greifeneder](https://www.linkedin.com/in/felix-greifeneder-1328216a/?originalSubdomain=it)



License
-------

[MIT](https://choosealicense.com/licenses/mit/)


External links
---------------
- [Documentation](smodex.readthedocs.org)
- [Soil Moisture Anomalies ADO Project](https://ado.eurac.edu/sma)
- [Soil Moisture Anomalies South Tyrol Use Case]()
