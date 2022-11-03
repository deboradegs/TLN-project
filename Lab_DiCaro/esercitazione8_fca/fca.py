import concepts

c = concepts.load_csv("fca_hp.csv")


c.lattice.graphviz(view=True)