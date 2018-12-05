from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Department, Base, CategoryItem, User

engine = create_engine('sqlite:///sportinggoodscatalogwithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Guest", email="guest@gmail.com",
             picture="https://www.freeiconspng.com/uploads/trophy-1-png-31.png")
session.add(User1)
session.commit()

# category for Baseball
department1 = Department(user_id=1, name="Baseball")

session.add(department1)
session.commit()

categoryItem2 = CategoryItem(user_id=1, name="Bats", description="Big Bats, Small Bats, Wooden Bats, Metal Bats",
                     price="$50.00", category="Equipment", department=department1)

session.add(categoryItem2)
session.commit()


categoryItem1 = CategoryItem(user_id=1, name="Gloves", description="Big Gloves, Small Gloves, Catchers Mits",
                     price="$35.00", category="Equipment", department=department1)

session.add(categoryItem1)
session.commit()

categoryItem2 = CategoryItem(user_id=1, name="Balls", description="Baseballs, Softballs, Practice Balls",
                     price="$2.99", category="Equipment", department=department1)

session.add(categoryItem2)
session.commit()

categoryItem3 = CategoryItem(user_id=1, name="Cleats", description="Black Cleats, Whites Cleats, Red cleats, & More!",
                     price="$50.00", category="Apparel", department=department1)

session.add(categoryItem3)
session.commit()

categoryItem4 = CategoryItem(user_id=1, name="Helmets", description="Batting Helmets, Catchers Masks",
                     price="$40.00", category="Equipment", department=department1)

session.add(categoryItem4)
session.commit()

categoryItem5 = CategoryItem(user_id=1, name="Hats", description="Fitted Hats & More!",
                     price="$20.00", category="Apparel", department=department1)

session.add(categoryItem5)
session.commit()

categoryItem6 = CategoryItem(user_id=1, name="Catchers Equipment", description="Knee Pads, Chest Pads",
                     price="$60.00", category="Apparel", department=department1)

session.add(categoryItem6)
session.commit()

categoryItem7 = CategoryItem(user_id=1, name="Jerseys",
                     description="Nike, Under Armour, and More!", price="$40.00", category="Apparel", department=department1)

session.add(categoryItem7)
session.commit()

categoryItem8 = CategoryItem(user_id=1, name="Pants", description="Nike, Under Armour, and More!",
                     price="$40.00", category="Apparel", department=department1)

session.add(categoryItem8)
session.commit()


# category for Basketball
department2 = Department(user_id=1, name="Basketball")

session.add(department2)
session.commit()


categoryItem1 = CategoryItem(user_id=1, name="Balls", description="Indoor Balls, Outdoor Balls",
                     price="$25.00", category="Equipment", department=department2)

session.add(categoryItem1)
session.commit()

categoryItem2 = CategoryItem(user_id=1, name="Hoops",
                     description="Mounted Hoops, Portable Hoops, Poolside Hoops", price="$200.00", category="Equipment", department=department2)

session.add(categoryItem2)
session.commit()

categoryItem3 = CategoryItem(user_id=1, name="Shoes", description="High Tops, Low Tops, & More",
                     price="$60.00", category="Apparel", department=department2)

session.add(categoryItem3)
session.commit()

categoryItem4 = CategoryItem(user_id=1, name="Jersey's", description="Nike, Under Armour, and More!",
                     price="$30.00", category="Apparel", department=department2)

session.add(categoryItem4)
session.commit()

categoryItem5 = CategoryItem(user_id=1, name="Shorts", description="Nike, Under Armour, and More!",
                     price="$35.00", category="Apparel", department=department2)

session.add(categoryItem5)
session.commit()

categoryItem6 = CategoryItem(user_id=1, name="Head Bands", description="Nike, Under Armour, and More!",
                     price="$12.00", category="Apparel", department=department2)

session.add(categoryItem6)
session.commit()


# category for Cycling
department1 = Department(user_id=1, name="Cycling")

session.add(department1)
session.commit()


