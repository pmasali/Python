import urllib.request
import urllib.parse
import urllib.error
import requests
from bs4 import BeautifulSoup
import json
import random
import ssl
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def grey_color_func(word, font_size, position, orientation, random_state=None,**kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

def main(url):

    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,'html.parser')
    script = soup.find('script', text = lambda t:t.startswith('window._sharedData'))
    page_json = script.text.split(' = ', 1)[1].rstrip(';')
    data = json.loads(page_json)
    loc_array = []
    loc_dict = dict()
    # print(data)
    for post in data['entry_data']['ProfilePage']:
        print('-------------------------------------------------')
        user = post['graphql']['user']['full_name']
        print('Profile of',user)
        print('-------------------------------------------------')
    for loc_src in post['graphql']['user']['edge_owner_to_timeline_media']['edges']:
        if loc_src['node']['location'] is None:
            loc_src['node']['location'] = ssl.PROTOCOL_SSLv23
        else: 
            loc_src_name = loc_src['node']['location']['name']
            loc_array.append(loc_src_name)
    for i in loc_array:
        loc_dict[i] = loc_dict.get(i,0) + 1
    print(loc_dict)

    wc = WordCloud(min_font_size = 5,font_step = 3, width = 400, height = 200, max_words = 15, random_state=1, margin=10).generate_from_frequencies(loc_dict)
    plt.title('Instagram Image Locations of {}'.format(user))
    plt.imshow(wc.recolor(color_func=grey_color_func, random_state=3),interpolation="bilinear")
    plt.axis('off')
    plt.legend(loc_dict)
    plt.show()
    plt.close()

if __name__ == '__main__':
    url = input('Enter the profile link for Word Cloud of location:')
    main(url)