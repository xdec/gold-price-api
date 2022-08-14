# Get The Latest Gold Price :chart_with_upwards_trend:

---

Scrape live gold prices via an API and store it in a CSV with a timestamp.

Available API's :electric_plug:
- [Metals IO](https://metals-api.com/)
    - Rate Limit: 50 free calls p/m
- [Gold API IO](https://www.goldapi.io/)
    - Rate Limit: 500 free calls p/m
    
----------------------------

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


        https://api.metalpriceapi.com/v1/latest?base=USD&currencies=XAU,XAG&api_key=Dxt3fx5NcET88EGsAtvrdJ
        
        
