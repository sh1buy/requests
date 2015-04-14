.. _quickstart:

 Краткое руководство
====================

.. module:: requests.models

Не терпится начать? Эта страница расскажет, как начать работать
с Requests.

Для начала убедитесь, что:

* Requests :ref:`установленна <install>`
* Requests :ref:`обновлена <updates>`


Давайте начнем с некоторых простых примеров.


Сделать запрос
--------------

Сделать запрос с помощью Requests очень просто.

Начнем с импорта модуля Requests::

    >>> import requests

Теперь, давайте попробуем получить веб-страницу. Для этого примера, запросим 
таймлайн Гитхаба ::

    >>> r = requests.get('https://api.github.com/events')

Итак, у нас есть объект :class:`Response <requests.Response>` названный ``r``. Мы можем
получить всю нужную нам информацию из этого объекта.

Простота API Requests означает, что метод HTTP-запроса всегда очевиден. Например,
так делается HTTP-запрос методом POST::

    >>> r = requests.post("http://httpbin.org/post")

Правда, приятно? А как насчет других методов: PUT, DELETE, HEAD и OPTIONS?
Все просто::

    >>> r = requests.put("http://httpbin.org/put")
    >>> r = requests.delete("http://httpbin.org/delete")
    >>> r = requests.head("http://httpbin.org/get")
    >>> r = requests.options("http://httpbin.org/get")

Это все хорошо, но это только малая часть того, что может Requests.


Передача Параметров В URL
-------------------------

Вам часто придется отправлять часть информации в строке запроса URL. Если
вы строили URL-адрес вручную, то знаете, что эти данные записываются в виде 
пары ключ/значение в URL после вопросительного знака, например ``httpbin.org/get?key=val``.
Requests позволяет представить эти аргументы в качестве словаря, используя 
аргумент ``params``. Как пример, если вы хотите передать ``key1=value1`` и 
``key2=value2`` в ``httpbin.org/get``, вы можете использовать следующий код::

    >>> payload = {'key1': 'value1', 'key2': 'value2'}
    >>> r = requests.get("http://httpbin.org/get", params=payload)

Вы можете убедиться, что URL был правильно закодирован, распечатав URL-адрес::

    >>> print(r.url)
    http://httpbin.org/get?key2=value2&key1=value1

Обратите внимание, что любой ключ словаря со значением ``None` не будет добавлен к
строке запроса URL-адреса.

Для того, чтобы передать список элементов в качестве значения необходимо пометить ключ, 
добавив к нему квадратные скобки ``[]``::

    >>> payload = {'key1': 'value1', 'key2[]': ['value2', 'value3']}
    >>> r = requests.get("http://httpbin.org/get", params=payload)
    >>> print(r.url)
    http://httpbin.org/get?key1=value1&key2%5B%5D=value2&key2%5B%5D=value3

Содержимое Ответа
-----------------

Мы можем прочитать содержимое ответа сервера. Снова рассмотрим таймлайн 
ГитХаба::

    >>> import requests
    >>> r = requests.get('https://api.github.com/events')
    >>> r.text
    u'[{"repository":{"open_issues":0,"url":"https://github.com/...

Запросы будут автоматически декодировать контент с сервера. Большинство Unicode
символов без проблем декодируется.

Когда вы делаете запрос, Requests делает обоснованные предположения о кодировке
ответа на основе HTTP-заголовков. Requests угадывает какая кодировка текста используется 
при доступе к ``r.text``. Вы можете выяснить какую кодировку Requests
использует и изменить ее с помощью свойства ``r.encoding``::

    >>> r.encoding
    'utf-8'
    >>> r.encoding = 'ISO-8859-1'

Если вы измените кодировку, Requests будет использовать новое значение ``r.encoding``
всякий раз, когда вы вызываете ``r.text``. Возможно, вам это пригодится, если вы хотите 
использовать особую логику при выборе кодировки. Например, в HTTP и XML есть возможность 
указать  кодировку в теле. В подобных ситуациях, вы должны использовать ``r.content``,
чтобы найти кодировку, и затем установить ``r.encoding``. Это позволит вам использовать 
``r.text`` с правильной кодировкой.

Requests может использовать пользовательские кодировки, если вы нуждаетесь в них. Если
вы создали нужную кодировку и зарегистрировали ее в модуле``codecs``, 
вы можете просто использовать имя кодека как значение ``r.encoding` и
Requests обработает кодировку.

Binary Response Content
-----------------------

You can also access the response body as bytes, for non-text requests::

    >>> r.content
    b'[{"repository":{"open_issues":0,"url":"https://github.com/...

The ``gzip`` and ``deflate`` transfer-encodings are automatically decoded for you.

