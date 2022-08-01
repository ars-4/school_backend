from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST


def delete_token(pre_token):
    token = RefreshToken(pre_token)
    try:
        token.blacklist()
        return Response({"message": "Token deleted successfully"}, status=HTTP_200_OK)
    except Exception as error:
        return Response({"error": str(error)}, status=HTTP_400_BAD_REQUEST)

