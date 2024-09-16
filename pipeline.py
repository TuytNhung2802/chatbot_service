import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration
from flask import Flask, request, jsonify

app = Flask(__name__)

class ChatBot:
    def __init__(self, model_path, max_length=256):
        # self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.device = torch.device("cpu")
        self.model_path = model_path
        self.max_length = max_length
        self.tokenizer = T5Tokenizer.from_pretrained(model_path, legacy=False)
        self.model = self.__load_checkpoint(model_path)


    def __load_checkpoint(self, model_path):
        state_dict = torch.load("./model/chatbot/best_checkpoint.ckpt", map_location=self.device)['state_dict']
        new_state_dict = {}
        for k, v in state_dict.items():
            new_state_dict[k.replace('model.', '')] = v

        model = T5ForConditionalGeneration.from_pretrained(model_path)
        model.load_state_dict(new_state_dict, strict=True)
        return model.to(self.device).eval()


    def generate_answer(self, question):
        source_encoding = self.tokenizer(
            question,
            max_length=self.max_length,
            padding="max_length",
            truncation=True,
            return_tensors="pt",
        ).to(self.device)

        with torch.no_grad():
            generated = self.model.generate(
                input_ids=source_encoding["input_ids"],
                attention_mask=source_encoding["attention_mask"],
                max_length=100,
            )
            result = self.tokenizer.decode(generated[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)
        return result

    def __call__(self, question):
        return self.generate_answer(question)

model_path = "./model/vit5-base"
chatbot = ChatBot(model_path)
@app.route("/question-and-answer", methods=['GET'])
def hello_world():
    args = request.args
    question = args.get('question')
    result = chatbot(question)
    print(result)
    return result

if __name__ == '__main__':
    app.run(debug=False)