from booklib.db import cnx


class Repository:
    def __init__(self):
        self.cnx = cnx
        self.table_name = ""
        self.columns = ()
        self.cursor = None

    def execute(self, query, params=None):
        self.cursor = self.cnx.cursor(buffered=True)
        self.cursor.execute(query, params)
        return self

    def commit(self):
        self.cnx.commit()
        return self

    def transform(self, columns, row):
        result = {}
        for key, value in zip(columns, row):
            result[key] = value
        return result

    def to_item(self, columns):
        row = self.cursor.fetchone()
        self.cursor.close()
        return self.transform(columns, row)

    def to_list(self, columns):
        result = []
        for row in self.cursor:
            item = self.transform(columns, row)
            result.append(item)
        self.cursor.close()
        return result

    def get_all(self):
        query = "SELECT * FROM {}".format(self.table_name)
        return self.execute(query).to_list(self.columns)

    def get_all_select(self, select):
        query = "SELECT {} FROM {}".format(", ".join(select), self.table_name)
        return self.execute(query).to_list(select)

    def filter_by_id(self, _id):
        query = "SELECT * FROM {} WHERE id=%s".format(self.table_name)
        return self.execute(query, (_id,)).to_item(self.columns)

    def filter_by(self, data):
        filter_query = " OR ".join(["".join([key, " = %s"]) for key in data])
        params = tuple(data.values())
        query = "SELECT * FROM {} WHERE {}".format(self.table_name, filter_query)
        return self.execute(query, params=params).to_list(self.columns)

    def create(self, data):
        columns = ", ".join(data.keys())
        values = ", ".join(["%s" for i in range(len(data))])
        params = tuple(data.values())
        query = "INSERT INTO {} ({}) VALUES ({})".format(
            self.table_name, columns, values
        )
        self.execute(query, params).commit()
        return self.filter_by_id(self.cursor.lastrowid)

    def update(self, _id, data):
        set_query = ", ".join(["".join([key, " = %s"]) for key in data])
        params = list(data.values())
        params.append(_id)
        params = tuple(params)
        query = "UPDATE {} SET {} WHERE id = %s".format(self.table_name, set_query)
        self.execute(query, params).commit()
        return self.filter_by_id(_id)

    def delete(self, _id):
        query = "DELETE FROM {} WHERE id = %s".format(self.table_name)
        return self.execute(query, (_id,)).commit()
