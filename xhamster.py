import requests
from lxml import html
from peewee import *
import re
from datetime import datetime

db = MySQLDatabase(host='localhost', port=3306, user='bo.zeng', passwd='123456', database='xhamster')
db.connect()


class BaseModel(Model):

    class Meta:
        database = db


class Video(BaseModel):
    name = CharField()
    duration = CharField(null=True)
    view_value = IntegerField(null=True)
    created_at = DateTimeField(null=True)
    visit_link = CharField()


class Image(BaseModel):
    src = CharField(unique=True)
    video = ForeignKeyField(Video, to_field="id")


class DownloadLink(BaseModel):
    quality = CharField()
    src = CharField(unique=True, max_length=3000)
    video = ForeignKeyField(Video, to_field="id")


class Tag(BaseModel) :
    name = CharField(unique=True)


class VideoTag(BaseModel):
    video = ForeignKeyField(Video, to_field="id")
    tag = ForeignKeyField(Tag, to_field="id")

if not Video.table_exists():
    Video.create_table()

if not Image.table_exists():
    Image.create_table()


if not DownloadLink.table_exists():
    DownloadLink.create_table()

if not Tag.table_exists():
    Tag.create_table()

if not VideoTag.table_exists():
    VideoTag.create_table()


headers = {
    'Host': 'xhamster.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586',
}

cookie = {'Cookie': 'stats_id=102058; first_visit=1500098656; prs=--; lang=en; __utmx=26208500.1AA9A6B4Q02NQCwITfCzaQ$0:0; __utmxx=26208500.1AA9A6B4Q02NQCwITfCzaQ$0:1500098735:8035200; _ga=GA1.2.1165501227.1500098705; _gid=GA1.2.1581390520.1501860795; stats_uid=5969b307cd4e-0632bc-33af24; stats_src=:1501860728:14; x_ndvkey=s%3A8%3A%2225b7cab1%22%3B; amplitude_idxhamster.com=eyJkZXZpY2VJZCI6ImYzNDU3MWRiLWU4MzEtNDFhZi1iOTY4LTQ3Y2JiNjYxM2FlYlIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTUwMTk0MDk4ODM4MiwibGFzdEV2ZW50VGltZSI6MTUwMTk0MjIwMTExNiwiZXZlbnRJZCI6NDksImlkZW50aWZ5SWQiOjAsInNlcXVlbmNlTnVtYmVyIjo0OX0=; x_viewes=a%3A7%3A%7Bi%3A0%3Bi%3A8029855%3Bi%3A1%3Bi%3A7950087%3Bi%3A2%3Bi%3A7970534%3Bi%3A3%3Bi%3A8051755%3Bi%3A4%3Bi%3A8050963%3Bi%3A5%3Bi%3A8071384%3Bi%3A6%3Bi%3A8076030%3B%7D; __atuvc=11%7C28%2C0%7C29%2C0%7C30%2C8%7C31; u-v-channels=0%3A148x25671; x_coutdated=true; _hjShownFeedbackMessage=true; stats_cnt=13; __atuvs=5985ce8b2ace9275002; UID=14278911; PWD=33f93a460453c236f4a8a4a81b2bc947e4593230' }
headers_with_cookie = {**headers, **cookie}


# get all video info form xhamster

response = requests.get(
    "https://xhamster.com/",
    headers=headers)
xml = html.fromstring(response.content)

# get paging max size
pages = xml.xpath("//div[@class='pager']/table/tr/td/div/a")
max_size = int(pages[-2].text)

for i in list(range(1, 2)):
    single_page_url = "https://xhamster.com/new/" + str(i) + ".html"
    print(single_page_url)
    single_response = requests.get(single_page_url, headers=headers)
    single_xml = html.fromstring(single_response.content)
    videos = xml.xpath("//div[@class='video']")
    for video in videos:
        # 3.get video name ,thumb image source and visit path
        visit_link = video.xpath("a")[0]
        visit_link_href = visit_link.attrib['href']
        thumb_image_src = visit_link.xpath("div[@class='thumb_container']/img")[0].attrib['src']
        video_name = visit_link.xpath('u')[0].text
        duration = visit_link.xpath('b')[0].text
        finger_rate = video.xpath("div[@class='hRate']/div")[0].text
        view_value = int(re.sub(',', '', video.xpath("div[@class='hRate']/div")[1].text))

        # get video detail information
        video_response = requests.get(visit_link_href, headers=headers)
        video_xml = html.fromstring(video_response.content)
        video_user = video_xml.xpath("//td[@id='videoUser']")[0]

        # get created_at
        author = video_user.xpath("div[@class='item']/span[@class='hint']")[0]
        created_at = datetime.strptime(author.attrib['hint'], '%Y-%m-%d %H:%M:%S %Z')

        # create video
        video, _ = Video.get_or_create(name=video_name, visit_link=visit_link_href)
        video.view_value = view_value
        video.duration = duration
        video.save()


        # create image
        image, flag = Image.get_or_create(src=thumb_image_src, video_id=video.id)
        # create tags
        tags = video_xml.xpath("//td[@id='channels']/table/tr/td")[1]
        for tag in tags:
            tmp_tag = None
            if not tag.xpath("i"):
                tmp_tag, t = Tag.get_or_create(name=tag.text)
            else:
                tmp_tag, t = Tag.get_or_create(name=tag.xpath("i")[0].tail)
            VideoTag.get_or_create(video_id=video.id, tag_id=tmp_tag.id)

        download_links = video_xml.xpath("//a[@class='download-video']")
        for link in download_links:
            href = link.attrib['href']
            quality = href.split('/')[-1]
            download_response = requests.get(href, headers=headers_with_cookie).history[0]
            download_url = download_response.headers['location']
            # create download link
            DownloadLink.get_or_create(quality=quality, src=download_url, video_id=video.id)


db.close()




