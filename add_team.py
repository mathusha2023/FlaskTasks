from data.users import User
from data.db_session import create_session


def add_team():
    db_sess = create_session()

    captain = User(surname="Scott", name="Ridley", age=21, position="captain", speciality="research engineer",
                   address="module_1", email="scott_chief@mars.org")

    u1 = User(surname="Bott", name="Ridley", age=19, position="vice-captain", speciality="research engineer",
              address="module_1", email="bott_rid@mars.org")

    u2 = User(surname="Watt", name="Pizel", age=22, position="navigator", speciality="geographer",
              address="module_3", email="pizelatt@mars.org")

    u3 = User(surname="Rott", name="Dudu", age=22, position="soldier", speciality="soldier",
              address="module_4", email="dudurott@mars.org")

    db_sess.add_all([captain, u1, u2, u3])
    db_sess.commit()
