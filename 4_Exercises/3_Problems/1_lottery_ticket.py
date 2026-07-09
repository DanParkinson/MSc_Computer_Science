'''
PROBLEM
A lottery has 44 numbers to put on the ticket.
Tickets have 6 numbers on them.
A psychic can predict 15 numbers out of the total 44 that are used in the lottery. 
At least 4 of these numbers are guarenteed to be in the winning ticket.
how many tickets should they buy to guarantee at least 1 3 number win
'''

'''
THOUGHT PROCESS
None predicted numbers dont matter

lets say the predictions are [1-15]

to win, we only need tickets that have at least three predicted numbers in them.
But, because tickets are 6 numbers long, they can contain multiple sets of unique 3s that will win the lottery

e.g. if i buy [1,2,3,4,5,6]
contains combinations [1,2,3], [2,3,4], [1,5,6] for example

So if the winning ticket is [1,2,3,42,43,44], with any combination of none predicted numbers, I still have a three number win
so we no longer need to consider those triples for other tickets, as we already have them covrered. 

We need to find the tickets that cover the most amount of unique combinations of three

PSEUDOCODE
predicted_numbers = [1 - 15]

uncovered_triples = all unique combinations of 3 predicted numbers
candidate_tickets = all unique combinations of 6 predicted numbers

tickets_to_buy = []

WHILE uncovered_triples is not empty

    best_ticket = NONE
    best_score = 0

    FOR each candidate_ticket
        score = 0

        FOR each uncovered_triple
            IF uncovered_triple is contained in candidate_ticket
                score += 1

        END FOR

        IF score > best_score
            best_score = score
            best_ticket = candidate_ticket

    END FOR

    ADD best_ticket to tickets_to_buy

    REMOVE every triple covered by best_ticket
    FROM uncovered_triples

END WHILE


tickets_containing_triples = {}

FOR each original triple
    FIND every selected ticket that contains the triple
    STORE those tickets against the triple

END FOR


necessary_tickets = []

FOR each triple
    IF only one ticket contains the triple
        ADD that ticket to necessary_tickets
        IF it has not already been added

END FOR


RETURN necessary_tickets

'''

predicted_numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def generate_uncovered_triples():
    triples = []

    for i in range(len(predicted_numbers)):
        for j in range(i + 1, len(predicted_numbers)):
            for k in range(j + 1, len(predicted_numbers)):
                triple = (
                    predicted_numbers[i],
                    predicted_numbers[j],
                    predicted_numbers[k],
                )

                triples.append(triple)
    return triples


def generate_candidate_tickets():
    tickets = []

    for i in range(len(predicted_numbers)):
        for j in range(i + 1, len(predicted_numbers)):
            for k in range(j + 1, len(predicted_numbers)):
                for l in range(k + 1, len(predicted_numbers)):
                    for m in range(l + 1, len(predicted_numbers)):
                        for n in range(m+1, len(predicted_numbers)):
                            ticket = (
                                predicted_numbers[i],
                                predicted_numbers[j],
                                predicted_numbers[k],
                                predicted_numbers[l],
                                predicted_numbers[m],
                                predicted_numbers[n],
                            )

                            tickets.append(ticket)
    return tickets



def lottery_game():
    remaining_triples = generate_uncovered_triples()
    all_triples = remaining_triples.copy()
    candidate_tickets = generate_candidate_tickets()
    selected_tickets = []

    while len(remaining_triples) > 0:
        '''
        Create a dictionary of tickets with value: triples covered
        Keep the highest scoring ticket
        remove all triples that are covered from the ticket
        repeat until no triple remain

        '''

        best_ticket = None
        best_ticket_score = 0
        ticket_to_covered_triples = {}

        for candidate_ticket in candidate_tickets:
            ticket_to_covered_triples[candidate_ticket] = []
            covered_triple_count = 0

            for triple in remaining_triples:
                if set(triple).issubset(set(candidate_ticket)):
                    covered_triple_count += 1
                    ticket_to_covered_triples[candidate_ticket].append(triple)

            if covered_triple_count > best_ticket_score:
                best_ticket_score = covered_triple_count
                best_ticket = candidate_ticket

        selected_tickets.append(best_ticket)

        for covered_triple in ticket_to_covered_triples[best_ticket]:
            remaining_triples.remove(covered_triple)

        print(f"Triples remaining: {len(remaining_triples)}")

    triple_to_tickets = {}

    for triple in all_triples:
        '''
        dictionary of triples and the tickets that they are in
        '''
        triple_to_tickets[triple] = []

        for selected_ticket in selected_tickets:
            if set(triple).issubset(set(selected_ticket)):
                triple_to_tickets[triple].append(selected_ticket)

    essential_tickets = []

    for triple, covering_tickets in triple_to_tickets.items():
        '''
        Any triple that has a score of 1 means it is only contained on one ticket and is needed
        Only removes 1 on practice runs
        '''
        if len(covering_tickets) == 1:
            required_ticket = covering_tickets[0]

            if required_ticket not in essential_tickets:
                essential_tickets.append(required_ticket)

    print(essential_tickets)
    print(len(essential_tickets))


if __name__ == "__main__":
    print(lottery_game())

        

                



