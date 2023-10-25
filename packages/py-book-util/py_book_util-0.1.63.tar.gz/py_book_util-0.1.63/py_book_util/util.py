# https://www.cnblogs.com/superbaby11/p/15560994.html
from threading import Thread
import io
import os
from contextlib import contextmanager


def run_cmd(cmd):
    """Run shell command and return command output.

    Examples:
        >>> run_cmd("cd ..")
        ''

    Args:
        cmd (string): A shell command.

    Returns:
        string: Command output.
    """
    import subprocess

    return subprocess.getoutput(cmd)


def run_deno_cmd(cmd):
    from pathlib import Path

    return run_cmd(str(Path.home()) + "/.deno/bin/" + cmd)


def print_run_cmd(cmd):
    import subprocess

    # http://blog.kagesenshi.org/2008/02/teeing-python-subprocesspopen-output.html
    p = subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        encoding="utf-8",
        errors="replace",
    )
    stdout_buffer = []
    while True:
        line = p.stdout.readline()
        stdout_buffer.append(line)
        print(line, end="")
        if line == "" and p.poll() != None:
            break
    return "".join(stdout_buffer)


def create_text_file(file_name, file_content):
    with open(file_name, "w") as file:
        file.write(file_content)


# https://www.jb51.net/article/232129.htm
class MyThread(Thread):
    def __init__(
        self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None
    ):
        super().__init__()
        self.fun = target
        self.args = args
        self.kwargs = kwargs

    def run(self):
        self.fun(*self.args, **self.kwargs)


def thread_run_cmd(cmd):
    t = MyThread(target=run_cmd, args=(cmd,), kwargs={})
    t.start()
    # t.join()


def thread_run_deno_cmd(cmd):
    t = MyThread(target=run_deno_cmd, args=(cmd,), kwargs={})
    t.start()
    # t.join()


def get_page_content(url):
    # https://www.cnblogs.com/herbert/p/10789343.html
    # https://www.selenium.dev/documentation/webdriver/drivers/remote_webdriver/#tabs-1-1
    from selenium import webdriver
    import time
    import os

    # https://blog.csdn.net/ad72182009/article/details/116117744
    if "http_proxy" in os.environ:
        del os.environ["http_proxy"]
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Remote(
        command_executor="http://127.0.0.1:4444/wd/hub", options=chrome_options
    )
    driver.get(url=url)
    # Wait some time for page loading
    time.sleep(4)
    found_page_source = driver.page_source
    driver.close()
    return found_page_source


def display_code(content):
    from IPython.display import Code

    return Code(data=content)


def display_iframe(url):
    from IPython.display import IFrame

    return IFrame(src=url, width="100%", height=300)


def get_file_md5sum(file):
    import hashlib
    import os

    if not os.path.exists(file):
        return "md5sum: {}: No such file or directory".format(file)
    elif os.path.isdir(file):
        return "md5sum: {}: Is a directory".format(file)
    elif os.path.isfile(file):
        with open(file, "rb") as fd:
            data = fd.read()
        # return "{}  {}".format(hashlib.md5(data).hexdigest(), file)
        return hashlib.md5(data).hexdigest()
    else:
        return "md5sum: {}: Unexpected error".format(file)


def get_str_md5sum(content):
    import hashlib

    return hashlib.md5(content.encode("utf8")).hexdigest()


def append_text_file(file_name, file_content):
    with open(file_name, "a") as file:
        file.write(file_content)


def replace_line_in_file(file_path, old_line_number, new_line_content):
    import fileinput

    line_number = 0
    with fileinput.FileInput(file_path, inplace=True) as f:
        for line in f:
            line_number = line_number + 1
            if line_number == old_line_number:
                print(new_line_content, end="")
            else:
                print(line, end="")


def insert_line_at_top_of_file(file_path, new_line_content, new_line_content_end="\n"):
    import fileinput

    flag_inserted = False
    with fileinput.FileInput(file_path, inplace=True) as f:
        for line in f:
            if flag_inserted == False:
                print(new_line_content, end=new_line_content_end)
                flag_inserted = True
            print(line, end="")


