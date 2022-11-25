def test_soccer_match_assert(soccer_match):
    assert (
        soccer_match.original_record == "San Jose Earthquakes 3, Santa Cruz Slugs 3\n"
    )


#
# def test_soccer_match_snapshot(snapshot, soccer_match):
#     snapshot.assert_match(soccer_match, 'soccer_match_1')
