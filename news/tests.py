import pickle
import redis
from news.models import News

# r = redis.StrictRedis('localhost')
# mydict = {1:2,2:3,3:4}
# p_mydict = pickle.dumps(mydict)
# r.set('mydict',p_mydict)
#
# read_dict = r.get('mydict')
# yourdict = pickle.loads(read_dict)

# import pickle
# import redis
#
# r = redis.StrictRedis(host='localhost', port=6379, db=0)
# obj = News.objects.all()
# pickled_object = pickle.dumps(obj)
# r.set('some_key', pickled_object)
# unpacked_object = pickle.loads(r.get('some_key'))
#
# #obj == unpacked_object