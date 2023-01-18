import timeit
from data_ingestion import  OpenpyxlDaskExcelReader

path = "data/raw"

# Using Dask
reader = OpenpyxlDaskExcelReader(path)

def dask_reading():
    data = reader.read_all()

dask_time = timeit.timeit(dask_reading)

print("Dask time:", dask_time)
print("File size:", file_size/10**6, "MB")
