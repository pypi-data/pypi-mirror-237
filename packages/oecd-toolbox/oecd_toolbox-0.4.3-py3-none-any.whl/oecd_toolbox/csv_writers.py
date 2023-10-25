import csv
import ujson as json
from pathlib import Path
from typing import Any, Callable, Iterable, List, Literal, Optional, Tuple, Iterator, Union
from dbnomics_data_model.observations import Frequency, detect_period_format_strict, period_format_strict_regex_list
from oecd_toolbox.converters import SimpleConverter
from dbnomics_fetcher_toolbox.resources import Resource
from slugify import slugify
import re
import daiquiri
import pandas as pd

logger = daiquiri.getLogger(__name__)


class FileResource(Resource):
    """ A resource-type consisting of a single downloadable file, identified by a URL
    and a target path where it should be deposited.
    """
    targetDataset: Path
    sourceFolder: Path
    fileToProcess: str
    query: Union[str, None] = None  # '.TOVT+TOVV.G46+G47..I15.'
    targetFreq: Union[Literal["M", "Q", "A"], None] = None  # (DataCapture target frequencies M|Q|A)
    fAggregator: Union[Callable[[Iterable], Any], None] = None  # e.g. pd.DataFrame.mean
  
    def delete(self):
        """ Deletes the local representation of a dataset including its containing folder. """
        for f in self.targetDataset.glob('*.*'):
            f.unlink()
        self.targetDataset.rmdir
    
    def __str__(self) -> str:
        return f'target ds: {self.targetDataset}, source fold: {self.sourceFolder}, file: {self.fileToProcess}, filter: {self.query}'


class DataCaptureConverter(SimpleConverter):
    ''' A converter to create DataCapture ready files from DbNomics jsonl files for an entire project.'''
    def prepare_resources(self) -> Iterator[Resource]:
        # print('Create an iterator of resources - can be a similar function outside of a subclass')
        
        for f in self.source_dir.rglob('series.jsonl'):
            dirPath = f.parents[0]
            fileName = f.name
            relDirPath = dirPath.relative_to(self.source_dir)
            did = slugify(str(relDirPath))
            yield FileResource(id=did, sourceFolder=dirPath, targetDataset=self.target_dir / relDirPath, fileToProcess=fileName)
            
    def process_single_resource(self, res: Resource):
        if not res.targetDataset.exists():
            res.targetDataset.mkdir(parents=True)
        series_jsonl_to_DataCapturecsv(res.sourceFolder / res.fileToProcess, Path(res.targetDataset / res.fileToProcess).with_suffix('.csv'))


class DataCaptureConverterWithRegex(SimpleConverter):
    ''' A converter to create DataCapture ready files from DbNomics jsonl files for an entire project.
        params should be provided as a list of tuples to prepare_resources (datasetID, regexFilter on codes)
    '''
    
    def prepare_resources(self, params: list) -> Iterator[Resource]:
        # print('Create an iterator of resources - can be a similar function outside of a subclass')
        
        for dirPath, filter in params:
            did = slugify(str(dirPath))
            yield FileResource(
                id=did,
                sourceFolder=self.source_dir / dirPath,
                targetDataset=self.target_dir / dirPath,
                fileToProcess='series.jsonl',
                query=filter
            )

    def process_single_resource(self, res: Resource):
        if not res.targetDataset.exists():
            res.targetDataset.mkdir(parents=True)
        series_jsonl_to_DataCapturecsv(
            res.sourceFolder / res.fileToProcess,
            Path(res.targetDataset / res.fileToProcess).with_suffix('.csv'),
            get_pattern_from_query(res.query)
        )


class DataCaptureConverterWithRegexAndAggregator(SimpleConverter):
    ''' A converter to create DataCapture ready files from DbNomics jsonl files for an entire project.
        params should be provided as a list of tuples to prepare_resources (datasetID, regexFilter on codes, target frequency, aggregator function)
    '''
    
    def prepare_resources(self, params: list) -> Iterator[Resource]:
        # print('Create an iterator of resources - can be a similar function outside of a subclass')
        
        for dirPath, filter, freq, func in params:
            did = slugify(str(dirPath))
            yield FileResource(
                id=did,
                sourceFolder=self.source_dir / dirPath,
                targetDataset=self.target_dir / dirPath,
                fileToProcess='series.jsonl',
                query=filter,
                targetFreq=freq,
                fAggregator=func
            )

    def process_single_resource(self, res: Resource):
        if not res.targetDataset.exists():
            res.targetDataset.mkdir(parents=True)
        series_jsonl_to_DataCapturecsv(
            res.sourceFolder / res.fileToProcess,
            Path(res.targetDataset / res.fileToProcess).with_suffix('.csv'),
            get_pattern_from_query(res.query),
            get_frequency_from_query(res.targetFreq),
            res.fAggregator
        )

#----------------------series_jsonl conversions----------------------
def obslist_to_csv(target_file: Path, obslist: List[dict]):
    """ Write to csv and observations list of dictionaries
        Fieldnames are inferred from the first observation
    """
    with open(target_file, 'w', encoding="UTF-8", newline='') as csvfile:   
            fieldnames = list(obslist[0].keys())
            writer = csv.DictWriter(f=csvfile, fieldnames=fieldnames, extrasaction='ignore')
            writer.writeheader()
            for data in obslist[1:]:
                writer.writerow(data)

