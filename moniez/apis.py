from rest_framework.views import APIView
from rest_framework.response import Response
from moniez.utils import fetch_consent_status
from moniez.utils import fetch_tracking_refrence_id

from moniez.utils import generate_tracking_id, initiate_consent

class RecommendationView(APIView):
    """ FETCH CLIENT DATA AND RECOMMEND Stocks data with label of the user """
    def get(self, request, format=None):
        #fetch data against user token
        # found data in CSV with 3 caps
        return Response(True)

class AllStocks(APIView):
    def get ():
        # return all stocks and render  
        return Response(True)
class SpendTracker(APIView):
    """Fetch Credit to Debit Ratio and pass on array for graph"""
    def get(self,request):
        return Response(True)


class TaxSaving(APIView):
    """Pass on Tax saving benefits according to the users bracket"""
    def get(self,request):
        return Response(True)

class Profile(APIView):
    """ Pass on user profile data """
    #net worth
    # name
    # Show overall Credit to Debit Ratio

    def get(self, request):
        return Response(True)

class CreateWealth(APIView):
    ## Custom percentage of their Bank balance
    ## Show Gov bonds BOB
    ## NPS
    ## All that stuff
    def get():
        return Response(True)

class Portfolio(APIView):
    def get():
        return Response(True)
    ##Check if each stock is doing better than nifty

## BELOW ARE HACKATHON APIS        

class InitiateConsent(APIView):
    """TO INITIATE CONSENT FOR A CLIENT"""
    def post(self,request):
        # USER TOKEN ONLY
        #FETCH CLIENT PHONE NUMBER from DB against User token
        mock_data = [9987600001,9987600002,9987600003,9987600004,9987600005] 
        phone_number = 9987600002
        # check if consent already exist?

        # PUNCH CONSENT 
        result = initiate_consent(phone_number,tracking_id=generate_tracking_id())
        print(result)
        if result==False:
            res = "Something went Wrong!"
        res ={
            "data":"Initiated Consent",
            "redirection_url": result['redirectionUrl']
        }

        #Store REF ID & tracking ID Against user in DB 
        # result['referenceId']
        return Response(data=res)

class FetchConsent(APIView):
    def get(self,request):
        #fetch Tracking and ref id against the user using
        hello = fetch_tracking_refrence_id()
        tracking_id =request.data['track_id']
        ref_id = request.data['ref_id']
        consent_result = fetch_consent_status(tracking_id,ref_id)
        print(consent_result)
        return Response(data=consent_result)

class FetchData(APIView):
    """ Fetch data here post consent and dump in DB """
    ## Against user 
    ## Credit to debit 
    ## their Portfoio
    ## their Bank statemnet 
    ## dump useful data

    def get(self,request):
        return Response()



"""
It’s also super easy. To install the Yahoo_fin library just run the command:

pip install yahoo_fin
If you ever need to upgrade in the future just run:

pip install yahoo_fin --upgrade
Yahoo_fin also has a few dependencies:

ftplib
io
pandas
requests
requests_html
Besides requests_html, these should all come pre-installed with Anaconda.

To install requests_html, it’s as easy as:

pip install requests_html
Note requests_html requires Python 3.6+ to function. You don’t need it to use the majority of the functionality in Yahoo_fin, but there are a few functions you won’t be able to use without it. We’ll highlight which functions depend on it in a sec.

Other than that, that’s it! You’re ready to get started!

Library Layout
Just before we start looking at specific useful examples, let’s quickly go over the layout of the Yahoo_fin library.

Yahoo_fin has two modules- stock_info and options.

stock_info has the following methods:

get_analysts_info()
get_balance_sheet()
get_cash_flow()
get_data()
get_day_gainers()
get_day_losers()
get_day_most_active()
get_holders()
get_income_statement()
get_live_price()
get_quote_table()
get_top_crypto()
get_stats()
get_stats_valuation()
tickers_dow()
tickers_nasdaq()
tickers_other()
tickers_sp500()
"""




