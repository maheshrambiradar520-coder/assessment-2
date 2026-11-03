import os

os.environ.setdefault("NLTK_DATA", "./nltk_data")

from minicheck.minicheck import MiniCheck

if __name__ == "__main__":
    doc = "A group of students gather in the school library to study for their upcoming final exams."
    claims = [
        "The students are preparing for an examination.",
        "The students are on vacation.",
    ]
    scorer = MiniCheck(model_name="flan-t5-large", cache_dir="./ckpts")
    labels, probabilities, _, _ = scorer.score(docs=[doc, doc], claims=claims)
    print("Predicted labels:", labels)
    print("Support probabilities:", [round(float(p), 4) for p in probabilities])
