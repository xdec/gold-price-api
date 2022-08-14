# Get The Latest Gold Price :chart_with_upwards_trend:

---

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

        function callNumbers() {

          // Call the Numbers API for random math fact
          var response = UrlFetchApp.fetch("https://api.metalpriceapi.com/v1/latest?base=USD&currencies=XAU,XAG&api_key=Dxt3fx5NcET88EGsAtvrdJ");
          Logger.log(response.getContentText());

          var fact = response.getContentText();
          var sheet = SpreadsheetApp.getActiveSheet();
          sheet.getRange(sheet.getLastRow() + 1,1).setValue([fact]);

        }

--------------------------------

        - API : https://api.metalpriceapi.com/v1/latest?base=USD&currencies=XAU,XAG&api_key=Dxt3fx5NcET88EGsAtvrdJ
        
        - Article : https://www.benlcollins.com/apps-script/api-tutorial-for-beginners/

        - Sheet : https://docs.google.com/spreadsheets/d/1SYWpE0tS5F_g5dnhNRqqY0I20KsK8o3HA5EnV2VDEis/edit#gid=0
        
        - Script : https://script.google.com/u/0/home/projects/1Hyj91AmRxCetEfTx3_Z0L_OdYjHDqPoZH_qlpkjgbZ9nWZ1Mk2epLBXy/edit
        
        - GCP : https://console.cloud.google.com/home/dashboard?project=ideationology-lab
        
        - Run : https://script.googleapis.com/v1/scripts/AKfycbxMBc17JzNiRP7RGSnZXVroeEVyrI9oEFbbkyAvwfYmTH4RqKJzdx5sjeBP048peELauQ:run
