import logging
import time
import requests


def url2html(session: requests.Session, url: str, **kwargs):
  """
    Usage::

      print(url2html(requests.Session(), 'https://www.baidu.com'))

    :param timeout: default = 30
    :param max_try: default = 3
    :param retry_gap: default = 5
    :param anti_cloudflare: default = False
  """
  max_try = kwargs['max_try'] if 'max_try' in kwargs else 3
  timeout = kwargs['timeout'] if 'timeout' in kwargs else 30
  retry_gap = kwargs['retry_gap'] if 'retry_gap' in kwargs else 5
  anti_cloudflare = kwargs['anti_cloudflare'] if 'anti_cloudflare' in kwargs else False

  try_cnt = 0
  result = ""

  while try_cnt < max_try:
    try:
      result = session.get(url, timeout=timeout).content.decode()
      # <!DOCTYPE html><html lang="en-US"><head><title>Just a moment...</title><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=Edge"><meta name="robots" content="noindex,nofollow"><meta name="viewport" content="width=device-width,initial-scale=1"><link href="/cdn-cgi/styles/challenges.css" rel="stylesheet"></head><body class="no-js"><div class="main-wrapper" role="main"><div class="main-content"><noscript><div id="challenge-error-title"><div class="h2"><span class="icon-wrapper"><div class="heading-icon warning-icon"></div></span><span id="challenge-error-text">Enable JavaScript and cookies to continue</span></div></div></noscript></div></div>
      if '<title>Just a moment...</title>' in result and anti_cloudflare: # cloudflare 反爬虫
        # cloudflare anti-bot
        # https://github.com/Anorov/cloudflare-scrape/commit/e510962c608382bcef5de75033d60cc98cb9561d
        # 也是基于requests的所以 设置环境变量proxy即可
        import toolkit_cmm.thirdparty.cloudflarescrape as cfscrape
        scraper = cfscrape.create_scraper(sess=session, delay=10)
        r = scraper.get(url)
        if r.status_code == 200:
          return r.content
        else:
          continue
      else:
        return result
    except Exception as e: # Timeout
      logging.exception(e)
      try_cnt += 1
      time.sleep(retry_gap)
      return ''
  return result


def html2soup(html):
  from bs4 import BeautifulSoup
  return BeautifulSoup(html, 'lxml')


def url2soup(session: requests.Session, url: str, **kwargs):
  return html2soup(url2html(session=session, url=url, **kwargs))
