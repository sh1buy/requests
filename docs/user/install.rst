.. _install:

Установка
=========

Эта часть документации рассказывает об установке Requests.
Первым шагом к использованию любого программного пакета является его правильная установка.


Распространение и Pip
---------------------

Проще всего установить Requests с помощью  `pip <https://pip.pypa.io>`_. Просто запустите следующую команду в терминале::

    $ pip install requests

или, с помощью `easy_install <http://pypi.python.org/pypi/setuptools>`_::

    $ easy_install requests

Но, лучше `этого не делать <https://stackoverflow.com/questions/3220404/why-use-pip-over-easy-install>`_.


Получить код
------------

Requests активно разрабатывается на GitHub, где ее код 
`всегда доступен <https://github.com/kennethreitz/requests>`_.

Вы можете либо клонировать публичный репозиторий::

    $ git clone git://github.com/kennethreitz/requests.git

Скачать `tarball <https://github.com/kennethreitz/requests/tarball/master>`_::

    $ curl -OL https://github.com/kennethreitz/requests/tarball/master

Или скачать `zipball <https://github.com/kennethreitz/requests/zipball/master>`_::

    $ curl -OL https://github.com/kennethreitz/requests/zipball/master


Если у вас есть копия исходного кода, вы можете встроить его в ваш пакет Python,
или установить его в site-packages::

    $ python setup.py install
