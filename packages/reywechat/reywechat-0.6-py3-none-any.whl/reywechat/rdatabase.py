# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2023-10-23 20:55:58
@Author  : Rey
@Contact : reyxbo@163.com
@Explain : Database methods.
"""


from reytool.rdatabase import REngine
from reytool.rprint import rprint


class RDatabase(object):
    """
    Rey's `database` type.
    """


    def __init__(
        self,
        rengine: REngine
    ) -> None:
        """
        Build `database` instance.

        Parameters
        ----------
        rengine : REngine instance.
        """

        # Set attribute.
        self.rengine = rengine




    def build_all(self): ...


class RDBBuild(object):
    """
    Rey's `database build` type.
    """


    def __init__(
        self,
        rengine: REngine
    ) -> None:
        """
        Build `database build` instance.

        Parameters
        ----------
        rengine : REngine instance.
        """

        # Set attribute.
        self.rengine = rengine


    def build(self) -> None:
        """
        Build all standard databases and tables.
        """

        # Set parameter.
        databases = [
            {
                "database": "wechat"
            }
        ]
        tables = [
            {
                "path": "wechat.receive_message",
                "fields": [
                    {
                        "name": "id",
                        "type_": "bigint",
                        "constraint": "NOT NULL",
                        "comment": "Message ID.",
                    },
                    {
                        "name": "room_id",
                        "type_": "varchar(20)",
                        "constraint": "DEFAULT NULL",
                        "comment": "Message room ID.",
                    },
                    {
                        "name": "receiver",
                        "type_": "varchar(24)",
                        "constraint": "NOT NULL",
                        "comment": "Message receiver ID.",
                    },
                    {
                        "name": "sender",
                        "type_": "varchar(24)",
                        "constraint": "NOT NULL",
                        "comment": "Message sender ID.",
                    },
                    {
                        "name": "type",
                        "type_": "int",
                        "constraint": "NOT NULL",
                        "comment": "Message type.",
                    },
                    {
                        "name": "content",
                        "type_": "bigint",
                        "constraint": "NOT NULL",
                        "comment": "Message content.",
                    },
                    {
                        "name": "xml",
                        "type_": "text",
                        "constraint": "DEFAULT NULL",
                        "comment": "Message XML content.",
                    },
                    {
                        "name": "file",
                        "type_": "text",
                        "constraint": "DEFAULT NULL",
                        "comment": "Message file path.",
                    }
                ],
                "primary": "id",
                "comment": "Receive message table."
            }
        ]

        # Build.
        self.rengine.build(databases, tables)