import scipy.sparse as sp
import pandas as pd

def load_dataframes():
    # Load the sparse matrix from the .npz file
    df = pd.read_csv("./data/" + "styles.csv", on_bad_lines="skip")
    print(df.head())

    df_embds = sp.load_npz('./data/sparse_matrix_df_embds_img.npz')

    # Access the matrix properties
    print('Shape:', df_embds.shape)
    print('Number of non-zero elements:', df_embds.nnz)

    return df,df_embds