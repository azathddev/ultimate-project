from rest_framework.response import Response


def response(message: str, detail: str | dict | list, status: int) -> Response:
    return Response(
        {
            "message": message,
            "detail": detail,
        },
        status=status,
    )
