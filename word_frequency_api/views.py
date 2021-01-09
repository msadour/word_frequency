"""Views."""

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from word_frequency_api.word_frequency import WordFrequency


class WordFrequencyView(APIView):
    """Class WordFrequencyView."""

    def get(self, request, *args, **kwargs):
        """Return the result from the user's request regarding the actions..

        Args:
            request: request sent by the client.
            args: Variable length argument list.
            kwargs: Arbitrary keyword arguments.

        Returns:
            Response from the server.
        """
        action = request.query_params.get("action")
        text = request.query_params.get("text", "")
        word = request.query_params.get("word", "")
        word_frequency = WordFrequency(text=text, word=word)

        if hasattr(word_frequency, action):
            result = getattr(word_frequency, action)()
            return Response(data=result)
        else:
            return Response(
                data={"error": "Bad request."}, status=status.HTTP_400_BAD_REQUEST
            )
