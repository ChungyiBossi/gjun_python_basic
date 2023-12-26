from transformers import AutoTokenizer, BertForMaskedLM
import torch

tokenizer = AutoTokenizer.from_pretrained("bert-base-chinese")
model = BertForMaskedLM.from_pretrained("bert-base-chinese")

inputs = tokenizer("巴黎是[MASK]国的[MASK]都。", return_tensors="pt")

with torch.no_grad():
    logits = model(**inputs).logits

# retrieve index of [MASK]
mask_token_index = (inputs.input_ids == tokenizer.mask_token_id)[0].nonzero(as_tuple=True)[0]
predicted_token_id = logits[0, mask_token_index].argmax(axis=-1)
probs, indices = torch.topk(torch.softmax(logits[0, mask_token_index], -1), 10) # 取得 [MASK] 的 topK預測
print("Prediction: ",tokenizer.decode(predicted_token_id))

for pred_tok_id in indices.tolist():
    pred_tokens = tokenizer.convert_ids_to_tokens(pred_tok_id)
    print(pred_tokens)
    for tok, prob in zip(pred_tokens, probs.tolist()[0]):
        print(tok, prob)