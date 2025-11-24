from sklearn.preprocessing import StandardScaler, OneHotEncoder, FunctionTransformer, PowerTransformer
import numpy as np 
import pandas as pd 

drop_columns_enc = ['payment_type_AB', 'payment_type_AD', 'payment_type_AE', 'employment_status_CG', 'housing_status_BG', 'device_os_x11']

def drop_func(df):
    df.columns = [col.split("__")[-1] for col in df.columns ]
    return df.drop(drop_columns_enc, axis =1, errors="ignore")

dropper = FunctionTransformer(drop_func)

# Convert every column to float32
def to_float32(X):
    if isinstance(X, pd.DataFrame):
        return X.astype(np.float32)
    return X.astype(np.float32)

cast_float32 = FunctionTransformer(to_float32, feature_names_out='one-to-one')