# Get The Latest Gold Price :chart_with_upwards_trend:

> [![Gold Price v_s Timeline (1)](https://user-images.githubusercontent.com/50515418/209144461-89643912-3dee-410a-9d52-4a7b17dcd3ef.png)](https://docs.google.com/spreadsheets/d/e/2PACX-1vTBXHupCi3x-nYBxY3MdFA4oLkZiZjY34o_qoWfjVke85775s3bzI6wsnJFkJ-sWbVq69jFfPVVTQ7U/pubchart?oid=478367470&format=interactive)

----------------------------

Scrape live gold prices via an API and store it in a CSV with a timestamp.

Available API's :electric_plug:
- [Metals IO](https://metals-api.com/)
    - Rate Limit: 50 free calls p/m
- [Gold API IO](https://www.goldapi.io/)
    - Rate Limit: 500 free calls p/m
    
----------------------------

# https://www.goldapi.io/dashboard

        var myHeaders = new Headers();
        myHeaders.append("x-access-token", "xxxxxxxx");
        myHeaders.append("Content-Type", "application/json");

        var requestOptions = {
          method: 'GET',
          headers: myHeaders,
          redirect: 'follow'
        };

        fetch("https://www.goldapi.io/api/XAU/USD", requestOptions)
          .then(response => response.text())
          .then(result => console.log(result))
          .catch(error => console.log('error', error));
          
--------------------------

        curl -X GET 'https://www.goldapi.io/api/XAU/USD' -H 'x-access-token: xxxxxxxxxxxx'

-------------------

# https://metalpriceapi.com/dashboard

[![image](https://user-images.githubusercontent.com/50515418/209143842-6a806a82-2386-4751-8b21-db119e5b1926.png)](https://docs.google.com/spreadsheets/d/1SYWpE0tS5F_g5dnhNRqqY0I20KsK8o3HA5EnV2VDEis/edit?usp=sharing)

        function callNumbers() {
          let url = "https://api.metalpriceapi.com/v1/latest?base=USD&currencies=XAU,XAG&api_key=Dxt3fx5NcET88EGsAtvrdJ";
          let fact = UrlFetchApp.fetch(url);

          let apiResponse = JSON.parse(fact.getContentText());
          Logger.log(apiResponse);

          const date = new Date(apiResponse.timestamp*1000);
          let unixdate = date.toLocaleDateString("en-IN");
          let unixtime = date.toLocaleTimeString("en-IN");

          let price = apiResponse.rates.XAU*1000000000;
          console.log(unixdate, unixtime, price);

          let sheet = SpreadsheetApp.getActiveSheet();
          sheet.getRange(1,1).setValue("Unix Timestamp");
          sheet.getRange(1,2).setValue("Rate of Gold");

          sheet.getRange(sheet.getLastRow() + 1,1).setValue(unixdate + ' ' + unixtime);
          sheet.getRange(sheet.getLastRow() + 0,2).setValue(price);
        }

--------------------------------

![image](https://user-images.githubusercontent.com/50515418/184533608-d2fc81b3-dfbe-41d3-8581-3728d7757200.png)

        - API : https://api.metalpriceapi.com/v1/latest?base=USD&currencies=XAU,XAG&api_key=Dxt3fx5NcET88EGsAtvrdJ
        
        - Article : https://www.benlcollins.com/apps-script/api-tutorial-for-beginners/

        - Sheet : https://docs.google.com/spreadsheets/d/1SYWpE0tS5F_g5dnhNRqqY0I20KsK8o3HA5EnV2VDEis/edit#gid=0
        
        - Script : https://script.google.com/home/projects/18aYVuDMURltcEGcgES_MY2JpLVcMsPcPSmRFxPPZ_Xz9Aug5EcD1MOze/edit
        
        - GCP : https://console.cloud.google.com/home/dashboard?project=ideationology-lab
        
        - Run : https://script.googleapis.com/v1/scripts/AKfycbxMBc17JzNiRP7RGSnZXVroeEVyrI9oEFbbkyAvwfYmTH4RqKJzdx5sjeBP048peELauQ:run
        
        - Library : https://script.google.com/macros/library/d/18aYVuDMURltcEGcgES_MY2JpLVcMsPcPSmRFxPPZ_Xz9Aug5EcD1MOze/1
        
        - Colab : https://colab.research.google.com/drive/1nwOWNFbWeea8KovPENqIAiwdAadhIZGH
        
