import pandas as pd
import numpy as np

# Create synthetic dataset
np.random.seed(42)
data_size = 100

df = pd.DataFrame({
    'feature1': np.random.rand(data_size)*10,
    'feature2': np.random.rand(data_size)*50,
    'target': np.random.rand(data_size)*100
})

df.to_csv('data/dataset.csv', index=False)
print("Synthetic dataset created!")

