import pymongo

mc = pymongo.MongoClient()
mc.test.foo.find_one()

print('ok!')
