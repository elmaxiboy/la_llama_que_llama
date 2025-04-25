Easy implementation of tiny LLM that answers easy questions in a ChatGPT fashion, locally.

### Install llama.cpp:

```sh
git clone https://github.com/ggerganov/llama.cpp.git
sudo apt-get install cmake
sudo apt install libcurl4-openssl-dev
cmake -B build
cmake --build build
```

### Download pre-trained model

[Link to tiny llama model](https://cdn-lfs-us-1.hf.co/repos/6c/c2/6cc203a4b605b1f54529984e310dd5d122bd444bc30b4123a35527d02845d4cb/9fecc3b3cd76bba89d504f29b616eedf7da85b96540e490ca5824d3f7d2776a0?response-content-disposition=attachment%3B+filename*%3DUTF-8%27%27tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf%3B+filename%3D%22tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf%22%3B&Expires=1745585148&Policy=eyJTdGF0ZW1lbnQiOlt7IkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NTU4NTE0OH19LCJSZXNvdXJjZSI6Imh0dHBzOi8vY2RuLWxmcy11cy0xLmhmLmNvL3JlcG9zLzZjL2MyLzZjYzIwM2E0YjYwNWIxZjU0NTI5OTg0ZTMxMGRkNWQxMjJiZDQ0NGJjMzBiNDEyM2EzNTUyN2QwMjg0NWQ0Y2IvOWZlY2MzYjNjZDc2YmJhODlkNTA0ZjI5YjYxNmVlZGY3ZGE4NWI5NjU0MGU0OTBjYTU4MjRkM2Y3ZDI3NzZhMD9yZXNwb25zZS1jb250ZW50LWRpc3Bvc2l0aW9uPSoifV19&Signature=EP9EEcLawO18pimqMfilVlmEGpXZA2tfhgMa4PMNP6WxQyLRAfP%7Et91TSSCD%7Eb82i-GtPmk19PWcHM3Nw9t58m-abWmGJkbZaWnSfAfmK%7ERfC7oLIyJPivsHesbuOm76bhAqc1k1N96GCNY9f-LMJdNG8bi5C80n2r%7EPnLcWuCw8-AjVdmnpMxLmRxNSIS9AhRUj5Q5fOxcshcd-HHW7qys2zAVmoKa4M9f5P3JRj2WKLincjo8ItS0pgoNLnW%7EupIhm9SZfeLtjdaQ5fTtcR1UiwOyryEWXM5hfWAZCQZlaRUujkSu8%7E4P-ucoP-oKWUx-XHlZMahILvhn9nKKjpg__&Key-Pair-Id=K24J24Z295AEI9)

Move model to `llama.cpp/models` directory  

### Run the app
```sh
python app.py
```
Navigate to `localhost:5000` and "llama a la llama" 🦙