import speedtest
import pandas as pd
from datetime import datetime


class Dsl:
    def record_dsl_speed(self, file):
        df = pd.read_excel(file, sheet_name='base')
        download = 0.0
        upload = 0.0
        # in case of connection problem this function will deliver speed = 0
        try:
            s = speedtest.Speedtest()
            s.get_best_server()
            download = s.download(threads=None) * (10 ** -6)
            upload = s.upload(threads=None) * (10 ** -6)
        
        except:
            pass
        now = datetime.now()
        date = now.strftime("%m/%d/%Y")
        hour = now.strftime("%H:%M:%S")
        df.loc[len(df)] = [date, hour, download, upload]
        df.to_excel(file, sheet_name='base', index=False)
