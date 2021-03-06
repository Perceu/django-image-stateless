import os
import sys
from io import BytesIO
from PIL import Image

from django.conf import settings
from django.core.wsgi import get_wsgi_application

DEBUG = os.environ.get('DEBUG', 'on') == 'on'
SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(32))
ALLOWED_HOST = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')


settings.configure(
    DEBUG = DEBUG,
    SECRET_KEY = 'THISASECRETKEY',
    ROOT_URLCONF = __name__,
    ALLOWED_HOST = ALLOWED_HOST,
    MIDDLEWARE_CLASSES = (
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XframeOptionsMiddleware',
    ),
)

from django.urls import path
from django import forms
from django.http import HttpResponse

class ImageForm(forms.Form):
    height = forms.IntegerField(min_value=1, max_value=2000)
    width = forms.IntegerField(min_value=1, max_value=2000)

    def generate(self, image_format='png'):
        height = self.cleaned_data['height']
        width = self.cleaned_data['width']
        image = Image.new('RGB', (width,height))
        content = BytesIO()
        image.save(content, image_format)
        content.seek(0)
        return content

def image_render(request, height, width):
    form = ImageForm(dict(width = width, height = height))
    if form.is_valid():
        image = form.generate()
        return HttpResponse(image, content_type='image/png')
    else:
        return HttpResponse('As dimenções não são validas')



def index(request):
    return HttpResponse('O projeto inicial esta rodando com sucesso!')


urlpatterns = (
    path('image/<int:height>/<int:width>', image_render, name='image'),
    path('', index),
)

application = get_wsgi_application()

if __name__=="__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)