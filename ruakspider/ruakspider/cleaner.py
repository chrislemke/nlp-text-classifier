import re


def clean_up(text):
    text = text.replace(" ", " ")
    text = text.replace("–", "-")
    text = re.sub(r"[IVXLCDM]+\.", "", text)
    text = text.replace(" ,", ",")
    text = text.replace(" .", ".")
    text = text.replace(" ;", ";")
    text = re.sub(r"[^A-Za-z0-9äÄöÖüÜß\s\.\-\!\?\:\;\,]", "", text)
    text = text.replace("ä", "ae")
    text = text.replace("ö", "oe")
    text = text.replace("ü", "ue")
    text = text.replace("Ä", "Ae")
    text = text.replace("Ö", "Oe")
    text = text.replace("Ü", "Ue")
    text = text.replace("ß", "ss")
    text = re.sub(r" +", " ", text)
    text = text.replace("\n", " ")
    return text


def dta_clean_up(text):
    text = re.sub(r"\[(.*?)\]", "", text)
    text = re.sub(r"\((.*?)\)", "", text)
    text = re.sub(r"\*(.*?)\*", "", text)
    text = re.sub(r"_(.*?)_", "", text)
    text = re.sub(r"[^A-Za-z0-9äÄöÖüÜß\s\.\-\!\?\:\;\,]", " ", text)
    text = text.replace("ä", "ae")
    text = text.replace("ö", "oe")
    text = text.replace("ü", "ue")
    text = text.replace("Ä", "Ae")
    text = text.replace("Ö", "Oe")
    text = text.replace("Ü", "Ue")
    text = text.replace("ß", "ss")
    text = text.replace("\n", " ")
    text = re.sub(r" +", " ", text)
    return text


def wiki_clean_up(text):
    text = re.sub(r"\[[^]]*\]", "", text)
    text = re.sub(r"\((.*?)\)", "", text)
    return clean_up(text)


def philo_at_clean_up(text):
    texts = re.split(r"(\d +\.)?\sBibliographie(:|$)+\n", text)
    text = content_text(texts)
    texts = re.split(r"(\d+\.)?\sLiteraturverzeichnis(:|$)+\n", text)
    text = content_text(texts)
    texts = re.split(r"(\d+\.)?\sLiteratur(:|$)+\n", text)
    text = content_text(texts)
    text = re.sub(r"Seite\s\d{1,3}\n", "", text)
    text = re.sub(r"\_Seite\_\d", "", text)
    text = re.sub(r"\n+\d+\n", "", text)
    text = re.sub(r"[\d]+\.", " ", text)
    text = re.sub(r"\.+[\d]", " ", text)
    text = re.sub(r"[IVXLCDM]+\,", "", text)
    text = re.sub(r"\d{1,3}([a-zA-Z])", r"\g<1>", text)
    text = re.sub(r"\[(.*?)\]", "", text)
    text = re.sub(r"\((.*?)\)", "", text)
    text = re.sub(r"\*(.*?)\*", "", text)
    text = re.sub(r"_(.*?)_", "", text)
    text = re.sub(r"\b\d{1,3}\b", "", text)
    text = re.sub(r" +", " ", text)
    text = text.replace(", ,", ", ")
    text = clean_up(text)
    text = re.sub(r"(?<=[A-z])\-\s(?=(?!bzw|und|oder)[A-z])", "", text)
    text = re.sub(r" +", " ", text)
    return text


def content_text(texts):
    not_none_texts = []
    for text in texts:
        if text != None:
            not_none_texts.append(text)
    return max(not_none_texts, key=len)


def wiki_title_clean_up(text):
    text = text.replace("_-_Wikipedia", "")
    return title_clean_up(text)


def title_clean_up(text):
    text = re.sub(r"[^A-Za-z0-9äÄöÖüÜß\s.!?:;,–]", "", text)
    text = text.replace("ä", "ae")
    text = text.replace("ö", "oe")
    text = text.replace("ü", "ue")
    text = text.replace("Ä", "Ae")
    text = text.replace("Ö", "Oe")
    text = text.replace("Ü", "Ue")
    text = text.replace("ß", "ss")
    text = text.replace(" ", "_")
    return text
