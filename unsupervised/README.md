As discussed in the main paper, we took a 10 micro s sample of the 3 fibers models and we reduced the traj taking only the center of every monomer with a temporal stride of 10 nano s (obtaining a total of 1000 reduced frames).

The file *soap.inputs* contains the parameters for the SOAP calculation applyed to every center for every reduced frame.

The unsupervised clustering was done on a reduced dimensionality data set, we used PCA method and kept up to the first 3 components.
In the *pamm.inputs* file are stored the paramerets used to obtain the inidivdual PAMM clustering on the 3 fibers sets.
