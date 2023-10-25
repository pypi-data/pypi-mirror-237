#!/usr/bin/env python

from __future__ import annotations
from typing import Iterator, Optional, Union
from rdf.terms import BNode, IRIRef, Literal


_GRAPHLABEL_DEFAULT = IRIRef('')

class Statement(tuple):
    def __new__(cls, subject:Union[IRIRef, BNode], predicate:IRIRef,
                object:Union[IRIRef, BNode, Literal],
                graph_label:Optional[Union[BNode, IRIRef]] = None) -> None:
        if graph_label is None:
            graph_label = _GRAPHLABEL_DEFAULT

        return super().__new__(cls, (subject, predicate, object, graph_label))

    def __init__(self, subject:Union[IRIRef, BNode], predicate:IRIRef,
                 object:Union[IRIRef, BNode, Literal],
                 graph_label:Optional[Union[BNode, IRIRef]] = None) -> None:
        """ An RDF Statement; a triple or fact

        :param subject: The subject of the statement.
        :type subject: Union[IRIRef, BNode]
        :param predicate: The relation between the subject and the object.
        :type predicate: IRIRef
        :param object: The object of the statement
        :type object: Union[IRIRef, BNode, Literal]
        :param graph_label: An optional label referring to the named graph this
                            statement is a part of.
        :type graph_label: Optional[Union[BNode, IRIRef]]
        :rtype: None
        """
        self.subject = subject
        self.predicate = predicate
        self.object = object
        self.graph_label = graph_label if graph_label is not None\
                else _GRAPHLABEL_DEFAULT

    def __getnewargs__(self):
        return (self.subject, self.predicate, self.object, self.graph_label)

    def __iter__(self) -> Iterator:
        if self.graph_label is _GRAPHLABEL_DEFAULT:
            return iter((self.subject, self.predicate, self.object))
        
        return iter((self.subject, self.predicate, self.object,
                     self.graph_label))

    def __eq__(self, other:Statement) -> bool:
        for resourceA, resourceB in ((self.subject, other.subject),
                                     (self.predicate, other.predicate),
                                     (self.object, other.object),
                                     (self.graph_label, other.graph_label)):
            if resourceA != resourceB:
                return False

        return True

    def __lt__(self, other:Statement) -> bool:
        if self.graph_label < other.graph_label:
            return True

        if self.graph_label == other.graph_label:
            if self.predicate < other.predicate:
                return True

            if self.predicate == other.predicate:
                if self.subject < other.subject:
                    return True

                if self.subject == other.subject:
                    if self.object < other.object:
                        return True

        return False

    def __str__(self) -> str:
        out = "%s, %s, %s" % (str(self.subject),
                              str(self.predicate),
                              str(self.object))
        if self.graph_label is not _GRAPHLABEL_DEFAULT:
            out += ", %s" % str(self.graph_label)

        return "(" + out + ")"

    def __hash__(self) -> int:
        return hash(repr(self))
