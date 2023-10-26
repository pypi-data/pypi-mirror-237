# -*- coding: utf-8 -*-
"""
@Author : zhang.yonggang
@File   : dlt_filter.py
@Project: pydlt
@Time   : 2023-10-25 15:28:03
@Desc   : The file is ...
@Version: v1.0
"""
import os.path

import json

from pydlt_plus import DltFileReader


def deal_output(msg, output_content, type_code, f_word=None):
    msg = msg.strip()
    if type_code == 0:
        output_content.append(msg)
    elif type_code == 1 and f_word:
        if f_word in output_content:
            output_content[f_word].append(msg)
        else:
            output_content[f_word] = [msg]
    elif type_code == 2:
        try:
            with open(output_content, 'a', encoding='utf-8') as file:
                file.write(f"{msg} {os.linesep}")
        except IOError:
            print('cannot open file {}'.format(output_content))
    return output_content


class DltFileFilter(DltFileReader):
    """
    A class to read and filter DLT message from DLT file BASE ON DltFileReader.
    Examples::
        # create reader as context manager
        with DltFileFilter("filepath") as reader:
            # read 1 message from file
            message = reader.read_message()

            # read all messages from file
            messages = reader.read_messages()

        # create reader as iterator
        for message in DltFileFilter("filepath"):  # read all messages
            # handle each message
        # filter info
        dff = DltFileFilter("log_2020-01-01_00.00.10.4.dlt", "utf8")
        dff.read_file(["abc", "神奈川県"], output_type="aaaa.txt")
        # translate dlt to other types
        dff.read_file(output_type="aaaa.txt")
    """
    def __init__(self, dlt_file_path, encoding="utf8"):
        if not os.path.exists(dlt_file_path):
            raise FileExistsError
        super(DltFileFilter, self).__init__(dlt_file_path, encoding)

    def read_file(self, filter_info=None, output_type="list"):
        """
        read and filter DLT message
        :param filter_info: filter_info could be a list or string or None(Not input).
        :param output_type: output_type could be a list or text(.txt or .log) or dict.
        :return:
        """
        if isinstance(filter_info, str):
            filter_info = [filter_info]
        # type_code: 0 is list, 1 is json file, 2 is text
        if output_type.lower() == "list":
            output_content = []
            type_code = 0
        elif output_type.lower().endswith(".json"):
            output_content = {}
            type_code = 1
        elif output_type.lower().endswith(".txt") or output_type.lower().endswith(".log"):
            type_code = 2
            output_content = output_type
        for msg in self.__iter__():
            msg = str(msg)
            if filter_info:
                for f_word in filter_info:
                    if f_word in msg:
                        output_content = deal_output(msg, output_content, type_code, f_word)
            else:
                output_content = deal_output(msg, output_content, type_code)
        if type_code == 1:
            with open(output_type, 'w', encoding='utf-8') as json_file:
                json.dump(output_content, json_file, ensure_ascii=False, indent=4)
        return output_content
