import torch
from transformers import AutoTokenizer, BertForSequenceClassification

def load_polarity_model(model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = BertForSequenceClassification.from_pretrained(model_name)
    return tokenizer, model

def predict_polarity_from_text(text, tokenizer, model):
    inputs = tokenizer(text, return_tensors="pt")

    with torch.no_grad():
        logits = model(**inputs).logits

    predicted_class_id = logits.argmax().item()
    prediction = model.config.id2label[predicted_class_id]

    # 先在這邊處理 label(只為了比較好記)，之後可能會換地方。
    prediction = 'positive' if prediction == 'LABEL_1' else 'negative'

    return prediction

if __name__ == '__main__':
    tokenizer, model = load_polarity_model("textattack/bert-base-uncased-yelp-polarity")
    polarity_prediction = predict_polarity_from_text(input('Pleas Input A Sentence: '), tokenizer, model)
    print(polarity_prediction)