def add_line_in_file(
    file_path, old_line_number, new_line_content, new_line_content_end="\n"
):
    import fileinput

    line_number = 0
    with fileinput.FileInput(file_path, inplace=True) as f:
        for line in f:
            line_number = line_number + 1
            if line_number == old_line_number:
                print(new_line_content, end=new_line_content_end)
            print(line, end="")


def del_line_in_file(file_path, old_line_number):
    import fileinput

    deleted_line = ""
    line_number = 0
    with fileinput.FileInput(file_path, inplace=True) as f:
        for line in f:
            line_number = line_number + 1
            if line_number == old_line_number:
                deleted_line = line
            else:
                print(line, end="")
    return deleted_line


def del_line_block_in_file(file_path, old_line_number_begin, old_line_number_end):
    import fileinput

    deleted_line = ""
    line_number = 0
    with fileinput.FileInput(file_path, inplace=True) as f:
        for line in f:
            line_number = line_number + 1
            if old_line_number_begin == line_number:
                deleted_line = line
            else:
                if (
                    old_line_number_begin < line_number
                    and line_number <= old_line_number_end
                ):
                    deleted_line = deleted_line + line
                else:
                    print(line, end="")
    return deleted_line


def move_line_in_file(file_path, old_line_number, new_line_number):
    if old_line_number <= new_line_number and new_line_number <= (old_line_number + 1):
        return ""
    else:
        new_line_content = del_line_in_file(file_path, old_line_number)
        if old_line_number > new_line_number:
            add_line_in_file(file_path, new_line_number, new_line_content, "")
        else:
            add_line_in_file(file_path, new_line_number - 1, new_line_content, "")


def move_line_block_in_file(
    file_path, old_line_number_begin, old_line_number_end, new_line_number
):
    if old_line_number_begin <= new_line_number and new_line_number <= (
        old_line_number_end + 1
    ):
        return
    else:
        new_line_content = del_line_block_in_file(
            file_path, old_line_number_begin, old_line_number_end
        )
        if old_line_number_begin > new_line_number:
            add_line_in_file(file_path, new_line_number, new_line_content, "")
        else:
            add_line_in_file(
                file_path,
                new_line_number - (old_line_number_end - old_line_number_begin + 1),
                new_line_content,
                "",
            )


def read_text_file(file_path):
    from pathlib import Path

    return Path(file_path).read_text()


def display_text(content):
    from IPython.display import Code

    return Code(data=content, language="text")


def remove_indent_space_in_file(
    file_path, block_line_begin, block_line_end, indent_space_number
):
    import fileinput

    line_number = 0
    with fileinput.FileInput(file_path, inplace=True) as f:
        for line in f:
            line_number = line_number + 1
            if line_number >= block_line_begin and line_number <= block_line_end:
                if len(line) < indent_space_number:
                    print(line, end="")
                else:
                    new_line_content = line[indent_space_number:]
                    print(new_line_content, end="")
            else:
                print(line, end="")


def rstrip_space_in_file(file_path, line_number):
    import fileinput

    cur_line_number = 0
    with fileinput.FileInput(file_path, inplace=True) as f:
        for line in f:
            cur_line_number = cur_line_number + 1
            if line_number == cur_line_number:
                print(line.rstrip() + "\n", end="")
            else:
                print(line, end="")


def display_image(img_file):
    from IPython.display import Image

    return Image(img_file)


def del_block_in_file(file_path, block_line_begin, block_line_end):
    import fileinput

    line_number = 0
    with fileinput.FileInput(file_path, inplace=True) as f:
        for line in f:
            line_number = line_number + 1
            if line_number >= block_line_begin and line_number <= block_line_end:
                pass
            else:
                print(line, end="")


