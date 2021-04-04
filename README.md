# Monitor the Internet Connection Speed

This repository contains a Python application to monitor the download and upload speed every 3 minutes.

1) OBJECTIVE

The objective of this application is to help internet users to check if the internet service provider is delivering the contracted connection speed.

2) INTRODUCTION

Internet service providers (ISP) market their products using the maximum connection speed that can be achieved prefixing it with a language like "up to". This strategy is deceiving, once the connection depends on several factors and may oscilate considerably in short periods of time. It's also important to emphasize that advertised speeds are based on wired connections to the modem. The internet connection speed will dip with a Wi-Fi router.

The government regulations for the providers vary from country to country. Taking Brazil as an example, IPS are obligated to deliver at least 40% of the contracted maximum speed as instantaneous speed, but the monthly average speed must be at least 80% of it (for download and upload).

Table 1 - Regulation for minimum speed delivery in Brazil 
![image](https://user-images.githubusercontent.com/81535464/113519855-2fd0b100-958f-11eb-8b52-bf628e04e87d.png)

(Source: https://www.anatel.gov.br/Portal/exibirPortalPaginaEspecialPesquisa.do?acao&tipoConteudoHtml=1&codNoticia=35544)

This application will measure the download and the upload speeds every 3 minutes and save the results to the file "result_dsl.xlsx" in the user's desktop.

3) DEVELOPMENT

The application is divided into three Python files:

  - ExcelUtils.py: contains the class "Excel" to conditionate the Excel file which the records will be written to;
  - DSLUtils.py: contains the class "Dsl" to measure the download and upload speeds;
  - main.py
  
       3.1 - CLASS Excel
       
       This class uses the packages xlsxwriter, os and winreg
                                                  
        pip install xlswriter
        
        pip install winreg
             
       3.1.1 - Function get_microsoft_office_version
           
       This function delivers the version of the Office installation by acessing the Windows Registry.
           
       This is important to compose the path for the Excel installation.
           
       If there is no Office installation, the function will return 0.
                  
       3.1.2 - Function is_excel_installed
           
       This function delivers a Boolean value checking if Microsoft Excel is installed by acessing the Windows Registry.
              
       3.1.3 - Function result_file_exists
           
       This function checks if the result Excel file "result_dsl.xlsx" exists.
                  
       3.1.4 - Function create_excel_file
           
       This function creates the result file "result_dsl.xlsx" with the expected columns names.
       
       ![image](https://user-images.githubusercontent.com/81535464/113520376-ed10d800-9592-11eb-93b7-da8cd12e29d6.png)
       
       
       3.2 - CLASS Dsl
       
       This class uses the package speedtest, pandas and datetime
       
        pip install speedtest-cli
              
        pip install pandas
              
       Please notice that the need package is "speedtest-cli" and not only "speedtest"!
       
       3.2.1 - Function record_dsl_speed
           
       This function measures the download and the upload speeds and saves the result to the Excel file "result_dsl.xlsx".

                  
 
