from threading import Timer
import os
from ExcelUtils import Excel
from DSLUtils import Dsl


def get_desktop_path():
    import os
    return os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')


def record_dsl_speed_to_excel(file):
    ex = Excel()
    dsl = Dsl()
    excel = ex.is_excel_installed()
    if excel:
        if not ex.result_file_exists(file):
            ex.create_excel_file(file)
        dsl.record_dsl_speed(file)
        Timer(180, record_dsl_speed_to_excel, args=(file,)).start()
    else:
        print("Microsoft Office is not installed")


def main():
    file_name = os.path.join(get_desktop_path(), 'dsl_speed.xlsx')
    record_dsl_speed_to_excel(file_name)


main()