def full_page_snapshot(url, dir_snapshot):
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time
    import os

    assert os.path.isdir(dir_snapshot)
    if "http_proxy" in os.environ:
        del os.environ["http_proxy"]
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver = webdriver.Remote(
        command_executor="http://127.0.0.1:4444/wd/hub", options=chrome_options
    )
    driver.maximize_window()
    driver.get(url=url)
    # Wait some time for page loading
    time.sleep(4)
    found_page_source = driver.page_source
    try:
        span_collapse = driver.find_element(by=By.XPATH, value='//span[text()="«"]')
        span_collapse.click()
    except Exception as e:
        print(e)
    driver.save_screenshot(dir_snapshot + os.path.sep + "screenshot.png")

    main_scroll_height = 0
    main_scroll_top = 0
    page_height = 0
    flag_main_element = False
    try:
        main_scroll_height = driver.execute_script(
            "return document.getElementById('MAIN').scrollHeight"
        )
        main_scroll_top = driver.execute_script(
            "return document.getElementById('MAIN').scrollTop"
        )
        page_height = driver.execute_script("return document.body.scrollHeight")
        flag_main_element = True
    except Exception as e:
        print(e)
        main_scroll_height = driver.execute_script(
            "return document.body.parentNode.scrollHeight"
        )
        main_scroll_top = driver.execute_script(
            "return document.body.parentNode.scrollTop"
        )
        page_height = driver.execute_script("return window.innerHeight")

    print(
        "main_scroll_height is %d main_scroll_top is %d page_height is %d"
        % (main_scroll_height, main_scroll_top, page_height)
    )
    while True:
        driver.execute_script("window.scrollBy(0, %d);" % page_height)
        time.sleep(1)
        if flag_main_element:
            new_main_scroll_height = driver.execute_script(
                "return document.getElementById('MAIN').scrollHeight"
            )
        else:
            new_main_scroll_height = driver.execute_script(
                "return document.body.parentNode.scrollHeight"
            )
        if new_main_scroll_height == main_scroll_height:
            break
        main_scroll_height = new_main_scroll_height
        print("main_scroll_height is %d" % main_scroll_height)

    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)
    page_index = 1
    driver.save_screenshot(dir_snapshot + os.path.sep + ("page_%06d.png" % page_index))

    if flag_main_element:
        main_scroll_height = driver.execute_script(
            "return document.getElementById('MAIN').scrollHeight"
        )
        page_height = driver.execute_script("return document.body.scrollHeight")
    else:
        main_scroll_height = driver.execute_script(
            "return document.documentElement.scrollHeight"
        )
        page_height = driver.execute_script("return window.innerHeight")

    window_page_y_offset = driver.execute_script("return window.pageYOffset")
    print(
        "page_index is %d window_page_y_offset is %d main_scroll_height is %d page_height is %d"
        % (page_index, window_page_y_offset, main_scroll_height, page_height)
    )

    while (int(window_page_y_offset) + int(page_height) < int(main_scroll_height)) and (
        page_index < 100
    ):
        driver.execute_script("window.scrollBy(0, %d);" % page_height)
        time.sleep(1)
        last_window_page_y_offset = window_page_y_offset
        window_page_y_offset = driver.execute_script("return window.pageYOffset")
        if int(last_window_page_y_offset) == int(window_page_y_offset):
            print(
                "last_window_page_y_offset == window_page_y_offset == %d"
                % window_page_y_offset,
            )
            break
        page_index = page_index + 1
        driver.save_screenshot(
            dir_snapshot + os.path.sep + ("page_%06d.png" % page_index)
        )
        print(
            "page_index is %d window_page_y_offset is %d main_scroll_height is %d page_height is %d"
            % (page_index, window_page_y_offset, main_scroll_height, page_height)
        )
    assert page_index < 100
    driver.save_screenshot(dir_snapshot + os.path.sep + "screenshot_last_page.png")
    driver.close()
    return page_index


def find_line_in_file(file_path, line_content, search_line_number_begin=0):
    import fileinput

    line_number = 0
    with fileinput.FileInput(file_path, mode="r") as f:
        for line in f:
            line_number = line_number + 1
            if line_number < search_line_number_begin:
                continue
            if line_content == line:
                return line_number
    return 0


