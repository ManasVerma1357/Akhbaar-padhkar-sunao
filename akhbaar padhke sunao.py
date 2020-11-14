''' 13.11.20
author-manas verma
akhbaar padhke sunao
'''


def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    import requests, json
    speak("news for today")
    url = ('https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=17a95ee85e8341479dee54d54b32a0f9')
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    for article in arts:
        speak(article['title'])
        print(article['title'])
        speak("Moving on to the next news..Listen Carefully")



