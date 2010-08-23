import sys, os

sys.path.append('/C:/devtool/Python26/Lib/site-packages/django')
sys.path.append('/D:/education/python/MicroBlog/src/MicroBlog')
os.environ['DJANGO_SETTINGS_MODULE'] = 'MicroBlog.settings'

from FluxHodgeBlodge.links import utils
client = utils.DeliciousClient('brianmatthewkessler','salami')
data = client.fetch()
utils.create_link(data)

