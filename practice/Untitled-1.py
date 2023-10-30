def solution(n, money, events):
    answer = n

    def combination(current_customers, remaining_money, event_index, used_events):
        nonlocal answer

        if event_index == len(events):
            answer = max(answer, current_customers)
            return

        cost, value = events[event_index].split()
        cost = int(cost)

        if event_index not in used_events:
            if value.startswith("x"):
                multiplier = int(value[1:])
                if cost <= remaining_money:
                    new_customers = current_customers * multiplier
                    new_used_events = used_events + [event_index]
                    combination(new_customers, remaining_money - cost, event_index +1, new_used_events)

            elif value.startswith("+"):
                addition = int(value[1:])
                if cost <= remaining_money:
                    new_customers = current_customers + addition
                    new_used_events = used_events + [event_index]
                    combination(new_customers, remaining_money - cost, event_index + 1, new_used_events)

        combination(current_customers, remaining_money, event_index +1, used_events)

    combination(n, money, 0, [])

    return answer