categoryItem1 = CategoryItem(user_id=1, name="Bikes", description="Road Bike, Mountain Bikes, BMX Bikes, and More!",
                     price="$1000.00", category="Equipment", department=department1)

session.add(categoryItem1)
session.commit()

categoryItem2 = CategoryItem(user_id=1, name="Helmets", description="Road Helmet, Mountain Helmet, Kids Helmets, and More!",
                     price="$50.00", category="Equipment", department=department1)

session.add(categoryItem2)
session.commit()

categoryItem3 = CategoryItem(user_id=1, name="Pumps", description="Hand Pumps, Foot Pumps",
                     price="$25.00", category="Equipment", department=department1)

session.add(categoryItem3)
session.commit()

categoryItem4 = CategoryItem(user_id=1, name="Jerseys", description="Road Jersey, Mountain Jersey, and More!",
                     price="$25.00", category="Apparel", department=department1)

session.add(categoryItem4)
session.commit()

categoryItem2 = CategoryItem(user_id=1, name="Shorts", description="Road Shorts, Mountain Shorts, and More!",
                     price="$30.00", category="Apparel", department=department1)

session.add(categoryItem2)
session.commit()


# category for Camping
department1 = Department(user_id=1, name="Camping")

session.add(department1)
session.commit()


categoryItem1 = CategoryItem(user_id=1, name="Tents", description="1 Person, 2 Person, even 10 Person Tents!!",
                     price="$150.00", category="Equipment", department=department1)

session.add(categoryItem1)
session.commit()

categoryItem2 = CategoryItem(user_id=1, name="Sleeping Bags", description="Synthetic, Down, and More!",
                     price="$75.00", category="Equipment", department=department1)

session.add(categoryItem2)
session.commit()

categoryItem3 = CategoryItem(user_id=1, name="Backpacks",
                     description="Day Packs, Weekend Packs, Weeklong Packs!!", price="$75.00", category="Equipment", department=department1)

session.add(categoryItem3)
session.commit()

categoryItem4 = CategoryItem(user_id=1, name="Jackets", description="Windproof, Waterproof, Fleece.",
                     price="$45.00", category="Apparel", department=department1)

session.add(categoryItem4)
session.commit()

categoryItem5 = CategoryItem(user_id=1, name="Hiking Boots", description="Keen, Merrell, and More!!",
                     price="$65.00", category="Apparel", department=department1)

session.add(categoryItem5)
session.commit()

categoryItem2 = CategoryItem(user_id=1, name="Flashlights", description="All your lighting needs...",
                     price="$12.00", category="Equipment", department=department1)

session.add(categoryItem2)
session.commit()


# category for Football
department1 = Department(user_id=1, name="Football")

session.add(department1)
session.commit()


categoryItem1 = CategoryItem(user_id=1, name="Balls", description="Leather Balls, Rubber Balls, Nerf Balls!",
                     price="$25.00", category="Equipment", department=department1)

session.add(categoryItem1)
session.commit()

categoryItem2 = CategoryItem(user_id=1, name="Helmets", description="Blue Helmets, Red Helmets, Yellow Helmets, & More!",
                     price="$50.00", category="Equipment", department=department1)

session.add(categoryItem2)
session.commit()

categoryItem3 = CategoryItem(user_id=1, name="Pads", description="Pads, Pads, and more Pads!",
                     price="$40.00", category="Equipment", department=department1)

session.add(categoryItem3)
session.commit()

categoryItem4 = CategoryItem(user_id=1, name="Jerseys",
                     description="Nike, Under Armour, and More!", price="$50.00", category="Apparel", department=department1)

session.add(categoryItem4)
session.commit()

categoryItem5 = CategoryItem(user_id=1, name="Shoes", description="Turf Shoes, Cleats, and More!",
                     price="$60.00", category="Apparel", department=department1)

session.add(categoryItem5)
session.commit()


# category for Golf
department1 = Department(user_id=1, name="Golf")

session.add(department1)
session.commit()


categoryItem1 = CategoryItem(user_id=1, name="Clubs", description="Drivers, Irons, Putters",
                     price="$50.00", category="Equipment", department=department1)

