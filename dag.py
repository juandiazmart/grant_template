import daft
from matplotlib import rc

rc("font", family="serif", size=12)
rc("text", usetex=True)

p_color = {"ec": "#46a546"}

pgm = daft.PGM()

# Data.
pgm.add_node("D", r"$D_{t,m}$", 2.5, 1, observed=True)
pgm.add_node("psi", r"$\psi$", 4, 1)
pgm.add_node("d", r"$d_{t,m}$", 2.5, 2,plot_params=p_color)
pgm.add_node("pi", r"$\pi_m$", 3.3, 3)
pgm.add_node("alphai", r"$\alpha_i$", 1.5, 2,plot_params=p_color)
pgm.add_node("xtm", r"$X_{i\,t,m}$", 2, 2.5,plot_params=p_color,observed=True)
pgm.add_node("alpha0", r"$\alpha_{0\,m}$", 3.3,2,plot_params=p_color)
pgm.add_node("ifr", r"$ifr_m$", 3.3, 3.7)
pgm.add_node("emp", r"$Emp$", 4, 3.7)
pgm.add_node("c", r"$c_{t,m}$", 2.5, 3)
pgm.add_node("g", r"$g$", 1.5, 4)
pgm.add_node("R", r"$R_{t,m}$", 2.5, 4,plot_params=p_color)
pgm.add_node("F", r"$F_{t,m}$", 2.5, 5,observed=True,plot_params=p_color)
pgm.add_node("R0", r"$R_{0,m}$", 3.3, 5)
pgm.add_node("beta0", r"$\beta_{0\,m}$", 2, 4.5,plot_params=p_color)
pgm.add_node("beta1", r"$\beta_{1\,m}$", 3.3, 4.3,plot_params=p_color)
pgm.add_node("kappa", r"$\kappa$", 3.3, 6)


# Add in the edges.
pgm.add_edge("d", "D")
pgm.add_edge("psi", "D")
pgm.add_edge("pi", "d")
pgm.add_edge("c", "d")
pgm.add_edge("alphai", "d")
pgm.add_edge("xtm", "d")
pgm.add_edge("alpha0", "d")
pgm.add_edge("ifr", "pi")
pgm.add_edge("emp", "pi")
pgm.add_edge("R", "c")
pgm.add_edge("g", "c")
pgm.add_edge("F", "R")
pgm.add_edge("R0", "R")
pgm.add_edge("beta0", "R")
pgm.add_edge("beta1", "R")
pgm.add_edge("kappa", "R0")


# And a plate.
pgm.add_plate([1.75, 0.5,1.8, 5], label=r"$t = 1,..., N$", shift=-0.1,fontsize=7,label_offset=[3, 3])
pgm.add_plate([1.75, 0.5, 1.8, 5], label=r"$m = 1,..., p$", shift=-0.1,fontsize=7,position="bottom right",label_offset=[1,3])
pgm.add_plate([1,1.7,1.25, 1.1], label=r"$i = 1,..., 3$", shift=-0.1,fontsize=7,position="top left",label_offset=[1,3])
# Render and save.
pgm.render()
pgm.savefig("dag_COVID.png", dpi=200)