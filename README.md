# Monitor Internet Connection Speed

This repository contains a Python application to monitor the download and upload speed every 3 minutes

1) OBJECTIVE

The objective of this application is to help internet users to check if the internet service provider is delivering the contracted connection speed.

2) INTRODUCTION

Internet service providers (ISP) market their products using the maximum connection speed that can be achieved prefixing it with a language like "up to". This strategy is deceiving, once the connection depends on several factors and may oscilate considerably in short periods of time. It's also important to emphasize that advertised speeds are based on wired connections to the modem. The internet connection speed will dip with a Wi-Fi router.

The government regulations for the providers vary from country to country. Taking Brazil as an example, IPS are obligated to deliver at least 40% of the contracted maximum speed as instantaneous speed, but the monthly average speed must be at least 80% of it (for download and upload).

Table 1 - Regulation for minimum speed delivery in Brazil (Source: https://www.anatel.gov.br/Portal/exibirPortalPaginaEspecialPesquisa.do?acao&tipoConteudoHtml=1&codNoticia=35544)
![image](https://user-images.githubusercontent.com/81535464/113519855-2fd0b100-958f-11eb-8b52-bf628e04e87d.png)

3) DEVELOPMENT

The application is divided into three Python files:

  - ExcelUtils.py: contains the class "Excel" to conditionate the Excel file which the records will be written to;
  - DSLUtils.py: contains the class "Dsl" to measure the download and upload speeds;
  - main.py
  
  3.1) Class Excel
  

 
