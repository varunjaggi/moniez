from rest_framework.views import APIView
from rest_framework.response import Response
from moniez.utils import fetch_consent_status
from moniez.utils import fetch_tracking_refrence_id

from moniez.utils import generate_tracking_id, initiate_consent

class RecommendationView(APIView):
    """ FETCH CLIENT DATA AND RECOMMEND """
    def get(self, request, format=None):
        #fetch data against user token
        
        return Response(True)

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