def series_jsonl_to_csv(source_file: Path):
    """ Simple generic csv flavour of the convertor. """
    L=[]
    with open(source_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            series = json.loads(line)
            for obs in series['observations'][1:]:
                dim_dict = dict()
                dim_dict['code'] = series['code']
                dim_dict['PERIOD'] = obs[0]
                for c, v in enumerate(series['observations'][0][1:]):
                        dim_dict[v] = obs[c+1]
                L.append(dim_dict)

    if not L:
        logger.debug('empty observations list')
    else:
        obslist_to_csv(target_file='series.csv', obslist=L)       


DC_eligible_frequencies = [Frequency.ANNUAL, Frequency.QUARTERLY, Frequency.MONTHLY, Frequency.BI_ANNUAL]
DC_eligible_frequency_codes = [f.to_dimension_code() for f in DC_eligible_frequencies]


def series_jsonl_to_DataCapturecsv(source_file: Path, target_file: Path, regex: Union[re.Pattern, None] = None, target_freq: Union[Frequency, None] = None, f_aggregation: Union[Callable[[Iterable], Any], None] = None):
    """ DataCapture csv flavour of the convertor. """
    L=[]
    sm = None
    with open(source_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            series = json.loads(line)
            if regex:
                sm = regex.match(series['code'])
                if not sm: 
                    logger.debug(f'series {series["code"]} skipped, not matching regex') 
            
            if sm or not regex:        
                if isinstance(series['dimensions'], list):
                    series_freq = series['dimensions'][0]
                elif isinstance(series['dimensions'], dict):
                    series_freq = series['dimensions']['FREQ']

                if series_freq in DC_eligible_frequency_codes:
                    columns = ['code', 'year', 'freq'] + series['observations'][0]
                    for obs in series['observations'][1:]:
                        dim_dict=dict.fromkeys(columns, "NA")
                        dim_dict['code'] = series['code']
                        dim_dict['year'], dim_dict['freq'], dim_dict['PERIOD'] = get_DC_compatible_date(obs[0])
                        for c, v in enumerate(series['observations'][0][1:]):
                            dim_dict[v] = obs[c+1]
                        L.append(dim_dict)
                        
                elif target_freq and f_aggregation and (target_freq in DC_eligible_frequencies):
                    columns = ['code', 'year', 'freq'] + series['observations'][0]
                    df = pd.DataFrame(data=series['observations'][1:],columns=series['observations'][0]) 
                    # this only aggregates values, but omits observation attributes that might be in the original file                   
                    df_new_freq = df.groupby(pd.PeriodIndex(df['PERIOD'], freq=target_freq.to_dimension_code()))['VALUE'].apply(f_aggregation)
                    for ind in df_new_freq.index:
                        dim_dict=dict.fromkeys(columns, "NA")
                        dim_dict['code'] = series['code']
                        dim_dict['year'], dim_dict['freq'], dim_dict['PERIOD'] = get_DC_compatible_date_pandas(ind)
                        dim_dict['VALUE'] = df_new_freq[ind]
                        L.append(dim_dict)
    
    obslist_to_csv(target_file=target_file, obslist=L)

def get_DC_compatible_date(period: str) -> Optional[Tuple[int, str, int]]:
    """Return a tuple of (year, frequency_code, period_withinyear) or `None` if unable to detect.

    # Working examples:
    >>> get_DC_compatible_date("2014")
    2014, Y, 1 
    >>> get_DC_compatible_date("2014-S1")
    2014, Q, 2
    >>> get_DC_compatible_date("2014-Q1")
    2014, Q, 1 
    >>> get_DC_compatible_date("2014-01")
    2014, M, 1

    # Invalid formats:
    >>> detect_period_format_strict("ABCDE")
    >>> detect_period_format_strict("2014Z01")
    """
    
    freq = detect_period_format_strict(period)
    if freq in DC_eligible_frequencies:
        for period_format, regex in period_format_strict_regex_list: 
            if freq == period_format:
                m = regex.match(period)
                if freq == Frequency.ANNUAL:
                    return int(m.group(1)), "Y", 1
                elif freq == Frequency.BI_ANNUAL:
                    return int(m.group(1)), "Q", int(m.group(2)) * 2
                else:
                    return int(m.group(1)), freq.to_dimension_code(), int(m.group(2))
    return None

def get_DC_compatible_date_pandas(period: pd.Period) -> Optional[Tuple[int, str, int]]:
    """Return a tuple of (year, frequency_code, period_withinyear) or `None` if unable to detect.

    # Working examples:
    >>> get_DC_compatible_date("2014")
    2014, Y, 1 
    >>> get_DC_compatible_date("2014-Q1")
    2014, Q, 1 
    >>> get_DC_compatible_date("2014-01")
    2014, M, 1

    # Invalid formats:
    >>> detect_period_format_strict("ABCDE")
    >>> detect_period_format_strict("2014Z01")
    """
    
    freq = period.freqstr[0]
    if freq in DC_eligible_frequency_codes:
        if freq == 'A':
            return period.year, 'Y', 1
        elif freq == 'Q':
            return period.year, 'Q', period.quarter
        else:
            return period.year, 'M', period.month
    return None

    
def get_pattern_from_query(query: Union[str, None]) -> re.Pattern:
    """ Working example: 
    >>> get_pattern_from_query('.TOVT+TOVV.G46+G47..I15.')
    ^.+\.(TOVT|TOVV)\.(G46|G47)\..+\.(I15)\..+$
    """ 
    if not query:
        return re.compile(r'.*') 
    
    seq = query.split('.')
    reseq = []
    for s in seq:
        if s == '':
            reseq.append(r'.+')
        else:
            plus_to_or = '(' + s.replace('+','|') + ')'
            reseq.append(plus_to_or)

    return re.compile(r'^'+r'\.'.join(reseq)+r'$')

def get_frequency_from_query(freq: Union[Literal["M","Q","A"], None]) -> Frequency:
    if freq == 'M':
        return Frequency.MONTHLY
    elif freq == 'Q':
        return Frequency.QUARTERLY
    elif freq == 'A':
        return Frequency.ANNUAL
    else:
        return None
