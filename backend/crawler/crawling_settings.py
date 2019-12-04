import json
import re
from konlpy.tag import Okt
from collections import Counter
import requests
from bs4 import BeautifulSoup as bs
import datetime

json = json
requests = requests
re = re
Okt = Okt
Counter = Counter
bs = bs
datetime = datetime

except_list = [
    '\n', '\t', '기자', '지난', '이후',
    '우리', '기사', '배포', '때문', '기간',
    '위해', '매체', '상황', '이상', '전격',
    '통해', '가운데', '대해', '가장', '현재',
    '이유', '라며', '무단', '생각', '최근',
    '이번', '영상', '설명', '사진', '인기',
    '제공', '이용', '위해', '지금', '가지',
    '다른', '편향', '때문', '관련', '여러'
]