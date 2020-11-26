import gdown
import time
# url = "https://drive.google.com/file/d/1RL582Pk80k4zjD_4zv5meSnqEN7F6ek7"...https://drive.google.com/uc?id=11ehkn33cmGFDDVuDAvjgjt8YW05Zbhp5"
print("starting")
time.sleep(100)
print("unslept")
gdown.download(url, "poetry.zip", quiet=False)
print('downloded')
