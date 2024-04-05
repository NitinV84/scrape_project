"""
URL configuration for scrape_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

# upstream django {
#     server 127.0.0.1:8000;  
# }

# upstream celery_worker {
#     server unix:/home/developer/Desktop/Django/scrape_project/celery.sock;  
# }

# upstream celery_beat {
#     server unix:/home/developer/Desktop/Django/scrape_project/celery_beat.sock;  
# }

# server {
#     listen 80;
#     server_name localhost;

#     location / {
#         proxy_pass http://django;
#         proxy_set_header Host $host;
#         proxy_set_header X-Real-IP $remote_addr;
#         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
#         proxy_set_header X-Forwarded-Proto $scheme;
#     }

#     location /celery/ {
#         proxy_pass http://celery_worker;
#         proxy_set_header Host $host;
#         proxy_set_header X-Real-IP $remote_addr;
#         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
#         proxy_set_header X-Forwarded-Proto $scheme;
#     }

#     location /celerybeat/ {
#         proxy_pass http://celery_beat;
#         proxy_set_header Host $host;
#         proxy_set_header X-Real-IP $remote_addr;
#         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
#         proxy_set_header X-Forwarded-Proto $scheme;
#     }

    # Custom error page for specific conditions
    # error_page 499 = @custom_error;
    # location @custom_error {
    #     return 499;
    # }

    # Example of returning a 499 error if user agent is Chrome
    # if ($http_user_agent ~* "chrome") {
    #     return 499;
    # }
# }


# sudo ln -s /etc/nginx/sites-available/scrape_project /etc/nginx/sites-enabled/
