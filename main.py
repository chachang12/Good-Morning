from NotionApi import *
from MeteoWeatherApi import *
from Messaging import *
from datetime import date
import schedule
import time


def todaysUpdate():
    plist = []
    currentDate = date.today()

    pages = get_pages()
    for page in pages:
        page_id = page["id"]
        props = page["properties"]
        url = props["URL"]["title"][0]['text']['content']
        #url = url[0]['text']['content']
        title = props["Title"]["rich_text"][0]["text"]["content"]
        published = props["Published"]["date"]["start"]
        published = datetime.fromisoformat(published)
        plist.append([url, title, published_date])

    body = todaysWeather

    for p in plist:
        if p[3] == currentDate:
            body += f"{p[0]}, {p[1]}, Due: {p[2]}\n"
    
    
    sendMessage(body)

def main():

    schedule.every().day.at("09:00").do(todaysUpdate)
    while True:
        schedule.run_pending()
        time.sleep(1)    

    


if __name__ == "__main__":
    main()
    

