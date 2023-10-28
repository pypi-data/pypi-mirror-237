One Software Development Kit
=====

Extend Django things as SDK for One Development


Installation and usage
======================

Quick start
-----------

1. Add "sdk" to your INSTALLED_APPS setting like this::

   ``` python
        INSTALLED_APPS = [
            ...,
            "sdk",
        ]
    ```

Django Allauth
--------------

1. Configure your settings.py

    ``` python
    # Add the following lines to your settings.py
    TEMPLATES = [
        {
            "OPTIONS": {
                # https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
                "context_processors": [
                    ...
                    "sdk.allauth.context_processors.allauth_settings",
                ],
            },
        },
    ]

    # django-allauth
    # ------------------------------------------------------------------------------
    # https://django-allauth.readthedocs.io/en/latest/configuration.html
    ACCOUNT_ADAPTER = "sdk.allauth.adapters.AccountAdapter"
    # https://django-allauth.readthedocs.io/en/latest/forms.html
    ACCOUNT_FORMS = {"signup": "sdk.allauth.forms.UserSignupForm"}
    # https://django-allauth.readthedocs.io/en/latest/configuration.html
    SOCIALACCOUNT_ADAPTER = "sdk.allauth.adapters.SocialAccountAdapter"
    # https://django-allauth.readthedocs.io/en/latest/forms.html
    SOCIALACCOUNT_FORMS = {"signup": "sdk.allauth.forms.UserSocialSignupForm"}

    ```

Riso Sweet Message
------------------

1. Add "messages" to your TEMPLATES setting like this::

   ``` python
    TEMPLATES = [
        {
            "OPTIONS": {
                "builtins": [
                    "sdk.contrib.messages.templatetags.sweet_message",
                ]
            },
        },
    ]
    ```

2. Add "messages" to your "base.html" like this

    ``` html
    {% sweet_message_media True %} # If your template already add jquery and bootstrap, you can set this to False
    </head>

    {% include 'messages/widget.html' %}
    </body>
    ```

Django Object Actions
---------------------

1. Add "django_object_actions" to your INSTALLED_APPS setting like this::

   ``` python
        INSTALLED_APPS = [
            ...,
            "django_object_actions",
        ]
    ```

2. Inherit your model from "sdk.contrib.admin.options" like this::

   ``` python
    from sdk.contrib.admin.options import GenericRelationAdmin, ModelAdmin, MasterModelAdmin
    from django_object_actions import action

    @admin.register(MyModel)
    class MyModelAdmin(ModelAdmin):
        ...
        @action(label="Publish", description="Submit this article")  # optional
        def publish_this(self, request, obj):
            pass
    ```


Django One Grappelli
--------------------

1. Add "grappelli" to your INSTALLED_APPS setting like this::

    ``` python
    INSTALLED_APPS = [
        ...,
        # "grappelli.saul",  Optional Metronic Saul theme
        # "grappelli.dashboard",  Optional custom dashboard
        "grappelli",  # grappelli must be placed before django.contrib.admin.
        "django.contrib.admin",
    ]
    ```

2. Add "grappelli" to your urls.py setting like this::

    ``` python
    urlpatterns = [
        ...,
        path("grappelli/", include("grappelli.urls")),  # grappelli URLS
        path("admin/", admin.site.urls),
    ]
    ```


Django Single Sign On
---------------------

    As a Server


1. Add "sdk.sso.server" to your INSTALLED_APPS setting like this::

    ``` python
    INSTALLED_APPS = [
        ...,
        "sdk.sso.server",
    ]
    ```

2. Add "sdk.sso.server" to your urls.py setting like this::

    ``` python
    from sdk.sso.server.server import sso_server
    urlpatterns = [
        ...,
        path("sso-server/", include(sso_server.get_urls())),
    ]
    ```

3. Create a Client in Django Admin


    As a Client


1. Add "sdk.sso.client" to your INSTALLED_APPS setting like this::

    ``` python
    INSTALLED_APPS = [
        ...,
        "sdk.sso.client",
    ]
    ```
   
2. Add "sdk.sso.client" to your urls.py setting like this::

    ``` python
    from sdk.sso.client.client import sso_client
    urlpatterns = [
        ...,
        path("sso-client/", include(sso_client.get_urls())),
    ]
    ```
   
3. Add SSO server config to your setting like this::

    ``` python
    SSO_PRIVATE_KEY = 'GEQE7hLKrK0itGpUnKWy9l13bZUO1JJBS3JtmcPC2PJI5A7c4rZA6N6IVzdEHQg1'
    SSO_PUBLIC_KEY = 'e5PQzclB0I1pIAVPHl9sRfgk0wBNVILI8IGwLk6slP4z77k6ENdASalhK5K1mbp1'
    SSO_SERVER = 'http://DOMAIN/sso-server/'
    ```

How to contribute
=================

Please make sure to update tests as appropriate.

Getting Started
---------------

1. Clone the repository

    ``` bash
    # Run the following command in your terminal
    pre-commit install
    git update-index --assume-unchanged .idea/runConfigurations/* .idea/riso.iml
    ```

2. Prepare the environment, Create a virtual environment with Python 3.11 or higher and activate it. Then install the
   dependencies using pip:

    ``` bash
    # Run the following command in your terminal
    cd riso
    pip install -r requirements.txt
    ```

3. Update following files

    ```
    # .envs/.local/.django
    # .envs/.local/.postgres
    ```

4. Then using pycharm runConfiguration to start coding

Useful commands
---------------

- Run test with coverage

    ``` bash
    docker-compose -f riso/local.yml run --rm django pytest --cov --cov-report term-missing --cov-report html
    ```

Other information
=================

What's in this project?
-----------------------

This project is a Django project with a single app called "sdk".
