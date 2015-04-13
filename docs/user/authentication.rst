.. _аутентификация:

Аутентификация
==============

Этот документ рассказывает о разных способах аутентификации с помощью Requests.

Большинство веб-сервисов запрашивают аутентификацию, причем аутентификацию разных типов.
Ниже мы приводим различные формы аутентификация доступные в Requests, переходя от
простого к сложному.


Базовая Аутентификация
----------------------

Множество веб-сервисов требуют аутентификация по средствам HTTP Basic Auth. Это
самый простой способ, который Requests поддерживает прямо из коробки.

Создать запрос с HTTP Basic Auth очень легко::

    >>> from requests.auth import HTTPBasicAuth
    >>> requests.get('https://api.github.com/user', auth=HTTPBasicAuth('user', 'pass'))
    <Response [200]>

На самом деле, HTTP Basic Auth так распространена, что в Requests есть сокращение для 
ее использования::

    >>> requests.get('https://api.github.com/user', auth=('user', 'pass'))
    <Response [200]>

 Просто передайте учетные данные в кортеже, так же, как в
``HTTPBasicAuth`` примером выше.


netrc Аутентификация
~~~~~~~~~~~~~~~~~~~~

Если метод аутентификации не передан чере аргумент ``auth``, Requests попробует
получить учетные данные аутентификации для хоста из пользовательского файла netrc.

если учетные данные для хоста найдены, запрос отправляется с помощью HTTP Basic
Auth.


Дайджест Аутентификация
-----------------------

Другая очень популярная форма HTTP аутентификации - это Дайджест аутентификация,
и Requests так же хорошо поддерживает ее из коробки::

    >>> from requests.auth import HTTPDigestAuth
    >>> url = 'http://httpbin.org/digest-auth/auth/user/pass'
    >>> requests.get(url, auth=HTTPDigestAuth('user', 'pass'))
    <Response [200]>


OAuth 1 Аутентификация
----------------------

Так же распространенной формой аутентификации для нескольких веб API является OAuth. 
Библиотека ``requests-oauthlib`` позволяет пользователям Requests с легкостью создавть запросы с OAuth аутентификацией.::

    >>> import requests
    >>> from requests_oauthlib import OAuth1

    >>> url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
    >>> auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
                      'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')

    >>> requests.get(url, auth=auth)
    <Response [200]>

Для получения дополнительной информации о том, как работает oauth-авторизации, пожалуйста, обратитесь к официальному `OAuth`_ сайту.
За примерами и документацией requests-oauthlib, пожалуйста, см. репозиторий `requests_oauthlib`_
на github


Другие способы Аутентификации
-----------------------------

Requests спланирована так, чтобы была возможность легко подключить 
другие формы аутентификации. Члены open-source сообщества часто 
пишутобработчики для более сложных или менее часто используемых форм аутентификации.
Некоторые из лучших собраны вместе, под игидой `Requests organization`_, включая:

- Kerberos_
- NTLM_

Если вы хотите использовать любую из этих форм аутентификации, перейдите на их
Github страницу и следуйте инструкциям.


Новые Формы Аутентификации
--------------------------

Если Вы не можете найти хорошую реализацию нужной вам формы аутентификации, вы 
можете реализовать ее самостоятельно. Requests позволяет легко добавить свои собственные
формы аутентификации.

Для этого, создайте подкласс :class:`AuthBase <requests.auth.AuthBase>` и реализуйте
``__call__()`` метод::

    >>> import requests
    >>> class MyAuth(requests.auth.AuthBase):
    ...     def __call__(self, r):
    ...         # Реализация моей аутентификации
    ...         return r
    ...
    >>> url = 'http://httpbin.org/get'
    >>> requests.get(url, auth=MyAuth())
    <Response [200]>

Во время установки запросы обработчик аутентификации присоединяется к нему. 
`__call__` метод, следовательно, должны сделать все, что требуется, 
чтобы аутентификация работала. Некоторые формы аутентификация будет дополнительно 
добавлять хуки, чтобы обеспечить больше функциональности.

Больше примеров вы можете найти по запросу `Requests organization`_ и в
файле ``auth.py``.

.. _OAuth: http://oauth.net/
.. _requests_oauthlib: https://github.com/requests/requests-oauthlib
.. _Kerberos: https://github.com/requests/requests-kerberos
.. _NTLM: https://github.com/requests/requests-ntlm
.. _Requests organization: https://github.com/requests

