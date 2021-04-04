import speedtest
import pandas as pd
from datetime import datetime


class Dsl:
    def record_dsl_speed(self, file):
        df = pd.read_excel(file, sheet_name='base')
        print(dir(speedtest))
        s = speedtest.Speedtest()
        s.get_best_server()
        download = s.download(threads=None) * (10 ** -6)
        upload = s.upload(threads=None) * (10 ** -6)
        now = datetime.now()
        date = now.strftime("%m/%d/%Y")
        hour = now.strftime("%H:%M:%S")
        df.loc[len(df)] = [date, hour, download, upload]
        df.to_excel(file, sheet_name='base', index=False)
