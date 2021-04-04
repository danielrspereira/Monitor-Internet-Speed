import winreg
import os
import xlsxwriter


class Excel:
    def is_excel_installed(self):
        installed = False
        ver = self.get_microsoft_office_version()
        try:
            winreg.OpenKey(winreg.HKEY_CURRENT_USER, "SOFTWARE\\Microsoft\\Office\\" + str(ver) + "\\Excel", 0,
                           winreg.KEY_READ)
            installed = True
        except (FileNotFoundError, IOError):
            pass
        return installed

    def get_microsoft_office_version(self):
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "SOFTWARE\\Microsoft\\Office", 0, winreg.KEY_READ)
        version_num = 0
        i = 0
        while True:
            try:
                subkey = winreg.EnumKey(key, i)
                i += 1
                if version_num < float(subkey):
                    version_num = float(subkey)

            except:
                break
        return version_num

    def result_file_exists(self, file):
        return os.path.isfile(file)

    def create_excel_file(self, file):
        # Create a workbook and add a worksheet.
        workbook = xlsxwriter.Workbook(file)
        worksheet = workbook.add_worksheet()
        worksheet.name = 'base'
        # Some data we want to write to the worksheet.
        columns = ["Date", "Time", "Download", "Upload"]
        # Start from the first cell. Rows and columns are zero indexed.
        row = 0
        col = 0
        # Iterate over the data and write it out row by row.
        for column in columns:
            worksheet.write(row, col, column)
            col += 1
        workbook.close()
