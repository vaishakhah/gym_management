from mysql import connector
from datetime import datetime
class Dbconnect:
    def get_connected(self):
        try:
            self.connection = connector.connect(
                host="localhost",
                user="root",
                password="VAISHAKHah@2005",
                database="gym_db"
            )
            return self.connection
        except Exception as e:
            return None
class GymMemberManager(Dbconnect):
    def get_object(self,id=None):
        try:
            self.connect = super().get_connected()
            self.cursor = self.connect.cursor()
            query="select * from member where id =%s"
            values=(id,)
            self.cursor.execute(query,values)
            record = self.cursor.fetchone()
            return record
        except Exception as e:
            return None

    def get(self):
        try:
            self.connect = super().get_connected()
            self.cursor = self.connect.cursor()
            query = "select * from member"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            print(records)
        except Exception as e:
            print(e)
    def post(self,**kwargs):
        try:
            self.connect = super().get_connected()
            self.cursor = self.connect.cursor()
            query = "insert into member(name ,place,mobile,plan,fee,joined_date)values(%s,%s,%s,%s,%s,%s)"
            values = [v for v in kwargs.values()]
            self.cursor.execute(query, values)
            self.connect.commit()
            print("New member added successfully")
        except Exception as e:
            print(e)
    def retrieve(self,id=None):
        try:
            self.connect = super().get_connected()
            self.cursor = self.connect.cursor()
            query = "select * from member where id =%s"
            values =(id,)
            self.cursor.execute(query,values)
            records = self.cursor.fetchone()
            print(records)
        except Exception as e:
            print(e)
    def delete(self,id=None):
        try:
            self.connect = super().get_connected()
            self.cursor = self.connect.cursor()
            query = "select * from member where id =%s"
            values = (id,)
            self.cursor.execute(query,values)
            records = self.cursor.fetchone()
            if records !=None:
                query ="delete from member where id =%s"
                self.cursor.execute(query,values)
                self.connect.commit()
                print("Member deleted successfully")
            else:
                print("Member not found")
        except Exception as e:
            print(e)
    def put(self,id=None,**kwargs):
        try:
            record = self.get_object(id=id)
            if record != None:
                self.cursor = self.connection.cursor()
                placeholder =""
                for k in kwargs.keys():
                    placeholder += k+ "=%s, "
                placeholder = placeholder.rstrip(", ")
                query = f"update member set {placeholder}where id = %s"
                values = [v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query, values)
                self.connection.commit()
                print("Member updated successfully..")
            else:
                print("Member not found....")
        except Exception as e:
            print(e)


#
