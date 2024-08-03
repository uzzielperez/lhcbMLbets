import pandas as pd
import h5py
import pyarrow as pa
import pyarrow.parquet as pq

# File paths
#hdf5_file = '/Users/uzzielperez/Desktop/LHCbML/lhcbml/eleVsPho/elevspho/SingleElectronPt50_IMGCROPS_n249k_RHv1.hdf5'
hdf5_file = '/Users/uzzielperez/Desktop/LHCbML/lhcbml/eleVsPho/elevspho/SinglePhotonPt50_IMGCROPS_n249k_RHv1.hdf5'

parquet_file = 'SinglePhotonPt50_IMGCROPS_n249k_RHv1.parquet'

# Open the HDF5 file and read datasets
with h5py.File(hdf5_file, 'r') as hdf:
    # Assuming 'X' and 'y' are datasets in the HDF5 file
    X = hdf['X'][:]
    y = hdf['y'][:]

# Create a DataFrame
df = pd.DataFrame(X)
df['target'] = y

# Convert the DataFrame to a PyArrow Table
table = pa.Table.from_pandas(df)

# Write the table to a Parquet file
pq.write_table(table, parquet_file)

print(f"Converted {hdf5_file} to {parquet_file}")
