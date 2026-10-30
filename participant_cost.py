def participant_cost(attendees, food_per_person, transport_per_person):
    return attendees * (food_per_person + transport_per_person)

# Test 1: Normal attendees
normal_attendee_count = participant_cost (10, 800, 200)
print(normal_attendee_count)

# Test 2: Zero attendees
zero_attendee_count = participant_cost (0, 800, 200)
print(zero_attendee_count)


#component: participant_cost
#returns: attendee, food per person, transport per person
#test: normal attendee count, zero attendee count
#issue: none

# https://github.com/okarasalvation/event_budget_helper.git