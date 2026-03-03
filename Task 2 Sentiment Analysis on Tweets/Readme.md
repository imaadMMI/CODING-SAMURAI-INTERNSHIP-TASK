# Twitter Sentiment Analysis with RoBERTa

This project uses a specialized version of the **RoBERTa** (Robustly Optimized BERT Pretraining Approach) model, specifically fine-trained on 58 million tweets for sentiment classification. It categorizes text into three labels: **Negative**, **Neutral**, and **Positive**.

---

## 🚀 Features
* **Preprocessing:** Automatically handles social media noise by replacing `@mentions` with `@user` and URLs with `http`.
* **Transformer Power:** Utilizes the `cardiffnlp/twitter-roberta-base-sentiment` model from Hugging Face.
* **Probability Scoring:** Uses Softmax to provide a confidence score (0 to 1) for each sentiment category.



---

## 🛠️ Installation & Environment
Due to specific Windows dependency requirements and recent security patches for PyTorch (**CVE-2025-32434**), it is recommended to use **Conda**.

### 1. Create and Activate Environment
```bash
conda create -n codingsamurai python=3.10
conda activate codingsamurai
```
### 2. Install Core Dependencies
Note: PyTorch 2.6+ is required for safe model loading.
```bash
conda install pytorch>=2.6 cpuonly -c pytorch
pip install transformers scipy
```

### 💻 Usage
Run the script from your terminal:
```bash
python tw-sentiment.py
```

### How the Code Works:

* **Cleaning**: The raw tweet is split into words. If a word starts with @ or http, it is normalized to ensure the model isn't confused by specific usernames or unique URLs.
* **Tokenization**: The text is converted into a tensor of input_ids that represent the numerical patterns the model was trained on.
* **Inference**: The model processes the tensors and returns Logits (raw numerical output).
* **Softmax**: We apply the Softmax function to the logits:

<img width="292" height="84" alt="image" src="https://github.com/user-attachments/assets/018f5094-deff-4416-a88f-eaf7733b57d6" />

  This turns the raw scores into a probability distribution where the sum of all labels equals 1.0.
### 📊 Example Output
For the tweet: "@elonmusk I don't like this new twitter version! #failure 😡"

The output will look like:
```bash
Negative 0.9452
Neutral 0.0421
Positive 0.0127
```
