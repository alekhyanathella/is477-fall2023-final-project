# Import libraries
import requests
import hashlib
import os

# Dataset Urls
iris_url = 'https://archive.ics.uci.edu/static/public/53/iris.zip'

# Pre-computed Hash value
iris_hash = 'd11fe30213d36434a0879aab7cb00ce3c812eb7ba2495874438abff7b7b762e9'

iris_path = os.path.join('data','iris', 'iris.zip')

if os.path.exists(os.path.join('data', 'iris')) == False:
    os.makedirs('data/iris', exist_ok=True)

if os.path.exists(iris_path) == False:
    try:
        iris_response = requests.get(iris_url)
        with open(iris_path, mode='wb') as f:
            f.write(iris_response.content)
    except:
        raise Exception("Error Downloading Iris.zip")
else:
    with open(iris_path, mode='rb') as f:
        data = f.read()
        sha256hash = hashlib.sha256(data).hexdigest()
    if sha256hash == iris_hash:
        print("Iris.zip: Computed hash matches expected hash")
    else:
        raise Exception("Computed hash does not match expected hash for Iris.zip")
    