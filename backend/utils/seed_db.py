from models.models import Price, Product, db


def seed_database(app):
    with app.app_context():
        db.drop_all()
        db.create_all()

        product1 = Product()
        product1.name = "Portland Zement"
        product1.sku = "PZ-001"
        product1.category = "Zement"

        db.session.add(product1)
        db.session.commit()

        price1 = Price()
        price1.price = 12.99
        price1.unit = "kg"
        price1.vendor = "Bauhaus"
        price1.url = "https://bauhaus.de/zement"
        price1.product_id = product1.id

        db.session.add(price1)
        db.session.commit()

        print("Datenbank erfolgreich mit Testdaten gefüllt!")
