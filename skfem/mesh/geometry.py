import numpy as np
from numpy import ndarray

from skfem import MappingIsoparametric
from skfem import Mesh


class Geometry(Mesh):
    """Degrees-of-freedom and their locations.

    Aims to be compatible with :class:`~skfem.mesh.Mesh`.

    """
    doflocs: ndarray = None
    dofnum = None

    def __init__(self, doflocs, dofnum):

        self.doflocs = doflocs
        self.dofnum = dofnum

    @property
    def refdom(self):
        return self.dofnum.element.refdom

    @property
    def brefdom(self):
        return self.dofnum.element.brefdom

    @property
    def p(self):
        return self.doflocs

    @property
    def t(self):
        return self.dofnum.topo.t

    @property
    def facets(self):
        return self.dofnum.topo.facets

    @property
    def t2f(self):
        return self.dofnum.topo.t2f

    @property
    def t2e(self):
        return self.dofnum.topo.t2e

    def mapping(self):
        return MappingIsoparametric(self, self.dofnum.element)

    def dim(self):
        return self.dofnum.element.dim
