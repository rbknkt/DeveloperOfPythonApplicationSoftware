# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, separator=','):
    participants_group_first = set(participants_first_group.split(separator))
    participants_group_second = set(participants_second_group.split(separator))
    common_participants = sorted(participants_group_first.intersection(participants_group_second))
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, separator='|'))

