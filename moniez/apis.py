from rest_framework.views import APIView
from rest_framework.response import Response
from moniez.utils import fetch_price
from moniez.stocks_data import LARGE_CAP, MID_CAP, SMALL_CAP
from moniez.recommendations import LOW_RISK, MID_RISK, HIGH_RISK, VERY_HIGH_RISK
from moniez.utils import fetch_consent_status
from moniez.utils import fetch_tracking_refrence_id
from moniez.utils import fetch_analytics_data


from moniez.utils import generate_tracking_id, initiate_consent


class RecommendationView(APIView):
    """FETCH CLIENT DATA AND RECOMMEND Stocks data with label of the user"""

    def post(self, request, format=None):
        # risk appetite value, tracking id, reference id

        # if low, rav = 0.33, medium = 0.67, high = 0.9

        risk_appetite_value = request.data.risk_appetite_value
        tracking_id = request.data.tracking_id
        reference_id = request.data.reference_id

        response = fetch_analytics_data(tracking_id, reference_id)

        credit_to_debit_ratio = response["analytics"]["overallAnalysis"][
            "creditDebitRatio"
        ]

        debit_to_credit_ratio = 1 - credit_to_debit_ratio

        if debit_to_credit_ratio is None:
            average_risk_score = risk_appetite_value

        average_risk_score = (debit_to_credit_ratio + risk_appetite_value) / 2

        data = VERY_HIGH_RISK

        if average_risk_score >= 0 and average_risk_score < 0.3:
            # equity, large cap crypto, stocks
            data = VERY_HIGH_RISK

        elif average_risk_score >= 0.3 and average_risk_score < 0.5:
            # equity + hybrid, nft, defi and metaverse, stocks
            data = HIGH_RISK

        elif average_risk_score >= 0.5 and average_risk_score < 0.8:
            # hybrid + debt, rd, fd, ppf, nps
            data = MID_RISK

        elif average_risk_score >= 0.8 and average_risk_score < 1:
            # rd, ppf
            data = LOW_RISK

        return Response({"data": data})


class CreditDebitRatioMonthly(APIView):
    """Monthly Credit to Debit Ratio"""

    def get():

        ratio = [
            "1.23",
        ]
        month = [
            "5",
        ]


class AllStocks(APIView):
    def get(self, request):
        data = "Something went wrong"
        res = {"data": data}
        if request.data["cap"] == "LARGE_CAP":
            data = LARGE_CAP
        if request.data["cap"] == "MID_CAP":
            data = MID_CAP
        if request.data["cap"] == "SMALL_CAP":
            data = SMALL_CAP
        # return all stocks and render
        return Response({"data": data})


class SpendTracker(APIView):
    """Fetch Credit to Debit Ratio and pass on array for graph"""

    def get(self, request):
        return Response(True)


class TaxSaving(APIView):
    """Pass on Tax saving benefits according to the users bracket"""

    def get(self, request):
        return Response(True)


class Profile(APIView):
    """Pass on user profile data"""

    # net worth
    # name
    # Show overall Credit to Debit Ratio

    def get(self, request):
        res = {"Name": "Varun Jaggi", "HEHE": "HEHE"}
        return Response(res)


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

    def post(self, request):
        phone_number = request.data["phonenumber"]
        # USER TOKEN ONLY
        # FETCH CLIENT PHONE NUMBER from DB against User token
        # mock_data = [9987600001,9987600002,9987600003,9987600004,9987600005]
        # phone_number = 9987600002
        # check if consent already exist?

        # PUNCH CONSENT
        result = initiate_consent(phone_number, tracking_id=generate_tracking_id())
        print(result)
        if result == False:
            res = "Something went Wrong!"
        res = {"data": "Initiated Consent", "redirection_url": result["redirectionUrl"]}

        # Store REF ID & tracking ID Against user in DB
        # result['referenceId']
        return Response(data=res)


class FetchConsent(APIView):
    def get(self, request):
        # fetch Tracking and ref id against the user using
        hello = fetch_tracking_refrence_id()
        tracking_id = request.data["track_id"]
        ref_id = request.data["ref_id"]
        consent_result = fetch_consent_status(tracking_id, ref_id)
        print(consent_result)
        return Response(data=consent_result)


class FetchData(APIView):
    """Fetch data here post consent and dump in DB"""

    ## Against user
    ## Credit to debit
    ## their Portfoio
    ## their Bank statemnet
    ## dump useful data

    def get(self, request):
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
