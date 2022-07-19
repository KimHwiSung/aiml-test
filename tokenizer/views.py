from konlpy.tag import Kkma, Komoran, Okt, Mecab, Hannanum
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
mec = Mecab()
okt = Okt()
kkm = Kkma()
kom = Komoran()
han = Hannanum()


def tokenize(pos_pattern, pos):
    for index, token in enumerate(pos_pattern):
        pos_word = token.split("/")
        if pos_word[-1] == pos:
            pos_pattern[index] = pos_word[-1]
        else:
            pos_pattern[index] = pos_word[0]
    return " ".join(pos_pattern)


class HealthCheck(APIView):
    def get(self, request):
        return Response(status=status.HTTP_200_OK)


class MecabText(APIView):
    def post(self, request):
        text = request.data.get("origin_text", None)
        if text is None:
            Response(status=status.HTTP_400_BAD_REQUEST)
        mec_tokenizer = mec.pos(text, flatten=True, join=True)
        rtn_json = {
            "tokenize": ", ".join(mec_tokenizer),
            "최종 입력 값": tokenize(mec_tokenizer, "JX")
        }
        return Response(rtn_json, status=status.HTTP_200_OK)


class KomText(APIView):
    def post(self, request):
        text = request.data.get("origin_text", None)
        if text is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        kom_tokenizer = kom.pos(text, flatten=True, join=True)
        rtn_json = {
            "tokenize": ", ".join(kom_tokenizer),
            "최종 입력 값": tokenize(kom_tokenizer, "JX")
        }
        return Response(rtn_json, status=status.HTTP_200_OK)


class HanText(APIView):
    def post(self, request):
        text = request.data.get("origin_text", None)
        if text is None:
            Response(status=status.HTTP_400_BAD_REQUEST)
        han_tokenizer = han.pos(text, flatten=True, join=True)
        rtn_json = {
            "tokenize": ", ".join(han_tokenizer),
            "최종 입력 값": tokenize(han_tokenizer, "J")
        }
        return Response(rtn_json, status=status.HTTP_200_OK)


class OktText(APIView):
    def post(self, request):
        text = request.data.get("origin_text", None)
        if text is None:
            Response(status=status.HTTP_400_BAD_REQUEST)
        okt_tokenizer = okt.pos(text, norm=True, stem=True, join=True)
        rtn_json = {
            "tokenize": ", ".join(okt_tokenizer),
            "최종 입력 값": tokenize(okt_tokenizer, "Josa")
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
        mec_tokenizer = mec.pos(text, flatten=True, join=True)
        rtn_json = {
            "Komoran": {
                "tokenize": ", ".join(kom_tokenizer),
                "최종 입력 값": tokenize(kom_tokenizer, "JX")
            },
            "Hannanum": {
                "tokenize": ", ".join(han_tokenizer),
                "최종 입력 값": tokenize(han_tokenizer, "J")
            },
            "Okt": {
                "tokenize": ", ".join(okt_tokenizer),
                "최종 입력 값": tokenize(okt_tokenizer, "Josa")
            },
            "Mecab": {
                "tokenize": ", ".join(mec_tokenizer),
                "최종 입력 값": tokenize(mec_tokenizer, "JX")
            },
        }
        return Response(rtn_json, status=status.HTTP_200_OK)


