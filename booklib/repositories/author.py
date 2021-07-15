from .base import Repository

class AuthorRepository(Repository):
  def __init__(self, cnx):
    Repository.__init__(self, cnx)
    self.columns = ("id", "name", "created_at", "updated_at")

  def get_all(self):
    query = "SELECT * FROM authors"

    return self.execute(query).to_list(self.columns)

  def filter_by_id(self, id):
    query = "SELECT * FROM authors WHERE id=%s"

    return self.execute(query, (id,)).to_item(self.columns)
  
  def create(self, data):
    columns = ", ".join(data.keys())
    values = ", ".join(["%s" for i in range(len(data))])
    params = tuple(data.values())
    query = "INSERT INTO authors ({}) VALUES ({})".format(columns, values)

    return self.execute(query, params).commit()
  
  def update(self, id, data):
    set_query = ", ".join(["".join([key, " = %s"]) for key in data])
    params = list(data.values())
    params.append(id)
    params = tuple(params)
    query = "UPDATE authors SET {} WHERE id = %s".format(set_query)

    return self.execute(query, params).commit()
  
  def delete(self, id):
    query = "DELETE FROM authors WHERE id = %s"

    return self.execute(query, (id,)).commit()