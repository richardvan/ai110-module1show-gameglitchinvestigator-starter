from logic_utils import check_guess, parse_guess, update_score, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == ("Too High", "📉 Go LOWER!")

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == ("Too Low", "📈 Go HIGHER!")

def test_guess_by_one_high():
    # Boundary: guess is exactly one above the secret
    result = check_guess(51, 50)
    assert result == ("Too High", "📉 Go LOWER!")

def test_guess_by_one_low():
    # Boundary: guess is exactly one below the secret
    result = check_guess(49, 50)
    assert result == ("Too Low", "📈 Go HIGHER!")

def test_string_guess_equal_to_secret():
    # check_guess falls back to string comparison when types mismatch
    result = check_guess("50", "50")
    assert result == ("Win", "🎉 Correct!")


def test_guess_below_range_easy():
    # Easy range is 1-20; guessing 0 is below the floor
    result = check_guess(0, 10)
    assert result == ("Too Low", "📈 Go HIGHER!")

def test_guess_above_range_easy():
    # Easy range is 1-20; guessing 21 is above the ceiling
    result = check_guess(21, 10)
    assert result == ("Too High", "📉 Go LOWER!")

def test_guess_above_range_normal():
    # Normal range is 1-100; guessing 101 is above the ceiling
    result = check_guess(101, 50)
    assert result == ("Too High", "📉 Go LOWER!")

def test_guess_above_range_hard():
    # Hard range is 1-200; guessing 201 is above the ceiling
    result = check_guess(201, 150)
    assert result == ("Too High", "📉 Go LOWER!")

def test_non_numeric_input_returns_error_message():
    # Letters are not a valid guess; an error message should be returned
    outcome, message = check_guess("abc", 50)
    assert outcome == "Invalid"
    assert "number" in message.lower()


# --- bad inputs must not count as attempts (parse_guess returns ok=False) ---

def test_letters_do_not_count_as_attempt():
    ok, guess_int, err = parse_guess("abc", low=1, high=100)
    assert ok is False
    assert guess_int is None
    assert err is not None

def test_out_of_range_low_does_not_count_as_attempt():
    ok, guess_int, err = parse_guess("0", low=1, high=100)
    assert ok is False
    assert guess_int is None
    assert "1" in err and "100" in err

def test_out_of_range_high_does_not_count_as_attempt():
    ok, guess_int, err = parse_guess("101", low=1, high=100)
    assert ok is False
    assert guess_int is None
    assert "1" in err and "100" in err

def test_valid_guess_counts_as_attempt():
    # Only a valid in-range guess returns ok=True, which is when attempts increment
    ok, guess_int, err = parse_guess("50", low=1, high=100)
    assert ok is True
    assert guess_int == 50
    assert err is None


# --- update_score: one test per branch ---

def test_update_score_win_normal():
    # Win on attempt 1: points = 100 - 10*(1+1) = 80
    assert update_score(0, "Win", 1) == 80

def test_update_score_win_points_capped():
    # Win on attempt 9: points = 100 - 10*(9+1) = 0 → capped at 10
    assert update_score(0, "Win", 9) == 10

def test_update_score_too_high_even_attempt():
    # Too High on an even attempt number adds 5 points
    assert update_score(50, "Too High", 2) == 55

def test_update_score_too_high_odd_attempt():
    # Too High on an odd attempt number deducts 5 points
    assert update_score(50, "Too High", 3) == 45

def test_update_score_too_low():
    # Too Low always deducts 5 points
    assert update_score(50, "Too Low", 1) == 45

def test_update_score_unknown_outcome():
    # Unrecognised outcome leaves the score unchanged
    assert update_score(50, "Invalid", 1) == 50


# --- get_range_for_difficulty ---

def test_range_easy():
    assert get_range_for_difficulty("Easy") == (1, 20)

def test_range_normal():
    assert get_range_for_difficulty("Normal") == (1, 100)

def test_range_hard():
    assert get_range_for_difficulty("Hard") == (1, 200)
