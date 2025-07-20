import kagglehub

# Download latest version
path = kagglehub.dataset_download("mdabbert/ultimate-ufc-dataset")

print("Path to dataset files:", path)