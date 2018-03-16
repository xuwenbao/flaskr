FROM hub.chinacloud.com/default/python:3.6.4
MAINTAINER Wenbao Xu<xuwenbao@chinacloud.com.cn>

WORKDIR /usr/src/app

ENV FLASK_APP app.py
ENV FLASKR_SETTINGS /usr/src/app/settings.py

COPY . .
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.douban.com/simple/

EXPOSE 8000
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

CMD ["python", "-m", "flask", "run", "--host", "0.0.0.0", "--port", "8000"]
