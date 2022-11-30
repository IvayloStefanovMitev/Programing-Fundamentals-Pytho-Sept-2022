lst_notes = []
while True:
    command = input()
    if command == 'End':
        break
    to_do_notes = command.split('-')
    importance = int(to_do_notes[0])
    note = to_do_notes[1]
    lst_notes.append([importance, note])

sorted_notes = sorted(lst_notes)

notes = [note[1] for note in sorted_notes]
print(lst_notes)
print(notes)
