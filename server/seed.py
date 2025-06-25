from server.app import create_app, db
from server.models import User, Guest, Episode, Appearance
from datetime import date

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    user = User(username="admin")
    user.set_password("password")
    db.session.add(user)

    g1 = Guest(name="Lupita Nyong'o", occupation="Actor")
    g2 = Guest(name="Alex Kawira", occupation="Doctor")
    db.session.add_all([g1, g2])

    e1 = Episode(date=date(2025, 6, 10), number=101)
    e2 = Episode(date=date(2025, 6, 11), number=102)
    db.session.add_all([e1, e2])

    a1 = Appearance(rating=5, guest=g1, episode=e1)
    a2 = Appearance(rating=4, guest=g2, episode=e2)
    db.session.add_all([a1, a2])

    db.session.commit()
    print("Database seeded!")