For example, to create an image from binary data returned by a request, you can
use the following code::

    >>> from PIL import Image
    >>> from StringIO import StringIO
    >>> i = Image.open(StringIO(r.content))


JSON Response Content
---------------------

There's also a builtin JSON decoder, in case you're dealing with JSON data::

    >>> import requests
    >>> r = requests.get('https://api.github.com/events')
    >>> r.json()
    [{u'repository': {u'open_issues': 0, u'url': 'https://github.com/...

In case the JSON decoding fails, ``r.json`` raises an exception. For example, if
the response gets a 401 (Unauthorized), attempting ``r.json`` raises ``ValueError:
No JSON object could be decoded``


Raw Response Content
--------------------

In the rare case that you'd like to get the raw socket response from the
server, you can access ``r.raw``. If you want to do this, make sure you set
``stream=True`` in your initial request. Once you do, you can do this::

    >>> r = requests.get('https://api.github.com/events', stream=True)
    >>> r.raw
    <requests.packages.urllib3.response.HTTPResponse object at 0x101194810>
    >>> r.raw.read(10)
    '\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\x03'

In general, however, you should use a pattern like this to save what is being
streamed to a file::

    with open(filename, 'wb') as fd:
        for chunk in r.iter_content(chunk_size):
            fd.write(chunk)

Using ``Response.iter_content`` will handle a lot of what you would otherwise
have to handle when using ``Response.raw`` directly. When streaming a
download, the above is the preferred and recommended way to retrieve the
content.


Custom Headers
--------------

If you'd like to add HTTP headers to a request, simply pass in a ``dict`` to the
``headers`` parameter.

For example, we didn't specify our content-type in the previous example::

    >>> import json
    >>> url = 'https://api.github.com/some/endpoint'
    >>> headers = {'user-agent': 'my-app/0.0.1'}

    >>> r = requests.get(url, headers=headers)

Note: Custom headers are given less precedence than more specific sources of information. For instance:

* Authorization headers will be overridden if credentials are passed via the ``auth`` parameter or are specified in a ``.netrc`` accessible in the environment.
* Authorization headers will be removed if you get redirected off-host.
* Proxy-Authorization headers will be overridden by proxy credentials provided in the URL.
* Content-Length headers will be overridden when we can determine the length of the content.

Furthermore, Requests does not change its behavior at all based on which custom headers are specified. The headers are simply passed on into the final request.


More complicated POST requests
------------------------------

Typically, you want to send some form-encoded data — much like an HTML form.
To do this, simply pass a dictionary to the ``data`` argument. Your
dictionary of data will automatically be form-encoded when the request is made::

    >>> payload = {'key1': 'value1', 'key2': 'value2'}
    >>> r = requests.post("http://httpbin.org/post", data=payload)
    >>> print(r.text)
    {
      ...
      "form": {
        "key2": "value2",
        "key1": "value1"
      },
      ...
    }

There are many times that you want to send data that is not form-encoded. If
you pass in a ``string`` instead of a ``dict``, that data will be posted directly.

For example, the GitHub API v3 accepts JSON-Encoded POST/PATCH data::

    >>> import json
    >>> url = 'https://api.github.com/some/endpoint'
    >>> payload = {'some': 'data'}

    >>> r = requests.post(url, data=json.dumps(payload))


POST a Multipart-Encoded File
-----------------------------

Requests makes it simple to upload Multipart-encoded files::

    >>> url = 'http://httpbin.org/post'
    >>> files = {'file': open('report.xls', 'rb')}

    >>> r = requests.post(url, files=files)
    >>> r.text
    {
      ...
      "files": {
        "file": "<censored...binary...data>"
      },
      ...
    }

You can set the filename, content_type and headers explicitly:

    >>> url = 'http://httpbin.org/post'
    >>> files = {'file': ('report.xls', open('report.xls', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}

    >>> r = requests.post(url, files=files)
    >>> r.text
    {
      ...
      "files": {
        "file": "<censored...binary...data>"
      },
      ...
    }

If you want, you can send strings to be received as files::

    >>> url = 'http://httpbin.org/post'
    >>> files = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}

    >>> r = requests.post(url, files=files)
    >>> r.text
    {
      ...
      "files": {
        "file": "some,data,to,send\\nanother,row,to,send\\n"
      },
      ...
    }

In the event you are posting a very large file as a ``multipart/form-data``
request, you may want to stream the request. By default, ``requests`` does not
support this, but there is a separate package which does -
``requests-toolbelt``. You should read `the toolbelt's documentation
<https://toolbelt.readthedocs.org>`_ for more details about how to use it.

For sending multiple files in one request refer to the :ref:`advanced <advanced>`
section.


Response Status Codes
---------------------

We can check the response status code::

    >>> r = requests.get('http://httpbin.org/get')
    >>> r.status_code
    200

Requests also comes with a built-in status code lookup object for easy
reference::

    >>> r.status_code == requests.codes.ok
    True

If we made a bad request (a 4XX client error or 5XX server error response), we
can raise it with
:meth:`Response.raise_for_status() <requests.Response.raise_for_status>`::

    >>> bad_r = requests.get('http://httpbin.org/status/404')
    >>> bad_r.status_code
    404

    >>> bad_r.raise_for_status()
    Traceback (most recent call last):
      File "requests/models.py", line 832, in raise_for_status
        raise http_error
    requests.exceptions.HTTPError: 404 Client Error

But, since our ``status_code`` for ``r`` was ``200``, when we call
``raise_for_status()`` we get::

    >>> r.raise_for_status()
    None

All is well.


Response Headers
----------------

We can view the server's response headers using a Python dictionary::

    >>> r.headers
    {
        'content-encoding': 'gzip',
        'transfer-encoding': 'chunked',
        'connection': 'close',
        'server': 'nginx/1.0.4',
        'x-runtime': '148ms',
        'etag': '"e1ca502697e5c9317743dc078f67693f"',
        'content-type': 'application/json'
    }

The dictionary is special, though: it's made just for HTTP headers. According to
`RFC 7230 <http://tools.ietf.org/html/rfc7230#section-3.2>`_, HTTP Header names
are case-insensitive.

So, we can access the headers using any capitalization we want::

    >>> r.headers['Content-Type']
    'application/json'

    >>> r.headers.get('content-type')
    'application/json'

It is also special in that the server could have sent the same header multiple
times with different values, but requests combines them so they can be
represented in the dictionary within a single mapping, as per
`RFC 7230 <http://tools.ietf.org/html/rfc7230#section-3.2>`_:

    > A recipient MAY combine multiple header fields with the same field name
    > into one "field-name: field-value" pair, without changing the semantics
    > of the message, by appending each subsequent field value to the combined
    > field value in order, separated by a comma.

Cookies
-------

If a response contains some Cookies, you can quickly access them::

    >>> url = 'http://example.com/some/cookie/setting/url'
    >>> r = requests.get(url)

    >>> r.cookies['example_cookie_name']
    'example_cookie_value'

To send your own cookies to the server, you can use the ``cookies``
parameter::

    >>> url = 'http://httpbin.org/cookies'
    >>> cookies = dict(cookies_are='working')

    >>> r = requests.get(url, cookies=cookies)
    >>> r.text
    '{"cookies": {"cookies_are": "working"}}'


Redirection and History
-----------------------

By default Requests will perform location redirection for all verbs except
HEAD.

We can use the ``history`` property of the Response object to track redirection.

The :meth:`Response.history <requests.Response.history>` list contains the
:class:`Response <requests.Response>` objects that were created in order to
complete the request. The list is sorted from the oldest to the most recent
response.

For example, GitHub redirects all HTTP requests to HTTPS::

    >>> r = requests.get('http://github.com')
    >>> r.url
    'https://github.com/'
    >>> r.status_code
    200
    >>> r.history
    [<Response [301]>]


If you're using GET, OPTIONS, POST, PUT, PATCH or DELETE, you can disable
redirection handling with the ``allow_redirects`` parameter::

    >>> r = requests.get('http://github.com', allow_redirects=False)
    >>> r.status_code
    301
    >>> r.history
    []

If you're using HEAD, you can enable redirection as well::

    >>> r = requests.head('http://github.com', allow_redirects=True)
    >>> r.url
    'https://github.com/'
    >>> r.history
    [<Response [301]>]


Timeouts
--------

You can tell Requests to stop waiting for a response after a given number of
seconds with the ``timeout`` parameter::

    >>> requests.get('http://github.com', timeout=0.001)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    requests.exceptions.Timeout: HTTPConnectionPool(host='github.com', port=80): Request timed out. (timeout=0.001)


.. admonition:: Note

    ``timeout`` is not a time limit on the entire response download;
    rather, an exception is raised if the server has not issued a
    response for ``timeout`` seconds (more precisely, if no bytes have been
    received on the underlying socket for ``timeout`` seconds).


Errors and Exceptions
---------------------

In the event of a network problem (e.g. DNS failure, refused connection, etc),
Requests will raise a :class:`~requests.exceptions.ConnectionError` exception.

In the rare event of an invalid HTTP response, Requests will raise an
:class:`~requests.exceptions.HTTPError` exception.

If a request times out, a :class:`~requests.exceptions.Timeout` exception is
raised.

If a request exceeds the configured number of maximum redirections, a
:class:`~requests.exceptions.TooManyRedirects` exception is raised.

All exceptions that Requests explicitly raises inherit from
:class:`requests.exceptions.RequestException`.

-----------------------

Ready for more? Check out the :ref:`advanced <advanced>` section.
