from .db import Database

class Model:
    def __init__(self):
        self.db = Database()

    def createFlag(self, location, description, image, video, createdby, table_name):
        result = self.remove_quots(table_name)
       	query = "INSERT INTO {} (location, description, image,video,createdby) VALUES ('{}','{}','{}','{}','{}') RETURNING flag_id".format(result,
            location, description, image, video, createdby)
        self.db.cursor.execute(query)
        res = self.db.cursor.fetchone()
        message = {
            'status': 201,
            'data': [
                {
                    'id': res[0],
                    'message':'created {}'.format(result)
                    }]
        }
        return message
    def update_data(self,updt,flag_id, data, table_name):
        table =self.remove_quots(table_name)
        update = self.remove_quots(updt)
        result = self.get_by_id(flag_id, table)
        if result:
            return self.update(update,data, table, flag_id)
        return {'message': 'id doesnt exist or it cant be edited'}


    def update(self, updt,data, table_name, flag_id):

        query = "UPDATE {} SET {} ='{}' WHERE flag_id = {} ".format(table_name, updt, data, flag_id)
        self.db.cursor.execute(query)
        self.db.connection.commit()
        message = {
            'status': 200,
            'data': [
                {	'id': flag_id,
                  'message': 'udated {} record {}'.format(table_name, updt)
                  }]
        }
        return message
    
    def update_status(self, updt,status, table_name, flag_id):
        result = self.remove_quots(table_name)
        update = self.remove_quots(updt)
        res = self.get_by_id(flag_id, result)
        if res:
            return self.update(update,status, result, flag_id)
        return {'message': 'id doesnot exist'}


    def get_by_id(self, flag_id, table_name):
        query = "SELECT * FROM {} WHERE flag_id = '{}'".format(table_name,flag_id)

        return self.db.fetch_one(query)

    def get_all(self, table_name):
        result = self.remove_quots(table_name)
        query = "SELECT * FROM {}".format(result)
        result = self.db.fetch_all(query)
        return {'status': 200, '{}'.format(table_name): result}


    def delete(self, flag_id, table_name):
        result = self.remove_quots(table_name)
        res = self.get_by_id(flag_id, result)
        if res:
            query = "DELETE FROM {} WHERE flag_id = '{}' RETURNING flag_id".format(result,flag_id)
            self.db.cursor.execute(query)
            _id = self.db.cursor.fetchone()
            message = {
                'status': 202,
                'data': [
                    {	'id': _id[0],
                      'message':'{} record has been deleted'.format(result)
                      }]
            }
            return message
        return {'message': 'id doesnt exist in {}'.format(result)}
    """get one"""

    def get_one(self, flag_id, table_name):
        result = self.remove_quots(table_name)
        flag = self.get_by_id(flag_id, result)
        if flag:
            return flag
        return {'message': 'flag with that id doesnot exist'}

    def remove_quots(self,param):
        return param.replace('"','')