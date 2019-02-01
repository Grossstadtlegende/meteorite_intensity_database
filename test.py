import helper
from table_definitions import Kingdom

session = helper.connect_db()

K1 = Kingdom('differentiated')
session.add(K1)
K2 = Kingdom('undifferentiated')
session.add(K2)
