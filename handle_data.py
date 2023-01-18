import os
import pandas as pd
from pathlib import Path
from pandas import read_csv

DATASETS = {
    "Soja Sample": "sample_pr_soja.csv",
    "Soja Clean Sample": "sample_pr_soja_clean.csv",
    "Feature Set": "feature_set.csv",
    "Train Set": "train.csv",
    "Test Set": "test.csv",
    "Results": "results.csv",
}


def path2data():
    return (
        Path(os.getenv("DATA")),
        Path(os.getenv("DATARAW")),
        Path(os.getenv("DATAPRD")),
    )


def load(dataset="Soja Sample", RAW=True):
    # TODO: enrich dictionary and make it into a function like path2dataset an imported constant
    file = DATASETS.get(dataset)
    _, RAW, PRD = path2data()
    if RAW is True:
        return read_csv(RAW / file)
    else:
        return read_csv(PRD / file)


def dump(data, dataset="Soja Clean Sample", PRD=True):
    file = DATASETS.get(dataset)
    _, RAW, PRD = path2data()
    data.to_csv(PRD / file, index=False)
