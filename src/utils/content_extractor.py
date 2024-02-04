import requests
from bs4 import BeautifulSoup

def get_website_content(url:str):
    """
    this function gets the textual content from the website
    """
    # get html content
    response = requests.get(url)
    response.raise_for_status()
    page_content = response.content
    soup = BeautifulSoup(page_content, "html.parser")

    # filter out using element name
    tagged_text = soup.find_all(['p','h1','h2','h3','li','tr','strong'])
    
    # as getting perfect hierarchy can be tricky, adding enough newlines helps in making sense between headings and its underlying content/list
    text_list=[]
    for i in tagged_text:
        if i.name=='p':
            txt=i.text+"\n"
            text_list.append(txt)
        elif i.name=='h2':
            txt="\n\n\n\n"+i.text+"\n"
            text_list.append(txt)
        elif i.name=='h3':
            txt=i.text+"\n\n"
            text_list.append(txt)
        elif i.name=='li':
            txt=i.text+"\n"
            text_list.append(txt)
        elif i.name=='tr':
            txt="\n"+i.text+"\n"
            text_list.append(txt)
        elif i.name=='strong':
            txt="\n\n"+i.text+"\n"
            text_list.append(txt)
        else:
            continue

    result_string = ''.join(text_list)
    return result_string