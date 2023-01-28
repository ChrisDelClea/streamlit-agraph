

class Edge:
  """
  https://visjs.github.io/vis-network/docs/network/edges.html
  """
  def __init__(self,
               source,
               target,
               color="#F7A7A6",
               # arrows_to=True,
               # arrows_from=False,
               **kwargs
               ):
    self.source=source
    self.__dict__['from']=source
    self.to=target
    self.color=color
    # self.arrows={"to": arrows_to, "from": arrows_from}
    self.__dict__.update(**kwargs)

  def to_dict(self):
    return self.__dict__