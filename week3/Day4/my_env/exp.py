import psycopg2

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save(self):
        """Save the item to the database."""
        connection = psycopg2.connect(database="menu_database", 
                                      user="postgres", 
                                      password="1904",
                                      host='localhost',
                                      port='5432')
        cursor = connection.cursor()
        query = "INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s) RETURNING item_id;"
        cursor.execute(query, (self.name, self.price))
        connection.commit()
        cursor.close()
        connection.close()

    # def delete(self):
    #     """Delete the item from the database."""
    #     connection = psycopg2.connect(database="menu_database", user="your_user", password="your_password")
    #     cursor = connection.cursor()
    #     query = "DELETE FROM Menu_Items WHERE item_name = %s;"
    #     cursor.execute(query, (self.name,))
    #     connection.commit()
    #     cursor.close()
    #     connection.close()

    # def update(self, new_name, new_price):
    #     """Update the item's name and price."""
    #     connection = psycopg2.connect(database="menu_database", user="your_user", password="your_password")
    #     cursor = connection.cursor()
    #     query = "UPDATE Menu_Items SET item_name = %s, item_price = %s WHERE item_name = %s;"
    #     cursor.execute(query, (new_name, new_price, self.name))
    #     connection.commit()
    #     cursor.close()
    #     connection.close()
    #     # Update instance attributes
    #     self.name = new_name
    #     self.price = new_price
