.. Requests documentation master file, created by
   sphinx-quickstart on Sun Feb 13 23:54:25 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Requests: HTTP для людей
========================

Релиз v\ |version|. (:ref:`Установка <install>`)

Requests - это HTTP библиотека для человека, написанная на Python. Requests распространяется под :ref:`лицензией Apache2 <apache2>`

Стандартный модуль Python **urllib2** обеспечивает большинство нужных вам возможностей HTTP, но его API просто **ужасен**. Он был написан в другое время и для другого интернета. Он требует *чудовищно* много работы (приходится даже переопределять методы) для того, чтобы делать простые вещи. 

Так быть не должно. Не в Python.

::

    >>> r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
    >>> r.status_code
    200
    >>> r.headers['content-type']
    'application/json; charset=utf8'
    >>> r.encoding
    'utf-8'
    >>> r.text
    u'{"type":"User"...'
    >>> r.json()
    {u'private_gists': 419, u'total_private_repos': 77, ...}

Вот `похожий код, но без использования Requests <https://gist.github.com/973705>`_.

Requests решает все задачи связанные с Python HTTP/1.1,  позволяя без проблем интегрировать ваши веб-сервисы. Вам не придется в ручную добавлять запросы к вашему URL или формировать POST запрос, а Keep-alive и HTTP соединения автоматически образуют пул. Все это работает на `urllib3 <https://github.com/shazow/urllib3>`,которая встроена в Requests.


Рекомендации
------------

Правительство Её Величества, Amazon, Google, Twilio, Runscope, Mozilla, Heroku, PayPal, NPR, Obama for America, Transifex, Native Instruments, The Washington Post, Twitter, SoundCloud, Kippt, Readability, Sony, и даже федеральные институты США, которые предпочли бы остаться не названными, используют Requests. Requests была скачана более 40,000,000 раз через PyPi

**Armin Ronacher**
    Requests - это прекрасный образец того, каким может быть API с правильным уровнем абстракции.

**Matt DeBoard**
    Могу сказать только то, что Я собираюсь как-нибудь набить модуль Requests для Python от @kennethreitz'а на моем теле. 

**Daniel Greenfeld**
    Заменил библиотеку из 1200 строк вышедшего из под контроля кода с помощью 10. Спасибо @kennethreitz'у за Requests.
    Это было офигенно. 

**Kenny Meyers**
    HTTP на Python: Если вы сомневаетесь или, если вы не сомневаетесь, используйте Requests. Красиво, быстро, в духе Python.

Особенности 
-----------

Requests готова для современного интернета. 
  
- Интернациональные Домены и URL
- Keep-Alive & Организация Пулов Соединений
- Сессии с Постоянными Cookie
- SSL Verification как в браузере
- Базовая/Дайджест Аутентификация
- Элегантные Key/Value Cookies
- Автоматическая Распаковка
- Тело Ответа с Поддержкой Unicode
- Поддержка Multipart запросов
- Таймаут Подключения
- Поддержка ``.netrc``
- Python 2.6—3.4
- Поточно-безопасно.


Руководство пользователя
------------------------

Эта часть документации начинается с некоторой
справочной информации о Requests, затем шаг за шагом фокусируется на
инструкции для получения максимума от Requests.


.. toctree::
   :maxdepth: 2

   user/intro
   user/install
   user/quickstart
   user/advanced
   user/authentication


Руководство сообщество
----------------------

Эта часть документации рассказывает подробнее о экосистеме и сообществе Requests.

.. toctree::
   :maxdepth: 1

   community/faq
   community/out-there.rst
   community/support
   community/vulnerabilities
   community/updates

API Документация
----------------

Если вы ищете информацию по конкретной функции, классу или методу,
эта часть документации для вас.

.. toctree::
   :maxdepth: 2

   api


Руководство Участника
---------------------

Если вы хотите внести свой вклад в проект, это часть документации для
вас.

.. toctree::
   :maxdepth: 1

   dev/philosophy
   dev/todo
   dev/authors
