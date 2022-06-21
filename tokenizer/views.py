from konlpy.tag import Kkma, Komoran, Okt, Mecab, Hannanum
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
# mec = Mecab()
okt = Okt()
kkm = Kkma()
kom = Komoran()
han = Hannanum()


class HealthCheck(APIView):
    def get(self, request):
        return Response(status=status.HTTP_200_OK)


class MecabText(APIView):
    def post(self, request):
        # text = request.data.get("origin_text", None)
        # if text is None:
        #     Response(status=status.HTTP_400_BAD_REQUEST)
        # mec_tokenizer = mec.pos(text, flatten=False, join=True)
        # rtn_json = {
        #     "tokenize": mec_tokenizer
        # }
        # return Response(rtn_json, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_200_OK)


class KomText(APIView):
    def post(self, request):
        text = request.data.get("origin_text", None)
        if text is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        kom_tokenizer = kom.pos(text, flatten=True, join=True)
        rtn_json = {
            "tokenize": ", ".join(kom_tokenizer)
        }
        return Response(rtn_json, status=status.HTTP_200_OK)


class HanText(APIView):
    def post(self, request):
        text = request.data.get("origin_text", None)
        if text is None:
            Response(status=status.HTTP_400_BAD_REQUEST)
        han_tokenizer = han.pos(text, flatten=True, join=True)
        rtn_json = {
            "tokenize": ", ".join(han_tokenizer)
        }
        return Response(rtn_json, status=status.HTTP_200_OK)


class OktText(APIView):
    def post(self, request):
        text = request.data.get("origin_text", None)
        if text is None:
            Response(status=status.HTTP_400_BAD_REQUEST)
        okt_tokenizer = okt.pos(text, norm=True, stem=True, join=True)
        rtn_json = {
            "tokenize": ", ".join(okt_tokenizer)
        }
        return Response(rtn_json, status=status.HTTP_200_OK)


class AllTokenizer(APIView):
    def post(self, request):
        text = request.data.get("origin_text", None)
        if text is None:
            Response(status=status.HTTP_400_BAD_REQUEST)
        kom_tokenizer = kom.pos(text, flatten=True, join=True)
        han_tokenizer = han.pos(text, flatten=True, join=True)
        okt_tokenizer = okt.pos(text, norm=True, stem=True, join=True)
        rtn_json = {
            "Komoran": ", ".join(kom_tokenizer),
            "Hannanum": ", ".join(han_tokenizer),
            "Okt": ", ".join(okt_tokenizer),
        }
        return Response(rtn_json, status=status.HTTP_200_OK)


