libreveal – scripts and utilities for Django
============================================

This is a collection of management commands, scripts and utilities we
use for deploying [Django][]-sites at [Reveal IT][].

Like Django, these are open source, available under the [BSD license][].
If you find any parts useful, feel free to rip them out and reuse them
whatever way you please.

#### Installation ####

While there are many ways to install Python libraries, we prefer using
[pip][] and [virtualenv][]. If you have that setup, installing libreveal
is as simple as this command:

    pip install -e git://github.com/revealit/libreveal.git#egg=revealit

After that, you should add `'revealit'` to your `INSTALLED_APPS` section
in Django’s `settings.py`.

#### Usage ####

To use the `uwsgi_reload` view, you will have to set `INTERNAL_IPS` in
your settings file to include the IP-addresses you want to be able to
reload the server. If running the reload command from the localhost,
adding 127.0.0.1 should be enough.

Then, you need to add the `uwsgi_reload` view to your URLconf. Something
like this should work:

    (r'^uwsgi_reload/$', 'revealit.views.uwsgi_reload'),

When that is all set up, you should be able to run
`curl http://example.com/uwsgi_reload/` from any IP address on the
`INTERNAL_IPS` list and have it reply `Reload OK`.

[Django]: http://www.djangoproject.com/
[Reveal IT]: http://revealit.dk/
[BSD license]: http://www.opensource.org/licenses/bsd-license.php
[pip]: http://pip.openplans.org/
[virtualenv]: http://virtualenv.openplans.org/

