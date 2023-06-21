from rest_framework import authentication


class BearerAuthentication(authentication.TokenAuthentication):
    """Bearer Authentications file. Used to define the keyword class variable.

    See more:
        https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication
    """
    keyword = 'Token'
