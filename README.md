# Service Chatbot using gRPC
Download checkpoint at [checkpoint drive](https://drive.google.com/drive/folders/1HhPKd6gpViJMw1IgSbLOpVtttjFLsOKi?usp=sharing). Remain 2 folder consisting `chatbot` and `vit5-base` in this drive. Add they into `model` folder as below.

## Structure of this service
```bash
chatbot_service
    ├── model
    │     ├── chatbot                 
    │     │      └── best_checkpoint.ckpt
    │     └── vit5-base                          
    │            ├── config.json                   
    │            ├── pytorch_model.bin
    │            ├── special_tokens_map.json
    │            ├── spiece.model
    │            ├── tokenizer_config.jso
    │            └── tokenizer.json
    │
    ├── client.py           
    ├── server.py
    └── pipeline.py
```
## Run server by localhost
1. Create conda env `conda create -n service python=3.9`
2. Activate conda env `conda activate service`
2. Install neccessary Python packages `pip install -r requirements.txt`
3. Run server `python server.py` on port `0.0.0.0:5002`
4. Run client `python client.py`