def dev_checkout_file(filename):
    cmd_ret = run_cmd("git log -1 -- %s" % filename)
    if cmd_ret == "":
        import os

        if os.path.isfile(filename):
            os.remove(filename)
        else:
            parent_dir = os.path.dirname(filename)
            if parent_dir.strip().__len__() > 0:
                if not os.path.isdir(parent_dir):
                    os.makedirs(parent_dir)
    else:
        print_run_cmd("git checkout %s" % filename)


def dev_show_diff(filename):
    cmd_ret = run_cmd("git log -1 %s" % filename)
    if cmd_ret == "":
        return display_code(filename)
    else:
        print_run_cmd("git diff " + filename)


def move_single_ipynb(file_ipynb):
    # file_ipynb = "20230306.ipynb"
    import os

    if os.path.isfile(file_ipynb):
        assert file_ipynb.endswith(".ipynb")
        assert len(file_ipynb) == len("yyyyMMdd.ipynb")
        import datetime

        current_date = datetime.datetime.now()
        dir_year = file_ipynb[0:4]
        dir_month = file_ipynb[4:6]
        assert int(dir_year) <= current_date.year
        assert int(dir_year) + 1 >= current_date.year
        print(int(dir_month))
        assert int(dir_month) <= 12
        assert int(dir_month) >= 1

        dir_ipynb = dir_year + "/" + dir_month
        if os.path.isdir(dir_ipynb) == False:
            os.makedirs(dir_ipynb)
        cmd_run = "git mv " + file_ipynb + " " + dir_ipynb
        print(cmd_run)
        cmd_ret = print_run_cmd(cmd_run)
    else:
        print("Can not find %s" % file_ipynb)


def git_add_ipynb(file_ipynb):
    cmd_run = "git add " + file_ipynb
    cmd_ret = print_run_cmd(cmd_run)


def endswith(*endstring):
    ends = endstring

    def run(s):
        f = map(s.endswith, ends)
        if True in f:
            return s

    return run


def dev_clean_ipynb():
    import os

    list_file = os.listdir(".")
    a = endswith(".ipynb")  # , '.txt','.py', '.md')
    f_file = filter(a, list_file)
    f_sort = sorted(f_file)
    idx = 0
    idx_limit = len(f_sort)
    for i in f_sort:
        idx = idx + 1
        git_add_ipynb(i)
        if idx < idx_limit:
            move_single_ipynb(i)
        else:
            print("Ignore %s" % i)


def empty_file(file_path):
    import fileinput

    with fileinput.FileInput(file_path, inplace=True) as f:
        for line in f:
            # print(line, end="")
            pass


def append_text_file_with_utf8(file_name, file_content):
    with open(file_name, "a", encoding="utf-8") as file:
        file.write(file_content)


