from operator import itemgetter
from itertools import count
from copy import copy

from anytree import Node, RenderTree, PostOrderIter

from mathesis.deduction.sequent_calculus import Sequent, SequentTree, sign


class DerivationTree:
    def __init__(self, premises, conclusions):
        self._tableau = SequentTree(premises, conclusions)
        self.bookkeeper = self._tableau.bookkeeper
        self.counter = self._tableau.counter

    def __getitem__(self, index):
        return self.bookkeeper[index]

    def apply(self, target: Node, rule):
        self._tableau.apply(target, rule)
        return self

    def tree(self, number=True):
        return self._tableau.tree()

    def latex(self, number=False, arrow=r"\Rightarrow"):
        output = ""
        for node in PostOrderIter(self.root):
            tmpl = ""
            if len(node.children) == 0:
                tmpl = r"\AxiomC{{${}$}}"
            elif len(node.children) == 1:
                tmpl = r"\UnaryInfC{{${}$}}"
            elif len(node.children) == 2:
                tmpl = r"\BinaryInfC{{${}$}}"
            output += tmpl.format(node.sequent.latex()) + "\n"
        return """\\begin{{prooftree}}\n{}\\end{{prooftree}}""".format(output)
