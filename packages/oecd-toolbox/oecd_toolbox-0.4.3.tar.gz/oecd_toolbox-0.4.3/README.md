# OECD Toolbox
A library of abstract classes that can serve as a skeleton for writing downloaders and converters for DbNomics style fetchers.
Additionally it contains utility/helper functions to handle common operations or transformations in both the downloading and conversion process. 

## Installation
To install the package - proceed the usual way:
```powershell
pip install oecd_toolbox
```
or if you have it installed already, upgrade:
```powershell
pip install oecd_toolbox --upgrade
```


## Build the project

To build the project, after changes, make sure the version number in _setup.cfg_ is updated.
Then issue the following command:

```powershell
python -m build
```


## Publish the project on pypi.org
WARNING!!! make sure no confidential data is stored in the published package

The package is published on pypi.org. Manually manage the available variants of the package [here](https://pypi.org/manage/project/oecd-toolbox/releases/).
Access details are stored in the Practices teams access details store.

To push the distributions that are available in the toolbox's _dist_ folder use twine with the commandline:

```powershell
twine upload dist/*
```

## DataCapture conversions

NEW in version 0.3.27 of the toolbox - the package includes a converter to generate DataCapture style csvs. To use this new converter copy into your fetcher project the 'tests\datacapture-postprocessor.py' file or just its contents (below). 

```python
import asyncio
import sys
from oecd_toolbox import csv_writers as lbc

def main():
  
    cnvtr = lbc.DataCaptureConverter()
    cnvtr.init_arguments_and_logging()
    asyncio.run(cnvtr.convert_resources(cnvtr.prepare_resources(), cnvtr.process_single_resource))

if __name__ == "__main__":
    sys.exit(main())
```

In order to run the conversion from jsonl files use the following powershell command assuming that you have already created a folder \<projectname-datacapture-data\> to recieve your csv files:

``` powershell
python datacapture-postprocessor.py <path-to\projectname-json-data> <path-to\projectname-datacapture-data> --force
```

A similar command could be added to the postprocessor in the continouous integration pipeline. The usual behaviour modifiers [--only --except --limit] are available.

NEW in version 0.4.0 beyond the basic converter two new converter flavours are available:
- **DataCaptureConverterWithRegex** can filter series from a resource, so that the conversion is lighter both in used resources and resulting file (filtering is based on an SDMX webservice like syntax - dots for dimension separators, '+' to connect eligible dimension members, empty position allows all members) The above sample code adapted:
    ```python
    def main():
        filterset = [
            ('sts_trtu_m', '.TOVT+TOVV.G46+G47..I15.'),
            ('prc_hicp_ctrb', '.I15+INX_A_AVG+RCH_A+RCH_A_AVG+RCH_M..CP00+CP01+CP02+CP03+CP04+CP041+CP043+CP044+CP045')
        ]

        cnvtr = lbc.DataCaptureConverterWithRegex()
        cnvtr.init_arguments_and_logging()
        asyncio.run(cnvtr.convert_resources(cnvtr.prepare_resources(filterset), cnvtr.process_single_resource))
    ```

- **DataCaptureConverterWithRegexAndAggregator** can handle frequency aggregations, it is sufficient to provide a target frequency from the list ['M','Q','A'] and an aggregator function (pandas-style) 

    ```python
    def main():
        filterset = [
            ("MMSD008A", None, "M", pd.DataFrame.mean),
            ("MMSD402A", None, "A", pd.DataFrame.median)
        ]

        cnvtr = lbc.DataCaptureConverterWithRegexAndAggregator()
        cnvtr.init_arguments_and_logging()
        asyncio.run(cnvtr.convert_resources(cnvtr.prepare_resources(filterset), cnvtr.process_single_resource))
    ```

## Common behaviour modifiers 

All fetcher components that adopt the toolbox inherit some behaviour modifiers from the underlying toolbox. These command line arguments can be used to modify how the programs iterate through `resources`:

- removing the excluded ones if the `--exclude` option is used; provide a space separated list of resource IDs
- keeping only some of them if the `--only` option is used; provide a space separated list of resource IDs 
- processing a limited number of resources if the `--limit` option is used; provide an integer after  the argument 

By default resources that were already processed with a ``SUCCESS`` or ``FAILURE`` status will not be processed again.
If the option ``--retry-failed`` is used, resources with FAILURE status will be retried.
If the option ``--force`` is used, process all resources. !!! This is often needed if the status log is not cleared after each execution.

The basic behaviour of the iterator will call ``process_resource(resource)``, logging messages, allowing
to track the processing progress. If an exception is raised during the execution of ``process_resource``:

- log the error and process the next resource, or re-raise if ``--fail-fast`` option is used
- call ``resource.delete()`` if ``--delete-on-error`` option is used





