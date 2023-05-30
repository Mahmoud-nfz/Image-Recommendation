import os
import kaggle

# Set your Kaggle API credentials
kaggle.api.authenticate()

# Define the dataset and file details
dataset = 'paramaggarwal/fashion-product-images-dataset'
file_name = 'fashion-dataset/images/10000.jpg'

# Define the target directory
target_directory = './public/'

# Create the target directory if it doesn't exist
os.makedirs(target_directory, exist_ok=True)

# Set the target file path
target_file = os.path.join(target_directory, os.path.basename(file_name))

# Download the file to the target directory
kaggle.api.dataset_download_file(dataset, file_name, path=target_file)

# The file will be downloaded to the specified target directory
