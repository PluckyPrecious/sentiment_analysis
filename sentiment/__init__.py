import azure.functions as func
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def main(req: func.HttpRequest) -> func.HttpResponse:
    analyzer = SentimentIntensityAnalyzer()
    text = req.params.get("text")
    scores = analyzer.polarity_scores(text)
    sentiment = "Yes! I'm a Pythonista and Loving it" if scores["compound"] > 0 else "negative"
    return func.HttpResponse(sentiment)