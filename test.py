import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Set your Kaggle API credentials

def fetch_image(image_name):
    api = KaggleApi()

    # Set your Kaggle API credentials (replace with your own)
    api.authenticate()

    # Define the dataset and file details
    dataset = 'paramaggarwal/fashion-product-images-dataset'
    file_name = 'fashion-dataset/images/'+image_name
    print(file_name)
    # return

    # Define the target directory
    target_directory = './public/'

    # Create the target directory if it doesn't exist
    os.makedirs(target_directory, exist_ok=True)

    # Set the target file path
    target_file = os.path.join(target_directory, os.path.basename(file_name))

    # Download the file to the target directory
    api.dataset_download_file(dataset, file_name, path=target_file)

    # The file will be downloaded to the specified target directory

fetch_image("10011.jpg")