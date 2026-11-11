from mysql import connector
from datetime import datetime

class DBConnect:
    def get_connector(self):
        self.connection = connector.connect(
            user="sharath",
            password="mysql",
            host="localhost",
            db="gym_db"
        )
        if self.connection:
            print("Successfully connected to database.")
            self.cursor = self.connection.cursor()
        else:
            print("Error: something wrong while connecting to database.")

    def close(self):
        self.connection.close()

class GymManagement(DBConnect):
    def __init__(self):
        super().get_connector()

    def get_object(self, id=None):
        if id:
            query = "select * from member where id=%s"
            try:
                self.cursor.execute(query, (id,))
                record = self.cursor.fetchone()
            except Exception as e:
                print("Error:", e)
            return record
        else:
            print("Give id as argument.")

    def get(self, id=None):
        query = "select * from member"
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        if not records:
            print("No records.")
            return
        return records

    def retreive(self, id=None):
        if not id:
            print("Error: id is not provided.")
            return
        records = self.get_object(id)
        if not records:
            print("No records.")
            return
        return records

    def post(self, **kwargs):
        values = [ v for v in kwargs.values() ]
        query = """
        insert into member (name, place, mobile, plan, fee, join_date)
        values (%s, %s, %s, %s, %s, %s)
        """
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            print("Data inserted successfully.")
        except Exception as e:
            print("Error:", e)

    def delete(self, id=None):
        query = "delete from member where id = %s"
        try:
            self.cursor.execute(query, (id,))
            self.connection.commit()
            self.cursor.execute(f"select * from member where id={id}")
            if not self.cursor.fetchall():
                return True, "Member deleted successfully."
            else:
                return False, "Member not deleted."
        except Exception as e:
            return False, f"Error: {e}"

    def put(self, id=None, **kwargs):
        if not id:
            return False, "Error: id is not provided."
        query_parts = [
            "update member set",
            ", ".join([f"{k}='{v}'" for k, v in kwargs.items()]),
            f"where id={id}"
        ]
        query = " ".join(query_parts)
        try:
            self.cursor.execute(query)
            self.connection.commit()
            return True, "Product updated successfully."
        except Exception as e:
            return False, "Error: " + e

if __name__ == "__main__":
    member_manager = GymManagement()
    # (name, place, mobile, plan, fee, join_date)
    # member_manager.post(
    #     name="Rahul", place="Kaloor", mobile="8957432315",
    #     plan="1 Month", fee=1000, join_date=datetime.datetime(2026, 7, 18, 18, 30)
    # )


    # member_manager.delete(3)
    # member_manager.post(
    #     name="Aravind", place="Palarivattom", mobile="8756346413",
    #     plan="3 month", fee=1200, join_date=datetime.strptime("2026-10-28 10:30 pm", "%Y-%m-%d %I:%M %p")
    # )


    print(member_manager.get())

    member_manager.close()