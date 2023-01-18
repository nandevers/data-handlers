import os
from multiprocessing import Pool

import dask.dataframe as dd
import openpyxl
import pandas as pd
import xlrd


class PandasMultiprocessingExcelReader:
    def __init__(self, path, processes=2):
        self.path = path
        self.processes = processes

    def read_excel(self, filename):
        return pd.read_excel(os.path.join(self.path, filename))

    def read_all(self):
        filenames = [f for f in os.listdir(self.path) if f.endswith('.xlsx')]
        with Pool(self.processes) as p:
            data = p.map(self.read_excel, filenames)
        return data


class OpenpyxlDaskExcelReader:
    def __init__(self, path):
        self.path = path

    def read_excel(self, filename):
        wb = openpyxl.load_workbook(os.path.join(self.path, filename))
        sheet = wb.active
        data = [[cell.value for cell in row] for row in sheet.rows]
        return data

    def read_all(self, filename=None):
        if filename is not None:
            if filename.endswith('.xlsx'):
                df = pd.DataFrame(self.read_excel(filename))
                return dd.from_pandas(df, npartitions=2)
            else:
                raise ValueError("The file should be an excel file with .xlsx extension")
        else:
            filenames = [f for f in os.listdir(self.path) if f.endswith('.xlsx')]
            data = []
            for f in filenames:
                df = pd.DataFrame(self.read_excel(f))
                data.append(dd.from_pandas(df, npartitions=2))
            return data


class XlrdDaskExcelReader:
    def __init__(self, path):
        self.path = path

    def read_excel(self, filename):
        with xlrd.open_workbook(os.path.join(self.path, filename)) as book:
            sheet = book.sheet_by_index(0)
            data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
        return data

    def read_all(self, filename=None):
        if filename is not None:
            if filename.endswith('.xlsx'):
                df = pd.DataFrame(self.read_excel(filename))
                return dd.from_pandas(df, npartitions=2)
            else:
                raise ValueError("The file should be an excel file with .xlsx extension")
        else:
            filenames = [f for f in os.listdir(self.path) if f.endswith('.xlsx')]
            data = []
            for f in filenames:
                df = pd.DataFrame(self.read_excel(f))
