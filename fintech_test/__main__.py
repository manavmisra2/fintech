import site
import os
import shutil
os.system("pip install jupyterlab_templates")
os.system("jupyter labextension install jupyterlab_templates")
os.system("jupyter serverextension enable --py jupyterlab_templates")


def main():
    print("Running Jupyter platform!")
    out = site.getsitepackages()
    if len(out) == 1:
        str_out = out
        out1 = ' '.join(str_out)
        filename = os.path.join(
            out1, "fintech_test", "jupyter_notebook_config.py")
        filename2 = filename.replace(os.sep, '/')
        filename3 = os.path.join(
            out1, "jupyterlab_templates/templates/jupyterlab_templates/")
        src_file = os.path.join(out1, "fintech_test", "quanturf_test.ipynb")
        src_path = src_file
        dst_path = filename3.replace(os.sep, '/')
        shutil.copy(src_path, dst_path)
        os.system("jupyter lab --config=" + filename2)
    if len(out) >= 2:
        str_out = out[1]
        filename = os.path.join(str_out, "fintech_test",
                                "jupyter_notebook_config.py")
        filename2 = filename.replace(os.sep, '/')
        filename3 = os.path.join(
            str_out, "jupyterlab_templates/templates/jupyterlab_templates/")
        filename3 = os.path.join(
            str_out, "jupyterlab_templates/templates/jupyterlab_templates/")
        src_file = os.path.join(str_out, "fintech_test", "quanturf_test.ipynb")
        src_path = src_file
        dst_path = filename3.replace(os.sep, '/')
        shutil.copy(src_path, dst_path)
        os.system("jupyter lab --config=" + filename2)


if __name__ == "__main__":
    main()


def listToString(s):

    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

    # return string
    return str1
