
<link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Work+Sans&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Roboto+Mono&display=swap" rel="stylesheet">

<style type='text/css' rel='stylesheet'>
    #package-name {
        font-family: 'Work Sans', sans-serif;
        line-height: normal;
        font-weight: 600;
        font-size: 220%
    }
    .package-desc {
        font-family: 'Work Sans', sans-serif;
        line-height: normal;
    }
    .overview-code {
        font-family: 'Roboto Mono', sans-serif;
        display: inline;
    }
    .overview-important {
        font-size: 150%;
        font-family: 'Work Sans', sans-serif;
    }
</style>

<p id='package-name'>jsonc-parser</p>
<hr>
<p class='package-desc'>This package is a lightweight, zero-dependency module for parsing files with <span class='overview-code' style='display: inline'>.jsonc</span> extension. (<i>a.k.a. JSON with comments</i>) </p>
<p class='overview-important'>Installation</p>
<p class='package-desc'>To install this package, simply download it from <a href='' target='_blank'>PyPI:</a></p>

    pip install jsonc-parser

<p class='package-desc'>Also you can build it yourself from source code available on <a href='' target='_blank'>GitHub</a></p>

<p class='overview-important'>Usage</p>
<p class='package-desc'>You need to just import <span class='overview-code'>JsoncParser</span> class from this package:</p>

    from jsonc_parser.parser import JsoncParser

<p class='package-desc'>This class requires no instance to function (i.e. it is fully static)</p>

<link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Work+Sans&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Roboto+Mono&display=swap" rel="stylesheet">

<style rel=stylesheet' type='text/css'>
    #functions {
        font-family: 'Work Sans', sans-serif;
        font-size: 2.1em;
        line-height: normal
    }
    .functions-desc-general {
        font-size: 1em;
        font-family: 'Work Sans', sans-serif;
        line-height: normal;
        padding-bottom: 14px;
    }

    .functions-code {
        font-family: 'Roboto Mono', sans-serif;
        display: inline;
    }
    .functions-declaration {
        font-weight: bold;
        font-size: 1.1em;
    }
</style>

<p id='functions'>Functions</p>
<p class='functions-desc-general'>These are all methods that <span class='functions-code'>JsoncParser</span> class provides for working with <span class='functions-code'>.jsonc</span> files:</p>

-   <p class='functions-declaration functions-code'>JsoncParser.parse_file(filepath: str) -> dict</p>
    <p class='functions-desc-general'>This function parses file, specified in <span class='functions-code'>filepath</span> parameter, and deserializes it into a valid Python object (dictionary), removing any comment in the process. No alterations are made it the file itself. <span class='functions-code'>filepath</span> parameter specifies path to <span class='functions-code'>.jsonc</span> file.</p>

        from jsonc-parser.parser import JsoncParser

        file_path = "./data.jsonc"
        # Content from 'data.jsonc' -> {"version": "1.0.0", /*This is my project's version*/}

        data = JsoncParser.parse_file(file_path)

        print(data)
        # Output: {'version': '1.0.0'}

    <p class='functions-desc-general'>This function can raise <span class='functions-code'><a href='#exc-incorrect-parameter-error'>FunctionParameterError</a></span> if <span class='functions-code'>filepath</span> parameter is not a string or is empty. Also this function will raise <span class='functions-code'><a href='#exc-file-error'>FileError</a></span> exception if file's format is unsupported and a <span class='functions-code'><a href='#exc-parser-error'>ParserError</a></span> exception if file cannot be parsed/contains invalid JSON data.</p>

-   <p class='functions-declaration functions-code'>JsoncParser.convert_to_json(filepath: str, remove_file: bool = False) -> None</p><p class='functions-desc-general'>This function converts file from <span class='functions-code'>.jsonc</span> to <span class='functions-code'>.json</span> format, removing any comments in the process. <span class='functions-code'>filepath</span> parameter specifies path to file and <span class='functions-code'>remove_file</span> parameter specifies if <span class='functions-code'>.jsonc</span> file will be removed (deleted from hard drive) after conversion. If set to True, this function will delete <span class='functions-code'>.jsonc</span> file leaving only <span class='functions-code'>.json</span> file. Otherwise, both files are not deleted.</p>
    <p class='functions-desc-general'>This function can raise <span class='functions-code'><a href='#exc-incorrect-parameter-error'>FunctionParameterError</a></span> if <span class='functions-code'>filepath</span> parameter is not a string or is empty or if <span class='functions-code'>remove_file</span> parameter is not a boolean.</p>

-   <p class='functions-declaration functions-code'>JsoncParser.convert_to_jsonc(filepath: str, remove_file: bool = False) -> None</p><p class='functions-desc-general'>This function converts file from <span class='functions-code'>.json</span> to <span class='functions-code'>.jsonc</span> format, enabling comment support. <span class='functions-code'>filepath</span> parameter specifies path to file and <span class='functions-code'>remove_file</span> parameter specifies if <span class='functions-code'>.jsonc</span> file will be removed (deleted from hard drive) after conversion. If set to True, this function will delete <span class='functions-code'>.jsonc</span> file leaving only <span class='functions-code'>.json</span> file. Otherwise, both files are not deleted.</p>
    <p class='functions-desc-general'>This function can raise <span class='functions-code'><a href='#exc-incorrect-parameter-error'>FunctionParameterError</a></span> if <span class='functions-code'>filepath</span> parameter is not a string or is empty or if <span class='functions-code'>remove_file</span> parameter is not a boolean.</p>

<link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Work+Sans&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Roboto+Mono&display=swap" rel="stylesheet">
<style rel='stylesheet' type='text/css'>
    .exc-code {
        font-family: 'Roboto Mono', sans-serif;
        display: inline
    }
    * {
        font-family: 'Work Sans', sans-serif;
        line-height: normal
    }
</style>

<style rel='stylesheet' type='text/css'>
    .exc-header {
        display: block;
        font-size: 1.1em;
        font-weight: bold;
    }
    .exc-desc {
        font-size: 1em;
    }
    .exc-block {
        padding-top: 14px
    }
    #exceptions-module {
        font-size: 2.1em;
        padding-bottom: 4px
    }
</style>

<div id='exceptions-module'>Exceptions</div>

<p id='exceptions-module-overview'>There are a total of <b>3</b> custom exceptions that <span class='exc-code'>jsonc-parser</span> can raise during its runtime. To access the in your script, simply imprt thef from <span class='exc-code'>jsonc_parser.errors</span> module:</p>

    from jsonc_parser.errors import FileError, IncorrectParameterError, ParserError

<p style='font-family: "Work Sans", sans-serif; font-size: 1.3em; line-height: normal'>Exceptions:</p>

-   <p class='exc-block'><p class='exc-header exc-code' id='exc-file-error'>FileError</p>
    <p class='exc-desc'>This exception indicates that there is a problem with selected file.</p></p>

-   <p class='exc-block'><p class='exc-header exc-code' id='exc-incorrect-parameter-error'>IncorrectParameterError</p>
    <p class='exc-desc'>This exception indicates that some of function's parameters are invalid. They may have wrong type, have invalid values or be errorous in some other way.</p></p>

-   <p class='exc-block'><p class='exc-header exc-code' id='exc-parser-error'>ParserError</p><p class='exc-desc'>This exception indicates that file cannot be parsed. It can have wrong extension, invalid data, etc</p></p>

