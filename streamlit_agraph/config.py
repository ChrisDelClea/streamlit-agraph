import json
import os
import streamlit as st


class Config:
  def __init__(self, height=750, width=750, directed=True, physics=True, hierarchical=False, from_json=None, **kwargs):
    self.height = f"{height}px"
    self.width = f"{width}px"
    if not directed:
      self.edges = {"arrows":"none"}

    # https://visjs.github.io/vis-network/docs/network/physics.html#
    self.physics = {"enabled": physics,
                    "solver":kwargs.get("solver", "barnesHut"),
                    "minVelocity":kwargs.get("minVelocity", 1),
                    "maxVelocity":kwargs.get("maxVelocity", 100),
                    "stabilization":{
                      "enabled": kwargs.get("stabilization", True),
                      "fit":kwargs.get("fit", True),
                      },
                    "timestep":kwargs.get("timestep", 0.5),
                    }
    # https://visjs.github.io/vis-network/docs/network/layout.html
    self.layout = {
        "hierarchical": {
          "enabled":hierarchical,
          "levelSeparation": kwargs.get("levelSeparation", 150),
          "nodeSpacing": kwargs.get("nodeSpacing", 100),
          "treeSpacing": kwargs.get("treeSpacing", 200),
          "blockShifting": kwargs.get("blockShifting", True),
          "edgeMinimization": kwargs.get("edgeMinimization", True),
          "parentCentralization": kwargs.get("parentCentralization", True),
          "direction": kwargs.get("direction", "UD"),        # UD, DU, LR, RL
          "sortMethod": kwargs.get('sortMethod', "hubsize"),  # hubsize, directed
          "shakeTowards": kwargs.get('shakeTowards', 'roots')  # roots, leaves
      }
    }
    self.groups = kwargs.get("groups", None)

    self.__dict__.update(**kwargs)

    if from_json:
        self.from_json(from_json)

  def to_dict(self):
    return self.__dict__

  def save(self, path):
      config_json = json.dumps(self.__dict__, indent=2)
      if os.path.isabs(path):
          save_path = path
      else:
          directory = os.getcwd()
          save_path = os.path.join(directory, path)
      with open(save_path, "w") as file:
          file.write(config_json)

  def from_json(self, path):
        with open(path, "r") as f:
            config_json = f.read()
        self.__dict__ = json.loads(config_json)


class ConfigBuilder(object):
    def __init__(self, nodes=None, edges=None, **kwargs):
        self.kwargs = {}
        self.nodes = nodes
        st.sidebar.write("Agraph Configurations")
        self.basic_widget = self.basic_widget()
        self.physics_widget = self.physics_widget()
        self.hierarchical_widget = self.hierarchical_widget()
        self.groups = self.group_widget()
        self.config = Config()

    def basic_widget(self):
        basic_expander = st.sidebar.expander("Basic Config", expanded=True)
        with basic_expander:
            basic_expander.number_input("height", value=750, key="height")
            basic_expander.number_input("width", value=750, key="width")
            basic_expander.checkbox("directed", value=True, key="directed")
            self.kwargs["height"] = st.session_state.height
            self.kwargs["width"] = st.session_state.width
            self.kwargs["directed"] = st.session_state.directed

    def physics_widget(self):
        physics_expander = st.sidebar.expander("Physics Config", expanded=False)
        with physics_expander:
            physics_expander.checkbox("physics", value=True, key="physics")
            physics_expander.selectbox("Solver",
                                       options=["barnesHut",
                                                "forceAtlas2Based",
                                                "hierarchicalRepulsion",
                                                "repulsion"],
                                       key="solver")
            physics_expander.number_input("minVelocity", value=1, key="minVelocity")
            physics_expander.number_input("maxVelocity", value=100, key="maxVelocity")
            physics_expander.checkbox("stabilize", value=True, key="stabilize")
            physics_expander.checkbox("fit", value=True, key="fit")
            physics_expander.number_input("timestep", value=0.5, key="timestep")

            self.kwargs["physics"] = st.session_state.physics
            self.kwargs["minVelocity"] = st.session_state.minVelocity
            self.kwargs["maxVelocity"] = st.session_state.maxVelocity
            self.kwargs["stabilization"] = st.session_state.stabilize
            self.kwargs["fit"] = st.session_state.fit
            self.kwargs["timestep"] = st.session_state.timestep
            self.kwargs["solver"] = st.session_state.solver

    def hierarchical_widget(self):
        hierarchical_expander = st.sidebar.expander("Hierarchical Config", expanded=False)
        with hierarchical_expander:

            def set_physics_off():
                if st.session_state.hierarchical:
                    st.session_state.physics = False

            hierarchical_expander.checkbox("hierarchical", value=False, key="hierarchical", on_change=set_physics_off)
            hierarchical_expander.number_input("levelSeparation", value=150, key="levelSeparation")
            hierarchical_expander.number_input("nodeSpacing", value=100, key="nodeSpacing")
            hierarchical_expander.number_input("treeSpacing", value=200, key="treeSpacing")
            hierarchical_expander.checkbox("blockShifting", value=True, key="blockShifting")
            hierarchical_expander.checkbox("edgeMinimization", value=True, key="edgeMinimization")
            hierarchical_expander.checkbox("parentCentralization", value=True, key="parentCentralization")
            hierarchical_expander.selectbox("direction", options=["UD", "DU", "LR", "RL"], key="direction")
            hierarchical_expander.selectbox("sortMethod", options=["hubsize", "directed"], key="sortMethod")
            hierarchical_expander.selectbox("shakeTowards", options=["roots", "leaves"], key="shakeTowards")
            self.kwargs.update({
                           "hierarchical": st.session_state.hierarchical,
                           "levelSeparation": st.session_state.levelSeparation,
                           "nodeSpacing": st.session_state.nodeSpacing,
                           "treeSpacing": st.session_state.treeSpacing,
                           "blockShifting": st.session_state.blockShifting,
                           "edgeMinimization": st.session_state.edgeMinimization,
                           "parentCentralization": st.session_state.parentCentralization,
                           "direction": st.session_state.direction,
                           "sortMethod": st.session_state.sortMethod,
                           "shakeTowards": st.session_state.shakeTowards
                           }
                          )

    def group_widget(self):
        group_expander = st.sidebar.expander("Group Config", expanded=False)
        group_expander.checkbox("groups", value=False, key="groups")
        if st.session_state.groups:
            if self.nodes:
                groups = list(set([node.__dict__.get("group", None) for node in self.nodes]))
                if None in groups:
                    groups.remove(None)
                with group_expander:
                    groups_dict = {}
                    for group in groups:
                        st.write(f"Group: {group}")
                        group_expander.text_input(f"Color (hex)", value=" #fe8a71", key=f"group_{group}")
                        groups_dict[group] = {"color": st.session_state[f"group_{group}"]}
                    self.kwargs.update({"groups": groups_dict})

    def build(self, dictify=False):
        # self.physics_widget()
        # self.hierarchical_widget()
        if dictify:
            return self.kwargs
        else:
            self.config = Config(**self.kwargs)
        return self.config