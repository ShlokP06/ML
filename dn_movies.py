import gdown
url = 'https://drive.google.com/file/d/11KO4iACgp0th-kmZFX-Hf-MYpV3LaEnB/view?usp=sharing'
gdown.download(url, "ratings.csv", quiet=False)
