"""Tests cases."""

from rest_framework.test import APITestCase, APIClient


class TestAPI(APITestCase):
    """Class TestAPI."""

    def setUp(self) -> None:
        """Set up attributes for tests."""
        self.client = APIClient()

    def test_calculate_highest_frequency(self) -> None:
        """Test calculate highest frequency.

        Raises:
            AssertError: Assertion failed.
        """
        response_word_the_three_time = self.client.get(
            "?action=calculate_highest_frequency&text=the sky, the moon and again the sky"
        )

        response_word_sky_moon_two_time = self.client.get(
            "?action=calculate_highest_frequency&text=sky moon sky moon"
        )
        assert response_word_the_three_time.data == [("the", 3)]
        assert response_word_sky_moon_two_time.data == [("sky", 2), ("moon", 2)]

    def test_calculate_frequency_for_word(self) -> None:
        """Test calculate frequency for word.

        Raises:
            AssertError: Assertion failed.
        """
        response_word_the = self.client.get(
            "?action=calculate_frequency_for_word&text=over the lake, I see the fish&word=the"
        )

        response_word_lake = self.client.get(
            "?action=calculate_frequency_for_word&text=over the lake, I see the fish&word=lake"
        )
        assert response_word_the.data == 2
        assert response_word_lake.data == 1

    def test_calculate_most_frequent_words(self) -> None:
        """Test calculate more frequent word.

        Raises:
            AssertError: Assertion failed.
        """
        response = self.client.get(
            "?action=calculate_most_frequent_words&text=over the lake, I see the fish"
        )
        assert response.data[0] == ("the", 2)
        assert response.data[1] == ("fish", 1)

    def test_wrong_request(self) -> None:
        """Test wrong action.

        Raises:
            AssertError: Assertion failed.
        """
        response_wrong_request = self.client.get(
            "?action=wrong_function&text=over the lake, I see the fish&word=lake"
        )
        assert response_wrong_request.status_code == 400