session.add(categoryItem1)
session.commit()

categoryItem2 = CategoryItem(user_id=1, name="Balls", description="Titleist, Callaway, Srixon, Top Flite and More!",
                     price="$22.00", category="Equipment", department=department1)

session.add(categoryItem2)
session.commit()

categoryItem3 = CategoryItem(user_id=1, name="Bags", description="Standing Bags, Cart Bags, Travel Bags, and More!",
                     price="$6.50", category="Equipment", department=department1)

session.add(categoryItem3)
session.commit()

categoryItem4 = CategoryItem(user_id=1, name="Shirts", description="Nike, Under Armour, and More!",
                     price="$55.00", category="Apparel", department=department1)

session.add(categoryItem4)
session.commit()

categoryItem2 = CategoryItem(user_id=1, name="Gloves", description="Nike, Callaway, FootJoy, and More!! ",
                     price="$15.00", category="Apparel", department=department1)

session.add(categoryItem2)
session.commit()


# category for Hockey
department1 = Department(user_id=1, name="Hockey")

session.add(department1)
session.commit()

categoryItem9 = CategoryItem(user_id=1, name="Skates",
                     description="Ice Skates, Roller Skates!!!", price="$50.00", category="Apparel", department=department1)

session.add(categoryItem9)
session.commit()


categoryItem1 = CategoryItem(user_id=1, name="Sticks", description="Ice Sticks, Street Sticks, Wood Sticks, Metal Sticks...",
                     price="30.00", category="Equipment", department=department1)

session.add(categoryItem1)
session.commit()

categoryItem2 = CategoryItem(user_id=1, name="Pucks", description="Ice Pucks, Street Pucks, & More!",
                     price="$10.00", category="Equipment", department=department1)

session.add(categoryItem2)
session.commit()

categoryItem3 = CategoryItem(user_id=1, name="Pads",
                     description="All your padding needs!", price="$55.00", category="Equipment", department=department1)

session.add(categoryItem3)
session.commit()

categoryItem4 = CategoryItem(user_id=1, name="Gloves", description="Bauer, CCM, and More!",
                     price="$8.95", category="Apparel", department=department1)

session.add(categoryItem4)
session.commit()

categoryItem2 = CategoryItem(user_id=1, name="Nets", description="Street Hockey Nets, Steel Nets, Folding Nets.",
                     price="$100.00", category="Equipment", department=department1)

session.add(categoryItem2)
session.commit()

categoryItem10 = CategoryItem(user_id=1, name="Jerseys", description="Team Jerseys, Practice Jerseys, and More!",
                      price="$50.00", category="Apparel", department=department1)

session.add(categoryItem10)
session.commit()


# category for Hunting
department1 = Department(user_id=1, name="Hunting")

session.add(department1)
session.commit()


categoryItem1 = CategoryItem(user_id=1, name="Guns",
                     description="Handguns, Shotguns, Rifles", price="$150.00", category="Equipment", department=department1)

session.add(categoryItem1)
session.commit()

categoryItem2 = CategoryItem(user_id=1, name="Archery", description="Traditional Bows, Compound Bows, Crossbows, and More! ",
                     price="$100.00", category="Equipment", department=department1)

session.add(categoryItem2)
session.commit()


# category for Soccer
department1 = Department(user_id=1, name="Soccer")
session.add(department1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Balls", description="Mini Balls, Junior Balls, Match Balls, and More!",
                     price="$25.00", category="Equipment", department=department1)

session.add(categoryItem1)
session.commit

categoryItem1 = CategoryItem(user_id=1, name="Cleats",
                     description="Nike, Adidas, and More!", price="$50.00", category="Apparel", department=department1)

session.add(categoryItem1)
session.commit()


categoryItem1 = CategoryItem(user_id=1, name="Jerseys",
                     description="Nike, Adidas, and More!", price="$30.00", category="Apparel", department=department1)

session.add(categoryItem1)
session.commit()


print "Added category items!"