# https://www.zopatista.com/python/2013/11/26/inplace-file-rewriting/
@contextmanager
def inplace(
    filename,
    mode="r",
    buffering=-1,
    encoding=None,
    errors=None,
    newline=None,
    backup_extension=None,
):
    """Allow for a file to be replaced with new content.

    yields a tuple of (readable, writable) file objects, where writable
    replaces readable.

    If an exception occurs, the old file is restored, removing the
    written data.

    mode should *not* use 'w', 'a' or '+'; only read-only-modes are supported.

    """

    # move existing file to backup, create new file with same permissions
    # borrowed extensively from the fileinput module
    if set(mode).intersection("wa+"):
        raise ValueError("Only read-only file modes can be used")

    backupfilename = filename + (backup_extension or os.extsep + "bak")
    try:
        os.unlink(backupfilename)
    except os.error:
        pass
    os.rename(filename, backupfilename)
    readable = io.open(
        backupfilename,
        mode,
        buffering=buffering,
        encoding=encoding,
        errors=errors,
        newline=newline,
    )
    try:
        perm = os.fstat(readable.fileno()).st_mode
    except OSError:
        writable = open(
            filename,
            "w" + mode.replace("r", ""),
            buffering=buffering,
            encoding=encoding,
            errors=errors,
            newline=newline,
        )
    else:
        os_mode = os.O_CREAT | os.O_WRONLY | os.O_TRUNC
        if hasattr(os, "O_BINARY"):
            os_mode |= os.O_BINARY
        fd = os.open(filename, os_mode, perm)
        writable = io.open(
            fd,
            "w" + mode.replace("r", ""),
            buffering=buffering,
            encoding=encoding,
            errors=errors,
            newline=newline,
        )
        try:
            if hasattr(os, "chmod"):
                os.chmod(filename, perm)
        except OSError:
            pass
    try:
        yield readable, writable
    except Exception:
        # move backup back
        try:
            os.unlink(filename)
        except os.error:
            pass
        os.rename(backupfilename, filename)
        raise
    finally:
        readable.close()
        writable.close()
        try:
            os.unlink(backupfilename)
        except os.error:
            pass


def update_line_in_file_with_utf8(
    file_path, old_line_number, new_line_content, flag_replace=True
):
    with inplace(file_path, "r", newline="", encoding="utf-8") as (infh, outfh):
        line_number = 0
        for line in infh:
            line_number = line_number + 1
            if line_number == old_line_number:
                outfh.write(new_line_content)
                if not flag_replace:
                    outfh.write(line)
            else:
                outfh.write(line)


def replace_line_in_file_with_utf8(file_path, old_line_number, new_line_content):
    update_line_in_file_with_utf8(file_path, old_line_number, new_line_content, True)


def add_line_in_file_with_utf8(file_path, old_line_number, new_line_content):
    update_line_in_file_with_utf8(file_path, old_line_number, new_line_content, False)


def change_prj_root(prj_dir, print_flag=True):
    import os

    while os.getcwd().endswith(prj_dir) is False:
        if print_flag:
            print(os.path.basename(os.getcwd()))
        os.chdir("..")
        if print_flag:
            print(os.getcwd())
    return os.getcwd()


def print_time_now():
    import time

    content = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(content)
    return content


def unique(data):
    obj = {}
    for item in data:
        obj[item] = item
    return list(obj.values())


def convert_id_to_underline(x):
    """转下划线命名"""
    import re

    return re.sub("(?<=[a-z])[A-Z]|(?<!^)[A-Z](?=[a-z])", "_\g<0>", x).lower()


def convert_id_to_upper_camel_case(x):
    """转大驼峰法命名"""
    import re

    s = re.sub("_([a-zA-Z])", lambda m: (m.group(1).upper()), x.lower())
    return s[0].upper() + s[1:]


def convert_id_to_lower_camel_case(x):
    """转小驼峰法命名"""
    import re

    s = re.sub("_([a-zA-Z])", lambda m: (m.group(1).upper()), x.lower())
    return s[0].lower() + s[1:]


def check_py_code(python_code):
    import autopep8

    fix_code = autopep8.fix_code(python_code)
    if fix_code != python_code:
        print(fix_code)
        assert False
    return fix_code


def sync_repo(repo):
    util.print_time_now()
    assert os.path.isdir(repo)
    os.chdir(repo)
    print("-----------------------------------------------")
    print(f"Checking {repo} ...")
    print("-----------------------------------------------")
    cmd = "git status"
    ret = invoke.run(cmd, encoding="utf-8")

    key = "Your branch is ahead of 'origin/"
    if ret.stdout.find(key) >= 0:
        cmd = "git push"
        invoke.run(cmd, encoding="utf-8")
        return

    keys = [
        "nothing to commit, working tree clean",
        "nothing added to commit but untracked files present",
    ]
    for key in keys:
        if ret.stdout.find(key) >= 0:
            return
    cmd = 'git commit -a -m "Sync"'
    invoke.run(cmd, encoding="utf-8")
