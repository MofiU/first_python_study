import requests

from lxml import html

# url = 'https://19-9.b.cdn13.com/008/022/8022442_hd.mp4?cdn_creation_time=1501937465&cdn_ttl=14400&cdn_bw=500k&cdn_bw_fs=660k&cdn_cv_data=198.71.235.18-dvp&cdn_hash=580cc176e1d193135b45935ce919d326'
# response = requests.get(url, stream=True)


headers = {
    # 'Cookie': 'stats_id=102058; first_visit=1500098656; prs=--; lang=en; __utmx=26208500.1AA9A6B4Q02NQCwITfCzaQ$0:0; __utmxx=26208500.1AA9A6B4Q02NQCwITfCzaQ$0:1500098735:8035200; _ga=GA1.2.1165501227.1500098705; _gid=GA1.2.1581390520.1501860795; stats_uid=5969b307cd4e-0632bc-33af24; stats_src=:1501860728:14; x_ndvkey=s%3A8%3A%2225b7cab1%22%3B; amplitude_idxhamster.com=eyJkZXZpY2VJZCI6ImYzNDU3MWRiLWU4MzEtNDFhZi1iOTY4LTQ3Y2JiNjYxM2FlYlIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTUwMTk0MDk4ODM4MiwibGFzdEV2ZW50VGltZSI6MTUwMTk0MjIwMTExNiwiZXZlbnRJZCI6NDksImlkZW50aWZ5SWQiOjAsInNlcXVlbmNlTnVtYmVyIjo0OX0=; x_viewes=a%3A7%3A%7Bi%3A0%3Bi%3A8029855%3Bi%3A1%3Bi%3A7950087%3Bi%3A2%3Bi%3A7970534%3Bi%3A3%3Bi%3A8051755%3Bi%3A4%3Bi%3A8050963%3Bi%3A5%3Bi%3A8071384%3Bi%3A6%3Bi%3A8076030%3B%7D; __atuvc=11%7C28%2C0%7C29%2C0%7C30%2C8%7C31; u-v-channels=0%3A148x25671; x_coutdated=true; _hjShownFeedbackMessage=true; stats_cnt=13; __atuvs=5985ce8b2ace9275002; UID=14278911; PWD=33f93a460453c236f4a8a4a81b2bc947e4593230',
    'Host': 'xhamster.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586',
}

response = requests.get(
    "https://xhamster.com/videos/next-door-milfs-from-the-uk-part-14-8053907",
    headers=headers)
#
xml = html.fromstring(response.content)

#
# get download link
# download_xml = xml.xpath("//a[@class='download-video']")
# for link in download_xml:
#     print(link.attrib)

#get video infomation

video_user = xml.xpath("//td[@id='videoUser']")[0]
#
#
#
# author = video_user.xpath("div[@class='item']/span[@class='hint']")[0]
# print(author.attrib)
#
#
# duration = video_user.xpath("div[@class='item']/span[@itemprop='duration']")[0]
# print(duration.attrib)
# print(duration.tail)
#
#
count = video_user.xpath("div[@class='item']/span[@itemprop='interactionCount']")[0]
print(count.attrib)
print(count.tail)



# get categories
#
# categories = xml.xpath("//td[@id='channels']")[0]
#
# links = categories.xpath("table/tr/td")[1]


# for link in links:
#     print(link.attrib)
#     if not link.xpath("i"):
#         print(link.text)
#     else:
#         print(link.xpath("i")[0].tail)

#
# response = requests.get(
#     "https://xhamster.com/",
#     headers=headers)
#
# xml = html.fromstring(response.content)


## get page size

# pages = xml.xpath("//div[@class='pager']/table/tr/td/div/a")
#
# max_size = pages[-2].text
# print(max_size)


# # get thumb image and visit link
#
#
# videos = xml.xpath("//div[@class='video']")

# for video in videos:
#     visit_link = video.xpath("a")[0]
#     video_name = visit_link.xpath('u')[0].text
#     thumb_image = visit_link.xpath("div[@class='thumb_container']/img")[0]
#     print(visit_link.attrib)
#     print(thumb_image.attrib)
    # print(video_name)

# response = requests.get("https://xhamster.com/movies/8076030/download/720p", headers=headers)

# print(response)
#
# with open('haha.html', 'wb') as out_file:
#     out_file.write(response.content)

# url = ''
#
# for resp in response.history:
#     if(resp.status_code == 307):
#         url = resp.headers['location']
#
#
# print(url)
# response = requests.get(url, stream=True)
# print(response.status_code)
# print(response.headers)
#
# file_size = response.headers['content-length']
# with open('haha.mp4', 'wb') as out_file:
#     # out_file.write(response.content)
#     sum  = 0
#     for chunk in response.iter_content(2048):
#         sum += 2048
#         out_file.write(chunk)
#         percantage = float(sum)/ float(file_size) * 100
#         if percantage >= 100:
#             print("download finish!")
#         else:
#             print("{0:.4f}%".format(percantage))
# del response