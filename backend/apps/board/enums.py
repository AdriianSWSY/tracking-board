from enum import Enum


class BoardStatus(Enum):
    """Options for status fields for the Board entity"""
    active = "ACTIVE"
    archived = "ARCHIVED"
    deleted = "DELETED"
