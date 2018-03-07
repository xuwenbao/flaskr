FROM 172.16.74.168/default/python:3.6.4
MAINTAINER Wenbao Xu<xuwenbao@chinacloud.com.cn>

WORKDIR /usr/src/app

ENV FLASK_APP app.py

COPY . .
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.douban.com/simple/

EXPOSE 8000

CMD ["python", "-m", "flask", "run", "--host", "0.0.0.0", "--port", "8000"]
