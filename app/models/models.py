from .db import Database

class Model:
    def __init__(self):
        self.db = Database()

    def createFlag(self, location, description, createdby, table_name):
        result = self.remove_quots(table_name)
       	query = "INSERT INTO {} (location, description,createdby) VALUES ('{}','{}','{}') RETURNING flag_id".format(result,
            location, description, createdby)
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


    def update_status(self, updt,data, table_name, flag_id):
        result = self.remove_quots(table_name)
        update = self.remove_quots(updt)
        qury = "SELECT * FROM {} WHERE flag_id = '{}' ".format(result, flag_id)
        res = self.db.fetch_one(qury)
        if not res:
            return {'message': 'id doesnot exist'}
        query = "UPDATE {} SET {} ='{}' WHERE flag_id = {} ".format(result, update, data, flag_id)
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

    def update_data(self, updt, flag_id,data, table_name,createdby):
        table =self.remove_quots(table_name)
        update = self.remove_quots(updt)
        result = self.get_by_id(flag_id, table,createdby)
        if result and result['status'] == 'none':
            
            query = "UPDATE {} SET {} ='{}' WHERE flag_id = {} AND createdby ={} ".format(table, update, data, flag_id, createdby)
            self.db.cursor.execute(query)
            self.db.connection.commit()
            message = {
                'status': 200,
                'data': [
                    {   'id': flag_id,
                      'message': 'updated {} record {}'.format(table_name, updt)
                      }]
            }
            return message
        return {'message': 'id doesnt exist or it cant be edited'}
    

    def get_by_id(self, flag_id, table_name,createdby):
        query = "SELECT * FROM {} WHERE flag_id = '{}' AND createdby = {}".format(table_name, flag_id, createdby)

        return self.db.fetch_one(query)

    

    def get_all(self, table_name,createdby,isAdmin):
        table = self.remove_quots(table_name)
        
        if isAdmin == True:
            query = "SELECT * FROM {}".format(table)
            result = self.db.fetch_all(query)
            return {'status': 200, '{}'.format(table): result}
        
        query = "SELECT * FROM {} WHERE createdby = {}".format(table,createdby)
        result = self.db.fetch_all(query)
        return {'{}'.format(table): result}


    
    def delete(self, flag_id, table_name, createdby):
        result = self.remove_quots(table_name)
        res = self.get_by_id(flag_id, result, createdby)
        if res and res['status']== "none":
            query = "DELETE FROM {} WHERE flag_id = '{}' AND createdby = {} RETURNING flag_id".format(result,flag_id,createdby)
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
        return {'message': 'record either cannot be deleted or it doesnt exist in {}'.format(result)}
    """get one"""

    def get_one(self, flag_id, table_name,createdby):
        result = self.remove_quots(table_name)
        flag = self.get_by_id(flag_id, result,createdby)
        if flag:
            return flag
        return {'message': 'flag with that id doesnot exist'}

    def remove_quots(self,param):
        return param.replace('"','')