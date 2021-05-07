import json
import re
from jsonc_parser.errors import FileError, FunctionParameterError, ParserError
import os


class JsoncParser:

    # regex = re.compile(r"//.*?\n|/\*.*?\*/", re.MULTILINE | re.DOTALL)
    regex = re.compile(r"(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)", re.MULTILINE | re.DOTALL)
    newline_replace_regex = re.compile("\n{2,}", re.MULTILINE)

    def parse_str(_string: str) -> dict:
        """
        Parse JSON-as-string and deserialize its content into Python dictionary,
        ignoring any comments.

        Parameters: `_string:str` - path to file

        This function will raise a `FunctionParameterError` exception if `_string` parameter
        has an incorrect type or is empty.
        This function will raise a `ParserError` exception if file cannot be parsed.
        This function will raise any additional exceptions if occurred.
        """

        def __re_sub(match):
            if match.group(2) is not None:
                return ""
            else:
                return match.group(1)

        if type(_string) != str:
            raise FunctionParameterError(
                "_string parameter must be str; got {} instead".format(type(_string).__name__)
            )

        if not _string:
            raise FunctionParameterError("there is not JSONC to be parsed")

        json_file = open(_string, "r")
        data_raw = json_file.read()
        json_file.close()

        try:
            data = JsoncParser.regex.sub(__re_sub, data_raw)
            return json.loads(JsoncParser.regex.sub(__re_sub, data))
        except Exception as e:
            raise ParserError("{} file cannot be parsed (message: {})".format(_string, str(e)))

    @staticmethod
    def parse_file(filepath: str) -> dict:
        """
        Parse .jsonc file and deserialize its content into Python dictionary,
        ignoring any comments.

        Parameters: `filepath:str` - path to file

        This function will raise a `FunctionParameterError` exception if `filepath` parameter
        has an incorrect type or is empty.
        This function will raise a `FileError` exception if file format is unsupported.
        This function will raise a `ParserError` exception if file cannot be parsed.
        This function will raise any additional exceptions if occurred.
        """

        def __re_sub(match):
            if match.group(2) is not None:
                return ""
            else:
                return match.group(1)

        if type(filepath) != str:
            raise FunctionParameterError(
                "filepath parameter must be str; got {} instead".format(type(filepath).__name__)
            )

        if not filepath:
            raise FunctionParameterError("path is empty.")

        if not os.path.exists(filepath) or not os.path.isfile(filepath):
            raise FileError("{} does not exist or is not a file".format(filepath))

        if filepath.split(".")[-1] not in ["json", "jsonc"]:
            raise FileError("file {} has an unsupported extension.".format(filepath))

        json_file = open(filepath, "r")
        data_raw = json_file.read()
        json_file.close()

        try:
            data = JsoncParser.regex.sub(__re_sub, data_raw)
            return json.loads(JsoncParser.regex.sub(__re_sub, data))
        except Exception as e:
            raise ParserError("{} file cannot be parsed (message: {})".format(filepath, str(e)))

    @staticmethod
    def convert_to_json(filepath: str, remove_file: bool = False) -> None:
        """
        Convert file from .jsonc to .json format, removing any comments from it

        Parameters: `filepath:str` is a path to file, `remove_file:bool` indicates if source file
        will be deleted or not. If set to True, .jsonc file will be deleted from the hard drive,
        otherwise file remains alongside with its .json output.

        This function will raise a `FunctionParameterError` if one or more of function's parameters
        has an incorrect type/invalid value.
        This function will raise any additional exceptions if occurred.

        """

        if type(filepath) != str:
            raise FunctionParameterError(
                "filepath parameter must be str; got {} instead".format(type(filepath).__name__)
            )

        if not filepath:
            raise FunctionParameterError("path is empty.")

        if type(remove_file) != bool:
            raise FunctionParameterError(
                "remove_file parameter must be bool; got {} instead.".format(
                    type(remove_file).__name__
                )
            )

        data = JsoncParser.parse_file(filepath)

        if remove_file:
            os.remove(filepath)

        new_filename = os.path.splitext(filepath)[0] + ".json"
        if os.path.exists(new_filename) and os.path.isfile(new_filename):
            raise FileError("{} file already exists".format(new_filename))

        json_file = open(new_filename, "x")
        json_file.write(json.dumps(data, indent=2))
        json_file.close()

    @staticmethod
    def convert_to_jsonc(filepath: str, remove_file: bool = False):
        """
        Convert file .jsonc format, enabling comments.

        Parameters: `filepath:str` is a path to file, `remove_file:bool` indicates if source file
        will be deleted or not. If set to True, .json file will be deleted from the hard drive,
        otherwise file remains alongside with its .jsonc output.

        This function will raise a `FunctionParameterError` if one or more of function's parameters
        has an incorrect type/invalid value.
        This function will raise any additional exceptions if occurred.
        """
        if type(filepath) != str:
            raise FunctionParameterError(
                "filepath parameter must be str; got {} instead".format(type(filepath).__name__)
            )

        if not filepath:
            raise FunctionParameterError("path is empty.")

        if type(remove_file) != bool:
            raise FunctionParameterError(
                "remove_file parameter must be bool; got {} instead.".format(
                    type(remove_file).__name__
                )
            )

        data = JsoncParser.parse_file(filepath)

        if remove_file:
            os.remove(filepath)

        new_filename = os.path.splitext(filepath)[0] + ".jsonc"
        if os.path.exists(new_filename) and os.path.isfile(new_filename):
            raise FileError("{} file already exists".format(new_filename))

        json_file = open(new_filename, "x")
        json_file.write(json.dumps(data, indent=2))
        json_file.close()
