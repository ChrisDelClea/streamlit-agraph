
class Node:
  def __init__(self,
              id,
              title=None, # displayed if hovered
              label=None, # displayed inside the node
              color=None,
              shape="dot",
              size=25,
              **kwargs
               ):
    self.id=id
    if not title:
      self.title=id
    else:
     self.title=title
    self.label = label
    self.shape=shape # # image, circularImage, diamond, dot, star, triangle, triangleDown, hexagon, square and icon
    self.size=size
    self.color=color #FDD2BS #F48B94 #F7A7A6 #DBEBC2
    self.__dict__.update(**kwargs)

  def to_dict(self):
    return self.__dict__