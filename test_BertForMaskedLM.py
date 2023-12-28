from transformers import AutoTokenizer, BertForMaskedLM
import torch

tokenizer = AutoTokenizer.from_pretrained("bert-base-chinese")
model = BertForMaskedLM.from_pretrained("bert-base-chinese")

print('tokens:', tokenizer.convert_ids_to_tokens(tokenizer("巴黎是[MASK]国的首都。").input_ids)) # 可以看一下切完的成果如何
inputs = tokenizer("巴黎是[MASK]国的首都。", return_tensors="pt") # 把句子切分成 wordpieces
with torch.no_grad():
    logits = model(**inputs).logits

# retrieve index of [MASK]
# 拆解下面這行
# mask_token_index = (inputs.input_ids == tokenizer.mask_token_id)[0].nonzero(as_tuple=True)[0]
x = (inputs.input_ids == tokenizer.mask_token_id) # 比較 tensor中是否與mask_token_id相等，是則為True, 反之False
print("Input_ids == mask_token_id: ", x)
y = x[0].nonzero(as_tuple=True) # 留下"非零的""index
print("Non-zero: ", y)
mask_token_index = y[0]
print("mask token id: ", mask_token_index)

# 拆解以下
# 取得第一名的[MASK]預測
predicted_token_id = logits[0, mask_token_index].argmax(axis=-1)
predicted_token = tokenizer.decode(predicted_token_id) # or tokenizer.convert_ids_to_tokens(predicted_token_id)
print('logit shape: ', logits.shape)
print('logit[0] shape: ', logits[0].shape)
print('logit[0, mask_token_index] shape: ', logits[0, mask_token_index].shape)
print('Predict [Mask] id: logit[0, mask_token_index].argmax(axis=-1):', logits[0, mask_token_index].argmax(axis=-1))
print('Predict [Mask] tok', tokenizer.convert_ids_to_tokens(logits[0, mask_token_index].argmax(axis=-1)))

# 拆解以下
# 取得前幾名的[MASK]預測
print("[MASK] logit:", logits[0, mask_token_index])
prediction_probability = torch.softmax(logits[0, mask_token_index], -1)
print("Prediction Prob:", prediction_probability)
topk_probs, topk_indices = torch.topk(prediction_probability, 3) # 取得 [MASK] 的 topK預測

print('topk probs: ', topk_probs)
print('topk indices: ', topk_indices, tokenizer.convert_ids_to_tokens(topk_indices[0]))


# Show result
for indice, prob in zip(topk_indices.tolist()[0], topk_probs.tolist()[0]):
    tok = tokenizer.convert_ids_to_tokens(indice)
    print(indice, tok, prob)