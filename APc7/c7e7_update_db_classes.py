import shelve
db = shelve.open('class-shelve')

sue = db['sue']
sue.giveRaise(.25)
db['sue'] = sue

tom = db['tom']
tom.giveRaise(.20)
db['tom'] = tom
db.close()

#bob => Bob Smith 30000
#sue => Sue Jones 50000.0
#tom => Tom Doe 65000.0
#Smith
#Doe
