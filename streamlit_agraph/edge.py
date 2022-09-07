

class Edge:
  """
  https://visjs.github.io/vis-network/docs/network/edges.html
  """
  def __init__(self,
               source,
               target,
               color="#F7A7A6",
               **kwargs
               ):
    self.source=source
    self.__dict__['from']=source
    self.to=target
    self.color=color
    self.__dict__.update(**kwargs)

  def to_dict(self):
    return self.__dict__