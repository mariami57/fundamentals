note = input()

note_list = []
while note != "End":
    note_list.append(note)

    note = input()

sorted_note = sorted(note_list,key=lambda x: int(x.split("-")[0]))
asc_notes = [note.split("-")[1] for note in sorted_note]

print(asc_notes)
