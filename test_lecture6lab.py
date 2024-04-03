import lecture6lab

def test_part1():
    politicians = [lecture6lab.Politician("Alice", 10), lecture6lab.Politician("Bob", 70)]
    assert politicians[0].name == "Alice"

def test_part2():
    voters = []
    for i in range(1, 101):
        voters.append(lecture6lab.Voter(i))
    assert voters[12].preferred_point == 13

def test_part3():
    politicians = [lecture6lab.Politician("Alice", 10), lecture6lab.Politician("Bob", 70)]
    voters = []
    for i in range(1, 101):
        voters.append(lecture6lab.Voter(i))
    assert voters[12].will_vote_for(politicians) == "Alice"

def test_part4():
    politicians = [lecture6lab.Politician("Alice", 10), lecture6lab.Politician("Bob", 70)]
    voters = []
    for i in range(1, 101):
        voters.append(lecture6lab.Voter(i))

    tally = {"Alice": 0, "Bob":0}    

    for voter in voters:
        politician_name = voter.will_vote_for(politicians)
        tally[politician_name] += 1

    assert tally["Alice"] == 40    