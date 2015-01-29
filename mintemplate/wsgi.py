"""
WSGI config for mintemplate project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys
import site

prev_sys_path = list(sys.path)
root = os.path.normpath(os.path.join(os.path.dirname(__file__), "../"))
sys.path.append(root)
site.addsitedir(os.path.join(root, ".env/lib/python%d.%d/site-packages" % sys.version_info[:2]))
site.addsitedir(os.path.join(root, ".env/lib64/python%d.%d/site-packages" % sys.version_info[:2]))

# addsitedir adds its directories at the end, but we want our local stuff
# to take precedence over system-installed packages.
# See http://code.google.com/p/modwsgi/issues/detail?id=112
new_sys_path = []
for item in list(sys.path):
  if item not in prev_sys_path:
    new_sys_path.append(item)
    sys.path.remove(item)
sys.path[:0] = new_sys_path

os.environ.setdefault("DJANGO_SETTINGS_MODULE", os.path.basename(os.path.dirname(__file__)) + ".settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
